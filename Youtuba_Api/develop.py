from .base import *     # base文件基类 这里修改开发时设置

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True