import os
from unittest import TestCase
from edgecast import (Client, MEDIA_TYPE_HTTP_SMALL_OBJECT)


class ClientTestCase(TestCase):
    """Test case for :class:`Client`.
    """

    def setUp(self):
        self.cdn_domain = os.environ['EDGECAST_CDN_DOMAIN']
        self.client = Client(
            account_number=os.environ['EDGECAST_ACCOUNT_NUMBER'],
            token=os.environ['EDGECAST_TOKEN']
        )

    def test_purge(self):
        """Client(..).purge(..)
        """

        # Purging with no patterns.
        self.client.purge(MEDIA_TYPE_HTTP_SMALL_OBJECT)

        # Purging with one pattern.
        patterns = [
            'http://%s%s' % (self.cdn_domain, p) for p in [
                '/_testing',
                '/_testing/*',
            ]
        ]

        for pattern in patterns:
            self.client.purge(MEDIA_TYPE_HTTP_SMALL_OBJECT, pattern)

        # Purging with multiple patterns.
        self.client.purge(MEDIA_TYPE_HTTP_SMALL_OBJECT, *patterns)

    def test_load(self):
        """Client(..).load(..)
        """

        # Purging with no URLs.
        self.client.load(MEDIA_TYPE_HTTP_SMALL_OBJECT)

        # Purging with one URL.
        urls = [
            'http://%s%s' % (self.cdn_domain, p) for p in [
                '/_testing/a',
                '/_testing/b',
            ]
        ]

        for url in urls:
            self.client.load(MEDIA_TYPE_HTTP_SMALL_OBJECT, url)

        # Purging with multiple URLS.
        self.client.load(MEDIA_TYPE_HTTP_SMALL_OBJECT, *urls)


__all__ = (
    'ClientTestCase',
)
