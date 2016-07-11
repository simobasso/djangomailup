"""
Django app to integrate with MailUp.

Basic usage:
>>> from djangomailup import MailUpClient
>>> client = MailUpClient()
...
>>> info = client.get_info()
>>> info.json()
"""

from .client import MailUpClient  # NOQA

__version__ = '0.1.1'

__title__ = 'djangomailup'
__author__ = 'Simone Basso'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 litl'
__all__ = ['MailUpClient']
