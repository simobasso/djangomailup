=============================
Djangomailup
=============================

.. image:: https://badge.fury.io/py/djangomailup.png
    :target: https://badge.fury.io/py/djangomailup

.. image:: https://pyup.io/repos/github/simobasso/djangomailup/shield.svg
    :target: https://pyup.io/repos/github/simobasso/djangomailup/
    :alt: Updates

.. image:: https://travis-ci.org/simobasso/djangomailup.png?branch=master
    :target: https://travis-ci.org/simobasso/djangomailup

.. image:: https://coveralls.io/repos/github/simobasso/djangomailup/badge.svg
    :target: https://coveralls.io/github/simobasso/djangomailup

.. image:: https://api.codacy.com/project/badge/Grade/df1f0dd3b14a4bc7ae43595a7880629d
    :target: https://www.codacy.com/app/simobasso/djangomailup?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=simobasso/djangomailup&amp;utm_campaign=Badge_Grade

Django app to integrate with MailUp

Documentation
-------------

The full documentation is at https://djangomailup.readthedocs.org.

Requirements
------------

*  OAuth2 `tokens for the MailUp REST API`_
*  MailUp account
*  Django >= 1.8
*  python 2.7+, 3.5+

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
* requests_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage
.. _requests: https://github.com/kennethreitz/requests
