from rest_framework import serializers
from .models import BiopsyData, VarInfo


class BiopsyDataSerializer(serializers.ModelSerializer):
    qnum = serializers.IntegerField(required=False, min_value=1, max_value=30)
    class Meta:
        model = BiopsyData
        exclude = ["update_date"]


class VarInfoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = VarInfo
        exclude = ["update_date"]

