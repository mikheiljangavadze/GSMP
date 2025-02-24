import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!)j2m=3v6&4t*&$i(%h@=i^c)jvyn_z__9yuj-&nl&6u9j9of='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    '127.0.0.1',
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gsmp.apps.GsmpConfig',
    'members.apps.MembersConfig',
    'mp_news.apps.MpNewsConfig',
    'debug_toolbar',
    'rosetta',
    'django_countries',
    'tinymce',
    'online_encyclopedia.apps.OnlineEncConfig',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'gsmpsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'gsmp.context_processors.breadcrumb_processor',

            ],
        },
    },
]

WSGI_APPLICATION = 'gsmpsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'ka'
LANGUAGES = [
    ('ka', 'ქართული'),
    ('en', 'English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'mp_news/static'),
        os.path.join(BASE_DIR, 'online_encyclopedia/static'),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'gsmp:home'
LOGOUT_REDIRECT_URL = 'gsmp:home'
LOGIN_URL = 'members:login'



AUTH_USER_MODEL = 'members.GsmpMember'
DEFAULT_USER_IMAGE = MEDIA_URL + 'members/default.png'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'members.authentication.EmailAuthBackend',
]




# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


EMAIL_HOST = "mail.gsmp.ge"
EMAIL_PORT = 465
EMAIL_HOST_USER = "info@gsmp.ge"
EMAIL_HOST_PASSWORD = "gelati1977"
EMAIL_USE_SSL = True


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
    }
}


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


# TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    # "language": "es_ES",  # To force a specific language instead of the Django current language.
}
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True
# TINYMCE_EXTRA_MEDIA = {
#     'css': {
#         'all': [
#             ...
#         ],
#     },
#     'js': [
#         ...
#     ],
# }



COUNTRIES_FIRST = [ 'GE', 'US', 'GB' ]
COUNTRY_DEFAULT = 'GE'