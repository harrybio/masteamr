# Add to settings.py manually:

import os, dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-local-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get(
            'DATABASE_URL',
            'postgresql://neondb_owner:npg_KFG76wlbMYim@ep-rapid-tooth-adrany32-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
        ),
        conn_max_age=600,
        ssl_require=True
    )
}

INSTALLED_APPS += ['corsheaders']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
] + MIDDLEWARE

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')
