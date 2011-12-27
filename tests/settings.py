# coding: utf-8

import os

BASE = os.path.abspath(os.path.dirname(__file__))

STATIC_ROOT = os.path.normpath(os.path.join(BASE, "../static"))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.normpath(os.path.join(BASE, "../db.sqlite")),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST_CHARSET': 'utf8',
    },
}

INSTALLED_APPS = (
    'fileicons',
    'fileicons.tests',
)