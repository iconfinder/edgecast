edgecast -- convenient EdgeCast CDN management
==============================================

The EdgeCast CDN exposes a RESTful API for forcefully loading and purging content from your CDN hosts. The ``edgecast`` module provides a simple interface for performing those actions.

Furthermore, the ``django_edgecast`` module provides a convient way to configure and access an application wide API client entity through your Django settings.


Installation
------------

To install ``edgecast`` and ``django_edgecast``, do yourself a favor and don't use anything other than `pip <http://www.pip-installer.org/>`_:

.. code-block:: bash

    $ pip install edgecast


Installation in Django
----------------------

After the module has been installed, you need to add ``django_edgecast`` to your list of ``INSTALLED_APPS`` in your application configuration:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_edgecast',
    )

You also need to add your account number, which can be found in the upper right corner of your control panel, and your token, which can be found under your account settings, to your application configuration:

.. code-block:: python

    EDGECAST_ACCOUNT_NUMBER = '..'
    EDGECAST_TOKEN = '..'

The Edgecast client can now be easily accessed from the entire application:

.. code-block:: python

    from django_edgecast import client
    
    ...


Testing
-------

Testing requires a set of valid credentials. All tests are performed against URLs in the ``/_testing`` path for the CDN node your select. Credentials are loaded from the environment during testing for security:

``EDGECAST_CDN_DOMAIN``
    CDN domain to use for tests.
``EDEDGECAST_ACCOUNT_NUMBER``
    Account number (visible in the upper right corner of your control panel.)
``EDGECAST_TOKEN``
    Token (available under your account settings in your control panel.)
