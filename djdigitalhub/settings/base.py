import os
from decouple import config
from django.contrib.messages import constants as messages

################################
##     BASE CONFIGURATION     ##
################################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


################################
##  APPLICATION CONFIGURATION ##
################################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Installed App
    'memberships.apps.MembershipsConfig',
    'courses.apps.CoursesConfig',
    'instructors.apps.InstructorsConfig',
    # Thirdparty App
]


###############################
##  MIDDLEWARE CONFIGURATION ##
###############################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djdigitalhub.urls'

################################
##    APPLICATION TEMPLATES   ##
################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join( BASE_DIR, 'templates' )],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

################################
##      INTERNALIZATION       ##
################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


################################
##  STATIC FILE CONFIGURATION ##
################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets')]


################################
##      WSGI CONFIGURATION    ##
################################

WSGI_APPLICATION = 'djdigitalhub.wsgi.application'

################################
##  SECURITY CONFIGURATION    ##
################################

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False

################################
##   MESSAGE CONFIGURATION    ##
################################
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

try:
    from .ck_editor import *
except Exception as e:
    pass