web: gunicorn VincentRaia.wsgi

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_tutorial_blog_ng.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())