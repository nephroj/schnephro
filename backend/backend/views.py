from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, Max
from django.contrib.auth import forms
from django.contrib.auth import logout as django_logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.jwt_auth import set_jwt_refresh_cookie
from dj_rest_auth.registration.views import RegisterView

import logging

from .utils import get_client_ip


class SetLoggingAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        level = request.data["level"]
        message = request.data["message"]
        logger = logging.getLogger("backend")

        if level == "INFO":
            logger.info(f'{request.user} | {get_client_ip(request)} | {message}')
            return Response("INFO log를 기록하였습니다.")
        elif level == "WARNING":
            logger.warning(f'{request.user} | {get_client_ip(request)} | {message}')
            return Response("WARNING log를 기록하였습니다.")
        elif level == "ERROR":
            logger.error(f'{request.user} | {get_client_ip(request)} | {message}')
            return Response("ERROR log를 기록하였습니다.")
        elif level == "CRITICAL":
            logger.critical(f'{request.user} | {get_client_ip(request)} | {message}')  
            return Response("CRITICAL log를 기록하였습니다.")   
        else:
            return Response("Level을 정확히 전달해 주세요.")   

 
