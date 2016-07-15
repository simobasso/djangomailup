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
from .oauth2 import AuthenticateSession  # NOQA

__version__ = '0.2.0'

__title__ = 'djangomailup'
__author__ = 'Simone Basso'
__license__ = 'MIT'
__all__ = ('MailUpClient', )
