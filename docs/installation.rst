============
Installation
============

Run this simple command in your terminal::

    pip install djangomailup

Add ``'djangomailup'`` to your ``INSTALLED_APPS`` setting:

.. code-block:: python

    INSTALLED_APPS = [
        ...  # other apps
        'djangomailup',
    ]

Then add ``MAILUP`` configurations in your settings like:

.. code-block:: python

    MAILUP = {
        "default": {
            "client_id": "client_id",
            "client_secret": "client_secret",
            "username": "m1234",
            "password": "password",
        },
    }

where:

1.  ``default``: is the name of configuration
2.  ``client_id`` and ``client_secret`` are tokens for MailUp API REST
3.  ``username`` and ``password`` are credentials for MailUp account

