"""Manage OAuth2 authentication."""
from requests import Session
from requests.auth import HTTPBasicAuth, AuthBase
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .conf import ENDPOINT
from .utils import response_parser


class oAuth2Auth(AuthBase):
    """requests OAuth2 authentication."""

    def __init__(self, access_token):
        """
        Use access_token to authenticate the requests.

        :param access_token: MailUp access token
        :type access_token: string
        """
        self.access_token = access_token

    def __call__(self, r):
        """Add token to the request."""
        r.headers['Authorization'] = 'Bearer ' + self.access_token
        return r


class AuthenticateSession(Session):
    """
    A requests authenticated :py:class:`Session <requests.Session>`.

    :param using: name of MAILUP configuration (default: 'default')
    :type using: string

    Same of :py:class:`Session <requests.Session>`,
    with oAuth2 logic.

    Usage::

        >>> form djangomailup import AuthenticateSession
        >>> s = AuthenticateSession()
        >>> url = 'https://services.mailup.com/'
        >>> s.get(url)
        <Response [200]>

    To use a different configuration use ``using`` argument::

        ...
        >>> s = AuthenticateSession(using='myotherconfiguration')
        ...
    """

    def __init__(self, using='default'):
        """Check configuration and set Session authentication."""
        super(AuthenticateSession, self).__init__()
        self._using = using
        self._check_configuration()

        access_token = self._get_access_token()

        self.auth = oAuth2Auth(access_token)

    def _get_access_token(self):
        """Get token and refresh_token from mailup."""
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }

        response = self.post(
            ENDPOINT["token"],
            data=data,
            auth=HTTPBasicAuth(self.client_id, self.client_secret),
        )

        data = response_parser(response)

        self.refresh_token = data["refresh_token"]
        return data["access_token"]

    def _check_configuration(self):
        """Check if configuration exist and is valid."""
        configurations = getattr(settings, "MAILUP", None)
        if not configurations:
            raise ImproperlyConfigured(
                "You must define a MAILUP configuration"
            )

        if self._using not in configurations:
            raise ImproperlyConfigured(
                "'{}' configuration doesn't exist".format(self._using)
            )

        conf = configurations[self._using]

        for key in ["username", "password", "client_id", "client_secret"]:
            try:
                setattr(self, key, conf[key])
            except KeyError:
                raise ImproperlyConfigured(
                    "Missing '{}' in '{}' configuration".format(
                        key,
                        self._using
                    )
                )
