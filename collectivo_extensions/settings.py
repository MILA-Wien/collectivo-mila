"""Custom settings for MILA's instance of collectivo."""
from collectivo_app.settings import *


INSTALLED_APPS += [
    'collectivo_extensions.mila_members'
]

# TODO Find better solution
# Remove devtools because populate command uses
# the built-in members extension
INSTALLED_APPS.remove('collectivo.devtools')
