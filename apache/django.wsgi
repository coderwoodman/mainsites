import os 
import sys    

sys.path.append('/var/www/mainsites')     
os.environ['DJANGO_SETTINGS_MODULE'] = 'mainsites.settings'    

import django.core.handlers.wsgi  
application = django.core.handlers.wsgi.WSGIHandler()