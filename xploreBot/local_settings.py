from .settings import *
# PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'xploreBot',
        'USER':'root',
        'PASSWORD':'Isandev2020.c0m',
        'HOST':'127.0.0.1',
        'PORT':'3306'
    }
}

