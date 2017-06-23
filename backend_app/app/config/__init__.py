import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "set your key"
DEBUG = True
TESTING = True
NEW_CONFIG_VARIABLE = ''
WTF_CSRF_ENABLED = True
#CSRF_ENABLED = True
APP_SETTINGS="settings.DevelopmentConfig"
WTF_CSRF_SECRET_KEY = "set your key"