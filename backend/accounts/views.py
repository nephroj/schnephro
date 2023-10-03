from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.jwt_auth import set_jwt_refresh_cookie
from dj_rest_auth.registration.views import RegisterView


class CustomRegisterView(RegisterView):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)

        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
            # 새로 추가함
            django_logout(request)
            if hasattr(self, "refresh_token"):
                set_jwt_refresh_cookie(response, self.refresh_token)
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response
