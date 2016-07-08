=============================
djangomailup
=============================

.. image:: https://badge.fury.io/py/djangomailup.png
    :target: https://badge.fury.io/py/djangomailup

.. image:: https://pyup.io/repos/github/simobasso/djangomailup/shield.svg
    :target: https://pyup.io/repos/github/simobasso/djangomailup/
    :alt: Updates

.. image:: https://travis-ci.org/simobasso/djangomailup.png?branch=master
    :target: https://travis-ci.org/simobasso/djangomailup

.. image:: https://codecov.io/gh/simobasso/djangomailup/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/simobasso/djangomailup

Django app to integrate with MailUp

Documentation
-------------

The full documentation is at https://djangomailup.readthedocs.org.

Requirements
------------

*  OAuth2 `tokens for the MailUp REST API`_
*  MailUp account
*  Django >= 1.8
*  python 2.7+, 3.4+

.. _tokens for the MailUp REST API: http://help.mailup.com/display/mailupapi/Authenticating+with+OAuth+v2

Quickstart
----------

Install djangomailup::

    pip install djangomailup


Add configuration in settings.py:

.. code-block:: python

    INSTALLED_APPS = [
        'djangomailup',
    ]
    
    MAILUP = {
        "default": {
            "client_id": "client_id",
            "client_secret": "client_secret",
            "username": "m1234",
            "password": "password",
        },
    }

Then use it in a project:

.. code-block:: python

    from djangomailup import MailUpClient
    
    client = MailUpClient()

Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

.. code-block:: bash

    $ pip install -r requirements_test.txt
    $ python runtests.py

Credits
---------

Tools used this package:

*  Cookiecutter_
*  cookiecutter-djangopackage_
*  rauth_


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage
.. _rauth: https://github.com/litl/rauth