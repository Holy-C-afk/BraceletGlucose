"""
WSGI config for diabetes_bracelet project.
"""

import os
from django.core.wsgi import get_wsgi_application
import sys
from decouple import config

sys.path.append('c:/Users/tachf/BARCELETGLUCOSE')  # Add the project directory to the Python path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_bracelet.settings')

application = get_wsgi_application()