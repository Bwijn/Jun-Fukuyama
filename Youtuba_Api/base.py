import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^3%xy)$_tygx^7w%66vv075#f9p^fk4o_$wdp1jjalrroe1#2s'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig',
    'video.apps.VideoConfig',
    'rest_framework',
    'corsheaders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Youtuba_Api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Youtuba_Api.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# 使用自定义User验证类
AUTH_USER_MODEL = 'users.User'
# 自定义认证类
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# 配置 API 框架
REST_FRAMEWORK = {

    # 指定用于支持coreapi的Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    # "PAGE_SIZE": 2,  # 每页显示多少个
    # 允许 许可 权限
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    # 验证类 认证 token
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 将request.user赋值为 token解密后的对象 原本默认是匿名用户
    ),

    # 异常处理
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
CORS_ALLOW_CREDENTIALS = True

# CORS_ORIGIN_WHITELIST = (
#
# )
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

import datetime

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',  # response中token的payload部分处理函数
    # 'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',  # 解密token的方法 这里定义
    # Token失效时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),

    # 不过期
    'JWT_VERIFY_EXPIRATION': False,
}

# ---------------------------------静态文件
STATIC_URL = '/static/'
STATIC_ROOT = './static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "/static/"),  # 实际名，即实际文件夹的名字
]

