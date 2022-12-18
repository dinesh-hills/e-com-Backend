import configparser
from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-cow#v(+#fs)#d)c!f)mg-2kcshzd^s-@j#-rr6$k#z&5#i)hw)'


dbconf = configparser.ConfigParser()
dbconf.read('Ecom_store/postgres_db.conf')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': dbconf['DB']['dbname'],
        'USER': dbconf['DB']['user'],
        'PASSWORD': dbconf['DB']['password'],
        'HOST': dbconf['DB']['host'],
        'PORT': dbconf['DB']['port'],
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/1'
CELERY_BEAT_SCHEDULE = {
    'generate reports': {
        'task': 'trail.tasks.test_worker_task',
        'schedule': 5,
        'args': ['Test Hello'],
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}