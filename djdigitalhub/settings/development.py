from .base import *
import os

################################
##     BASE CONFIGURATION     ##
################################

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

################################
##    DATABASE CONFIGURATION  ##
################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

##############################
##  HAYSTACK CONFIGURATION  ##
##############################

from django.utils.translation import ugettext_lazy as _
WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh/')
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

###############################
##   CKEDITOR CONFIGURATION  ##
###############################
try:
    from .ck_editor import *
except Exception as e:
    pass

###############################
##    LOGGER CONFIGURATION   ##
###############################
try:
    from .logger_settings import *
except Exception as e:
    pass

###############################
##   MAILGUN CONFIGURATION   ##
###############################

MAILGUN_API_KEY = config('MAILGUN_API_KEY')
ENCRYPT_KEY = b'i_D8bT2mswqAleNqCAUqRfcxsii4dQRLJk8-E1W0oow='

###############################
##    STRIPE CONFIGURATION   ##
###############################

STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')

################################
##  LANGUAGE CONFIGURATION    ##
################################
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', _('EN')),
    ('de', _('DE')),
)
# LANGUAGE_CODE = 'de'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]