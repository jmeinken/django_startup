"""
INSTRUCTIONS:

settings_global.py
- stored in github with the project and should have something
for all relevant settings, even if that is just a comment.

settings.py
- excluded from github; import settings_global.py and then override anything
that is private (like passwords) or needs to be customized for this instance

settings_production.py
- excluded from github; import settings.py and then
  override anything that needs to be customized for this service (usually URL-related)
  and turn off DEBUG
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY ##############################################################

# you must add a SECRET_KEY in your settings file
# SECRET_KEY = 'add_secret_key'
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8008",
]

ADMINS = [
    ("John", "john.meinken@cchmc.org"),
]

# FILE STRUCTURE ####################################################

sys.path.append("../")
sys.path.append("../django_user_manager/")

WSGI_APPLICATION = "project.wsgi.application"

ROOT_URLCONF = "project.urls"

STATIC_URL = "/static/"
STATIC_ROOT = "/_static"

# APP SETUP ###########################################################

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "user_manager",
    "main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # 'user_manager.middleware.ChiAuthLoginMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "project.context_processors.settings_context_processor",
                "user_manager.context_processors.settings_context_processor",
            ],
        },
    },
]

# DATABASES ###############################################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# for multi-database systems, add your database router
# DATABASE_ROUTERS = ['project.routers.CustomDatabaseRouter']

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# AUTHENTICATION ########################################################

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "user_manager.authentication_backends.ChiAuthBackend",
]

AUTH_USER_MODEL = "user_manager.User"

# this url gets called when @login_required view is accessed
LOGIN_URL = "/user_manager/login"
# use as a sign in link <a href="{{ LOGIN_URL_FOR_LINK }}">Sign In</a>
LOGIN_URL_FOR_LINK = "/user_manager/login"
# use as a sign out link <a href="{{ LOGOUT_URL_FOR_LINK }}">Sign Out</a>
LOGOUT_URL_FOR_LINK = "/user_manager/logout"

# set CHI_AUTH url and access token if you want to accept CHI_AUTH passwords (default)
# CHI_AUTH_API_ACCESS_TOKEN = 'get_access_token'
# CHI_AUTH_URL = 'https://chi-dev.uc.edu/auth/'
# CHI_AUTH_AUTOCREATE_CHI_AUTH_USER = False
# CHI_AUTH_AUTOCREATE_LOCAL_USER = False
# CHI_AUTH_CHECK_SYSTEMS = 'local, ucad'

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization #######################################################

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_L10N = False
USE_TZ = False
DATE_FORMAT = "m/d/Y"

# SITE GENERAL CONFIGURATION #################################################

SITE_TITLE = "My Website"
SITE_CONTACT_EMAIL = "john.meinken@cchmc.org"

CRISPY_TEMPLATE_PACK = "bootstrap4"

# for systems using redcap_importer, set API tokens
# REDCAP_API_TOKENS = {
#         "myproject": "mytoken",
# }
