"""
Django settings for eventex project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.utils import six
from decouple import config, Csv
from dj_database_url import parse as dburl

from boto.s3.connection import OrdinaryCallingFormat

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR        = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT    = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS',default=[], cast=Csv())

DEFAULT_FROM_EMAIL = 'contato@cinepro.com'
DEFAULT_TO_EMAIL = 'contato@cinepro.com'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_without_migrations',
    'django_extensions',
    'stdimage',
    #'watermarker',
    'webapp.core',
    #'webapp.core.apps.CoreConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

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
                'webapp.core.context_processors.empresa',
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#PREPEND_WWW = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL          = '/static/'
STATIC_ROOT         = os.path.join(BASE_DIR, 'staticfiles')

#MEDIA_URL           = '/media/'
#MEDIA_ROOT          = os.path.join(BASE_DIR,'media')

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

USE_S3 = config('USE_S3', cast=bool)

if USE_S3:

    INSTALLED_APPS += (
        'storages',
    )

    AWS_ACCESS_KEY_ID = config('DJANGO_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('DJANGO_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('DJANGO_AWS_STORAGE_BUCKET_NAME')
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIRY = 60 * 60 * 24 * 7

    # TODO See: https://github.com/jschneier/django-storages/issues/47
    # Revert the following and use str after the above-mentioned bug is fixed in
    # either django-storage-redux or boto
    AWS_HEADERS = {
        'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY, AWS_EXPIRY))
    }

    STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
    STATIC_ROOT = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME

    MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    MEDIA_ROOT = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_STORAGE = 'webapp.s3utils.StaticRootS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'webapp.s3utils.MediaRootS3BotoStorage'

# Email configuration
EMAIL_BACKEND       = config('EMAIL_BACKEND')
EMAIL_HOST          = config('EMAIL_HOST')
EMAIL_PORT          = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS       = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER     = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')