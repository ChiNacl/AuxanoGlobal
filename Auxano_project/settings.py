"""
Django settings for Auxano_project project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'b&7b7&8_s!a86debwfnrd%im8vc8i+t7qf$ec1f!i6*fpn2jit'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'b&7b7&8_s!a86debwfnrd%im8vc8i+t7qf$ec1f!i6*fpn2jit')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = ['https://auxanoglobal.herokuapp.com/', '127.0.0.1', 'localhost']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = 'same-origin'


INSTALLED_APPS = [
    'auxano.apps.AuxanoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Auxano_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Auxano_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'auxanodb',
#         'PORT': '5432',
#         'USER': 'postgres',
#         'PASSWORD': 'maria',
#         'HOST': '127.0.0.1',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7hs8cro6g4qip',
        'PORT': '5432',
        'USER': 'fmrgyfwajphuxk',
        'PASSWORD': '7ba984876ae379f084e2cc8cedce4ec399ba93dda8eb1797a64f7479a042fd6d',
        'HOST': 'ec2-3-217-14-181.compute-1.amazonaws.com',
    }
}

# postgresql-flat-05309
# db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Auxano_project/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

import dj_database_url

DATABASE_URL = 'postgres://fmrgyfwajphuxk:7ba984876ae379f084e2cc8cedce4ec399ba93dda8eb1797a64f7479a042fd6d@ec2-3-217-14-181.compute-1.amazonaws.com:5432/d7hs8cro6g4qip'
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True, default=DATABASE_URL)

import django_heroku

django_heroku.settings(locals())

# DATABASES['default'].update({'conn_max_age':600, 'ssl_require': True})

