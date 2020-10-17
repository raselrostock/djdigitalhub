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
    'accounts.apps.AccountsConfig',
    'courses.apps.CoursesConfig',
    'instructors.apps.InstructorsConfig',
    'memberships.apps.MembershipsConfig',
    'notifications.apps.NotificationsConfig',
    'pages.apps.PagesConfig',
    'quizes.apps.QuizesConfig',
    'search.apps.SearchConfig',
    'subscriptions.apps.SubscriptionsConfig',
    # Thirdparty App
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'haystack',
    'imagekit',
    'whoosh',
]


###############################
##  MIDDLEWARE CONFIGURATION ##
###############################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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
                'notifications.context_processors.notification_count',
            ],
        },
    },
]

################################
##      INTERNALIZATION       ##
################################

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

###############################
##    LOGIN CONFIGURATION    ##
###############################

LOGIN_REDIRECT_URL = 'memberships:dashboard'
LOGIN_URL = 'login'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

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

################################
##  LANGUAGE CONFIGURATION    ##
################################

LANGUAGE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('EN')),
    ('de', _('DE')),
)
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'de'
LOCALE_PATHS = [os.path.join(LANGUAGE_DIR, 'locale')]