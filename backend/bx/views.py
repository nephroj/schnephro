from django.shortcuts import render
from django.db import models
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from .serializers import *
from .models import *
from backend.utils import *

import csv
import io


class AnswerViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerUserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def get_queryset(self):
        user = self.request.user
        return Answer.objects.filter(doctor=user)


class AnswerUserQnumAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def get(self, *args, **kwargs):
        qnum = kwargs["qnum"]
        setn = kwargs["setn"]

        user = self.request.user
        if setn == 999:
            qset = (user.id + user.retry ) % 3
        else:
            qset = (user.id + setn ) % 3
        
        obj = Answer.objects.filter(qsetnum=qset, doctor=user).filter(qnum=qnum)
        if obj:
            answers = obj.values()[0]
        else:
            answers = {}
            
        return Response(answers)


class QuestionViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        user = self.request.user
        user_id = user.id
        qset = (user_id + user.retry) % 3

        return Question.objects.filter(qset=qset).all()    


class QuestionIdAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        qid = kwargs["qid"]
        setn = kwargs["setn"]

        user = self.request.user
        if setn == 999:
            qset = (user.id + user.retry ) % 3
        else:
            qset = (user.id + setn ) % 3

        qdicts = Question.objects.filter(qset=qset, qid=qid).values()
        qdict0 = qdicts[0]

        day_limit = 11
        max_day = len(qdicts)
        if max_day > day_limit:
            qdicts = qdicts[max_day-day_limit:max_day]       
   
        def reorganize(qdicts): 
            vars = VariableInfo.objects.filter(Q(type="vital")|Q(type="lab")|Q(type="risk_factor")).values_list('abbr', flat=True)
            new_dicts = {}
            for var in vars:
                var_values = []
                for qdict in qdicts:
                    value = qdict[var]
                    if value and var in ["eGFR", "BST"]:
                        result = round(value)
                    else:
                        result = value
                    var_values.append(result)
                new_dicts[var] = var_values
            return new_dicts

        data = reorganize(qdicts)

        final = {
            "user_id": user.id,
            "retry": user.retry,
            "qset": qset,
            "qid": qid,
            "max_day": max_day,
            "day_limit": day_limit,
            "age_adm": qdict0["age_adm"],
            "sex": qdict0["sex"],
            "dept": qdict0["dept"],
            "BMI": qdict0["BMI"],
            "diagnosis": qdict0["diagnosis"],
            "predict": qdict0["predict"],
            "probability": qdict0["probability"],
            "non_recovery": qdict0["non_recovery"],
            "data": data            
        }
        return Response(final)


## Variable Info
class VariableInfoViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = VariableInfo.objects.all()
    serializer_class = VariableInfoSerializer

class VariableInfoWriteViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = VariableInfo.objects.all()
    serializer_class = VariableInfoSerializer


## CSV 파일 upload
class UploadDataViewSet(ViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = UploadDataSerializer

    def list(self, request):
        return Response("csv 파일을 업로드해 주세요.")
    
    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type

        # 만약 CSV 파일이 아니라면 ERROR
        if "csv" not in content_type:
            return Response("CSV 형식으로 업로드해 주세요.")
        
        # Read csv file InMemoryUploadedFile
        file = file_uploaded.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))

        # Generate a list comprehension
        dicts = [line for line in reader if line["qid"] != ""]
        dict_keys = list(dicts[0].keys())

        # get field type from Model
        model_fields = Question._meta.get_fields()
        fields_name = [field.name for field in model_fields if field.name not in ["update_date", "id"]]
        fields_missing = [fname for fname in fields_name if fname not in dict_keys]
        
        # model fields에 있는 변수가 csv 파일에 없다면 ERROR
        if fields_missing:
            missed = ", ".join(fields_missing)
            return Response(f"{missed} 변수를 더 추가해주세요.")
        
        # TODO: dicts의 column에 중복 변수 있을 시 ERROR -> 작동 안 함
        dict_key_dupl = set([x for x in dict_keys if dict_keys.count(x) > 1])
        if dict_key_dupl:
            duplicated = ", ".join(dict_key_dupl)
            return Response(f"{duplicated} 변수가 중복되어 존재합니다.")            
        
        int_list = []
        float_list = []
        char_list = []
        for model_field in model_fields:
            if isinstance(model_field, models.IntegerField):
                int_list.append(model_field.name)
            elif isinstance(model_field, models.FloatField):
                float_list.append(model_field.name)
            elif isinstance(model_field, models.CharField):
                char_list.append(model_field.name)
        
        # Change data type from field type information
        for dict0 in dicts:
            for key in dict_keys:
                if dict0[key].lower() in ['', "nan", "na"]:
                    dict0[key] = None
                elif key in int_list:
                    dict0[key] = int(dict0[key])
                elif key in float_list:
                    dict0[key] = float(dict0[key])
                elif key not in fields_name:
                    return Response(f"{key} 변수는 db에 없습니다.")

        new_dicts = [Question(**item) for item in dicts]
        Question.objects.all().delete()
        Question.objects.bulk_create(new_dicts)


        # 변수 정보 등록
        var_info = VariableInfo.objects.values()       
        var_list = [item["abbr"] for item in var_info]
        order_max = max([item["order"] for item in var_info]) if var_info else 0
        n = order_max
        for field in fields_name:
            if field not in var_list:
                n += 1
                info = {
                    "order": n,
                    "abbr": field,
                    "name": "",
                    "unit": "",
                    "lower": 0,
                    "upper": 0,
                    "type": "",
                }
                item = VariableInfo(**info)
                item.save()

        return Response(f"{content_type}을 성공적으로 업로드하였습니다.")
    

class UploadVariableInfoViewSet(ViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = UploadDataSerializer

    def list(self, request):
        return Response("csv 파일을 업로드해 주세요.")
    
    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type

        # 만약 CSV 파일이 아니라면 ERROR
        if "csv" not in content_type:
            return Response("CSV 형식으로 업로드해 주세요.")
        
        # Read csv file InMemoryUploadedFile
        file = file_uploaded.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))

        dicts = reader
        new_dicts = [VariableInfo(**item) for item in dicts]
        VariableInfo.objects.all().delete()
        VariableInfo.objects.bulk_create(new_dicts)

        return Response(f"{content_type}을 성공적으로 업로드하였습니다.")