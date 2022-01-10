from .default import *

DEBUG = eval(os.environ.get('DEBUG', 'True'))

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'automatica',
        'USER': 'automatica',
        'PASSWORD': 'automatica',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
