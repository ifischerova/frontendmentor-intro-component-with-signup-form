import os
from form.settings import *
import dj_database_url

ALLOWED_HOSTS = ['frontendmentor-intro-component.herokuapp.com']

CSRF_TRUSTED_ORIGINS = ['https://frontendmentor-intro-component.herokuapp.com']

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

DEBUG = os.environ.get('DEBUG', None) == 'true'