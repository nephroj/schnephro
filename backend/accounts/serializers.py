from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer


UserModel = get_user_model()
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'down_num'):
            extra_fields.append('down_num')
        if hasattr(UserModel, 'pdf_num'):
            extra_fields.append('pdf_num')
        if hasattr(UserModel, 'datatable_num'):
            extra_fields.append('datatable_num')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)
