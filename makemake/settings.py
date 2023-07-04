from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY", default="django-insecure")

DEBUG = config("DEBUG", default=False)

ALLOWED_HOSTS = ["*", "*.makemake.rw"]
MODE = config("MODE", default="dev")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django.forms",
    "user",
    "index",
    # AllAuth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "makemake.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "makemake.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = "assets"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

AUTH_USER_MODEL = "user.User"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# All Auth SETTINGS
SIGNUP_FORM_CLASS = "user.forms.CreateUserForm"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "required"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_FORM_CLASS = SIGNUP_FORM_CLASS
ACCOUNT_LOGIN_ON_EMAIL_COMFIRMATION = False
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Make Make |"

# Email configurations

DEFAULT_FROM_EMAIL = "no-reply@makemake.rw"


# Production settings

CSRF_TRUSTED_ORIGINS = [
    "https://*.makemake.rw",
    "http://*.makemake.rw",
]

if MODE == "production":
    EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
    ANYMAIL = {
        "MAILJET_API_KEY": config("MAILJET_API_KEY", default=""),
        "MAILJET_SECRET_KEY": config("MAILJET_SECRET_KEY", default=""),
    }
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    STATIC_ROOT = "/home/certqgcy/makemake.rw/static"
    STATIC_ROOT = "/home/certqgcy/makemake.rw/media"
