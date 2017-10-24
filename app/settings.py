"""
Django settings for testP project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET', ')6+vf9(1tihg@u8!+(0abk+y*#$3r$(-d=g5qhm@1&lo4pays&')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not os.environ.get('PROD_MODE', None)

ALLOWED_HOSTS = ['localhost', 'my.hackupc.com', '127.0.0.1', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'form_utils',
    'bootstrap3',
    'organizers',
    'checkin',
    'reimbursement',
    'table',
    'user',
    'hackers'
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['app/templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.environ.get('PG_PWD', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('PG_NAME', 'backend'),
            'USER': os.environ.get('PG_USER', 'backenduser'),
            'PASSWORD': os.environ.get('PG_PWD'),
            'HOST': os.environ.get('PG_HOST', 'localhost'),
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/staticfiles'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, os.path.join('app', "static")),
]

SENDGRID_API_KEY = os.environ.get('SG_KEY', None)
# Load filebased email backend if no Sendgrid credentials and debug mode
if not SENDGRID_API_KEY and DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'tmp/email-messages/'
else:
    EMAIL_BACKEND = "sgbackend.SendGridBackend"

# Jet configs
JET_SIDE_MENU_COMPACT = True
JET_INDEX_DASHBOARD = 'app.jet_dashboard.CustomIndexDashboard'

# Set up custom auth
AUTH_USER_MODEL = 'user.User'
LOGIN_URL = 'account_login'

# Reimbursement configuration
DEFAULT_REIMBURSEMENT = 100
DEFAULT_CURRENCY = '$'
DEFAULT_EXPIRACY_DAYS = 5

BOOTSTRAP3 = {
    # Don't normally want placeholders.
    'set_placeholder': False,
}

# Hackathon specific configuration
HACKATHON_NAME = 'HackUPC'
HACKATHON_DOMAIN = os.environ.get('DOMAIN', 'localhost:8000')
ALLOWED_HOSTS.append(HACKATHON_DOMAIN)

DEFAULT_FROM_EMAIL = 'HackUPC Team <contact@hackupc.com>'
REIMBURSEMENT_EMAIL = 'HackUPC Reimbursements Team <reimbursement@hackupc.com>'

# Loaded on email templates (except auth ones)
STATIC_KEYS_TEMPLATES = {
    'fb': 'hackupc',
    'twitter': 'hackupc',
    'email': 'contact@hackupc.com',
    'description': 'Join us for BarcelonaTech\'s hackathon. 700 hackers. 36h. October 13th-15th.',
    # Static url to your logo
    'logo_url': 'https://my.hackupc.com/static/logo.png',
    # MailChimp subscribe URL (optional)
    'subscribe_url': '//hackupc.us12.list-manage.com/subscribe/post?u=d49fc444ec7d45ce418dc02d2&amp;id=3aeef9df9d',
    # Live page url
    'live_url': 'https://hackupc.com/live',
    # Issues url, shows up on 500 error
    'issues_url': 'https://github.com/hackupc/backend/issues/new',
    # Regex to match possible organizers emails
    'r_organizer_email': '^.*@hackupc\.com$',
    'google_analytics': 'UA-69542332-2',
    'when_to_arrive': 'Registration opens at 3:00 PM and closes at 6:00 PM on Friday October 13th, '
                      'the opening ceremony will be at 7:00 pm.',
    'when_to_leave': 'Closing ceremony will be held on Sunday October 15th from 3:00 PM to 5:00 PM. '
                     'However the projects demo fair will be held in the morning from 10:30 AM to 1 PM.',
    'applications_open': True,

}

EMAIL_SUBJECT_PREFIX = '[HackUPC]'
EVENT_NAME = 'HackUPC'

EVENT_DOMAIN = os.environ.get('DOMAIN', 'localhost:8000')
ALLOWED_HOSTS.append(EVENT_DOMAIN)
CURRENT_EDITION = 'Fall 2017'

# Optional, if not set will skip invite.
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'hackupctest'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

# Default reimbursement amount, optional, will have empty value if no amount

if os.environ.get('EMAIL_HOST_PASSWORD', None):
    # Error reporting email. Will send an email in any 500 error from server email
    SERVER_EMAIL = 'server@hackupc.com'
    ADMINS = [('Devs', 'devs@hackupc.com'), ]
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.sendgrid.net')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'hupc_mail')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
