from .base import *  # NOQA

DEBUG = True
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # NOQA
