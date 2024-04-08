from decouple import config

env = config('ENV', default='development')

if env == 'development':
    from .dev import *
elif env == 'production':
    from .prod import *
else:
    from .base import *
