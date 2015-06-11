from base import *

import dj_database_url

DEBUG = False

TEMPLATE_DEBUG = False 

# Parse database configuration from $DATABASE_URL

DATABASES = {'default': dj_database_url.config(),}
