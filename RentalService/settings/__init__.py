import os

from .base import *

if os.environ.get('environment') == 'production':
    from .production import *
else:
    from .local import *
