from pathlib import Path
import os
import environ
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environ file
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    DEV=(bool, False)
)
# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = env("SECRET_KEY") 
DEBUG = int(env("DEBUG", default=0))
ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")
SITE_ID = int(env("SITE_ID", default=1))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    "rest_framework_simplejwt.token_blacklist",
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'accounts',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("MYSQL_DATABASE"),
        'USER': env("MYSQL_USER"), 
        'PASSWORD': env("MYSQL_PASSWORD"),
        'HOST': env("MYSQL_HOST"), 
        'PORT': env("MYSQL_PORT"), 
    }
} 

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]
if not int(env("DEV")): 
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (   
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S", 
}


# Authentication
AUTH_USER_MODEL = 'accounts.CustomUser'

REST_AUTH = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.CustomUserDetailsSerializer',

    "USE_JWT": True,
    # "JWT_AUTH_COOKIE": 'access_token',
    "JWT_AUTH_REFRESH_COOKIE": 'refresh_token',
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_COOKIE_USE_CSRF': True,
    "SESSION_LOGIN": False
}
REST_AUTH['JWT_AUTH_SECURE'] = True if int(env("HTTPS")) else False

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    # 'ACCESS_TOKEN_LIFETIME': timedelta(seconds=10),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(seconds=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}


## CORS settings
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(" ")

CORS_URLS_REGEX = r'^/api.*'
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = env("CSRF_TRUSTED_ORIGINS").split(" ")


# SSL
if int(env("HTTPS")):
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
FILE_UPLOAD_PERMISSIONS=0o640


# Email
if int(env("DEV")):
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_USE_TLS = int(env("EMAIL_USE_TLS"))
    EMAIL_HOST = env("EMAIL_HOST")
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = int(env("EMAIL_PORT"))
    DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")


## Logging
FILE_BACKEND = os.path.join(BASE_DIR, 'log/backend.log')
FILE_ERROR = os.path.join(BASE_DIR, 'log/error.log')
 
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'formatters': {
        'verbose': {
            'format': "%(asctime)s (%(levelname)s) %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
 
    'handlers': {
        # 개발 환경에서 console 출력
        'console': {
            'level': 'INFO',
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        # Error or Warning 상황은 error.log 파일에 기록
        'file_error': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': FILE_ERROR,
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'encoding': 'utf-8',
        },
        # backend작동은 backend.log에 기록
        'file_backend': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': FILE_BACKEND,
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'encoding': 'utf-8',
        },
    },
 
    'loggers': {
        'django': {
            'handlers': ['console', 'file_error'],
            'propagate': False,
        },
        'backend': {
            'handlers': ['file_backend'],
            'propagate': False,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },   
    }
}