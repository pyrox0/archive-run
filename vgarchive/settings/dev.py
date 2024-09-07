from vgarchive.settings.common import *

from vgarchive.settings import common

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5pvrv(*#6@e=sk3&=zt6znv^0#9(b+5weaws_6et&fuph3*n#6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = common.INSTALLED_APPS + [
    "django.contrib.staticfiles",
    # Admin shell
    "django_admin_shell",
    # Hot reload
    "django_browser_reload",
]

MIDDLEWARE = common.MIDDLEWARE + [
    # Hot reload
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db/vgarchive.db",
    }
}

# django.contrib.staticfiles
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")
