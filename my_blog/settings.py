"""
Django settings for my_blog project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*cpb_z0x^8hq#6&$62go=%tg%$j0r8#20xxrcmu3j6-+-b08y2'
SECRET_KEY_2 = 'asdasds'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_elasticsearch_dsl',
    'ckeditor',
    'ckeditor_uploader',
    'rest_api',
    'apps.user',
    'apps.publications',
    'rest_framework',
    'apps.comment',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': "django.db.backends.postgresql",
            'NAME': 'my_blog',
            "USER": "postgres",
            "PASSWORD": "",
            'HOST': 'localhost',
            'PORT': '5432',
        }
}

ELASTICSEARCH_DSL={
    'default': {
        'hosts': '127.0.0.1:9200'
    },
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 'auto',
    },
}

CKEDITOR_BASEPATH = os.path.join('','public/static/ckeditor')
CKEDITOR_UPLOAD_PATH =  os.path.join("uploads/")

CKEDITOR_IMAGE_BACKEND = "pillow"
# Куда вносятся изменения, с помощью команды collectstatic изменения переносятся в основную папку public откуда уже подключаются к файлам html
STATICFILES_DIRS = (
    os.path.join('', 'assets'),
)

# Абсолютный путь к каталогу, в который collectstatic соберет все статические файлы.
STATIC_ROOT = os.path.join('', 'public/static')
MEDIA_ROOT = os.path.join('', 'public/media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'