from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.auth import views, forms
from rest_framework import routers

from .views import SetLoggingAPIView
from accounts.views import CustomRegisterView

router = routers.DefaultRouter()
# router.register('question', QuestionViewSet, basename='question')


urlpatterns = [

    # API
    path('api/', include(router.urls)),
    path('api/setlogging/', SetLoggingAPIView.as_view(), name="set-logging"),

    # path('api/author-summary/<int:pmid>/', AuthorSummaryAPIView.as_view(), name="author-summary"),
    # path('api/abstract-summary/<int:pmid>/', AbstractSummaryAPIView.as_view(), name="abstract-summary"),

    # Admin
    path('schadmin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/custom-register/', CustomRegisterView.as_view(), name="custom-register"),
    # path('dj-rest-auth/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    # path('dj-rest-auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    # path('password-reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Reactjs
    re_path('.*', TemplateView.as_view(template_name='react.html')),
    path('password-reset/<uidb64>/<token>/', TemplateView.as_view(template_name='react.html'), name='password_reset_confirm'),

]
