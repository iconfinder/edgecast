from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from edgecast import *


# Fetch the credentials.
account_number = getattr(settings, 'EDGECAST_ACCOUNT_NUMBER', None)
token = getattr(settings, 'EDGECAST_TOKEN', None)

if not account_number:
    raise ImproperlyConfigured('EDGECAST_ACCOUNT_NUMBER is required.')
if not token:
    raise ImproperlyConfigured('EDGECAST_TOKEN is required.')

# Initialize the application-wide client.
client = Client(account_number=account_number,
                token=token)

__all__ = (
    'MEDIA_TYPE_FLASH_MEDIA_STREAMING',
    'MEDIA_TYPE_HTTP_LARGE_OBJECT',
    'MEDIA_TYPE_HTTP_SMALL_OBJECT',
    'MEDIA_TYPE_APPLICATION_DELIVERY_NETWORK',
    'client',
)
