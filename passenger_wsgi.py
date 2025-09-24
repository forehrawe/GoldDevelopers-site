import os
import sys

PROJECT_DIR = '/home/cp63894136337/GoldDevelopers/'

sys.path.insert(0, PROJECT_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'


try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception as e:
    with open('err.txt', 'w') as f:
        f.write(str(e))