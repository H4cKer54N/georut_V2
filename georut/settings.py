import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-&f@_*j80aiak0%_xdruj=^ntwr$dy+_3#5g$wpds-_hs3gk57k'

DEBUG = True
if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ['georut.com', 'www.georut.com','localhost']

# Application definition

INITIAL_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

THIRD_PARTY_APPS = [
    'simple_history',  # app para auditar cambios en los modelos
    'axes',  # app para bloquear intentos de acceso
]

CREATED_APPS = [
    # 'Articles',
    # 'Categories',
    # 'Clients',
    # 'Iva',
    # 'Orders',
    'Users',
    'index',  # app para la página de inicio
    'globalconfig',  # app para configuración global
    # 'Vehicles',
    # 'Warehouse',

]
INSTALLED_APPS = INITIAL_APPS + THIRD_PARTY_APPS + CREATED_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'axes.middleware.AxesMiddleware',
    'Users.middleware.CaptureIPMiddleware',

]

ROOT_URLCONF = 'georut.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'globalconfig.context_processors.context_configuration'
            ],
        },
    },
]

WSGI_APPLICATION = 'georut.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_GROUP_MODEL = 'Users.CustomGroup'


LANGUAGES = (
    ('es', _('Español')),
    ('it', _('Italian')),
    ('en', _('English')),
)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'Users:login'
LOGIN_URL = 'Users:login'

AXES_FAILURE_LIMIT = 10
AXES_COOLOFF_TIME = .10
AXES_LOCK_OUT_AT_FAILURE = True

AUTH_USER_MODEL = "Users.User"
SIMPLE_HISTORY_ENFORCE_HISTORY_MODEL_PERMISSIONS = True

