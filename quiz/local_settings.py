import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$b*4p*)ce#7_4=2ho#=-(_(3i$ulf6766n-neagu7$n3mpfe8z'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'new_quiz',
        'USER': 'postgres',
        'PASSWORD': '0305post',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


DEBUG = True