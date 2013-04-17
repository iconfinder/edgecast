import requests
import json


MEDIA_TYPE_FLASH_MEDIA_STREAMING = 2
"""Flash Media Streaming media type.
"""

MEDIA_TYPE_HTTP_LARGE_OBJECT = 3
"""HTTP Large Object media type.
"""

MEDIA_TYPE_HTTP_SMALL_OBJECT = 8
"""HTTP Small Object media type.
"""

MEDIA_TYPE_APPLICATION_DELIVERY_NETWORK = 14
"""Application Delivery Network media type.
"""


class Client(object):
    """EdgeCast CDN client.
    """

    def __init__(self,
                 account_number,
                 token):
        """Initialize an EdgeCast CDN client.

        :param account_number: Account number
        :param token: Token.
        """

        self.account_number = account_number
        self.token = token

        self._session = requests.Session()

    def _request(self,
                 endpoint_method,
                 method,
                 data):
        """Perform a request.

        :param endpoint_method: Endpoint method such as ``purge``.
        :param method: Request method.
        :param data: JSON request data.
        """

        response = self._session.request(
            method,
            'https://api.edgecast.com/v2/mcc/customers/%s/edge/%s' % (
                self.account_number,
                endpoint_method,
            ),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'TOK:%s' % (self.token),
            },
            data=json.dumps(data)
        )

        response.raise_for_status()

    def purge(self, media_type, *patterns):
        """Purge one or more resources from the CDN.

        :param media_type: Media type.
        :param \*patterns: CDN URLs or patterns.
        """

        for pattern in patterns:
            self._request('purge',
                          'PUT',
                          {'MediaPath': pattern, 'MediaType': media_type})

    def load(self, media_type, *urls):
        """Load one or more resources into the CDN.

        :param media_type: Media type.
        :param \*urls: URLs from which to load the resources.
        """

        for url in urls:
            self._request('load',
                          'PUT',
                          {'MediaPath': url, 'MediaType': media_type})


__all__ = (
    'MEDIA_TYPE_FLASH_MEDIA_STREAMING',
    'MEDIA_TYPE_HTTP_LARGE_OBJECT',
    'MEDIA_TYPE_HTTP_SMALL_OBJECT',
    'MEDIA_TYPE_APPLICATION_DELIVERY_NETWORK',
    'Client',
)
