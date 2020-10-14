from .base import *

env = environ.Env()
env.read_env(str(BASE_DIR('.env.local')))
DEBUG = env('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        }
}

STATIC_URL = env('STATIC')