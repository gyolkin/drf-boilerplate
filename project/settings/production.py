from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = os.getenv("CORS_ORIGIN_WHITELIST", "").split(",")

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", default="engine"),
        "NAME": os.getenv("DB_NAME", default="name"),
        "USER": os.getenv("POSTGRES_USER", default="user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="password"),
        "HOST": os.getenv("DB_HOST", default="host"),
        "PORT": os.getenv("DB_PORT", default="port"),
    }
}

STATIC_ROOT = BASE_DIR / "static"
