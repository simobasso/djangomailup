"""mailup client."""
from requests.auth import HTTPBasicAuth
from rauth import OAuth2Service
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from .conf import DEFAULT_ALIAS, ENDPOINT, DEFAULTS, BASE_URL
from .decoders import mailup_token_request


class MailUpClient(object):
    """MailUp client for django."""

    def __init__(self, using=None):
        """set token."""
        self._using = using
        conf = self._check_configuration()

        client_id = conf.get("client_id", "")
        client_secret = conf.get("client_secret", "")

        service = OAuth2Service(
            client_id=client_id,
            client_secret=client_secret,
            name='mailup',
            authorize_url=ENDPOINT["authorize"],
            access_token_url=ENDPOINT["token"],
            base_url=BASE_URL,
        )

        data = {
            "grant_type": "password",
            "username": conf.get("username", ""),
            "password": conf.get("password", ""),
        }
        r = service.get_raw_access_token(
            'POST',
            data=data,
            auth=HTTPBasicAuth(client_id, client_secret),
        )
        access_token = mailup_token_request(r, 'access_token')

        self.session = service.get_session(access_token)

        if service.access_token_response:
            self.session.access_token_response = service.access_token_response

    def _check_configuration(self):
        """Check if configuration exist."""
        configurations = getattr(settings, "MAILUP", None)
        if not configurations:
            raise ImproperlyConfigured(
                "You must define a MAILUP configuration"
            )

        configuration = self._using or DEFAULT_ALIAS

        if configuration not in configurations:
            raise ImproperlyConfigured(
                "{} configuration doesn't exist".format(configuration)
            )

        conf = configurations[configuration]

        for setting, default in DEFAULTS.items():
            conf.setdefault(setting, default)

        return conf

    def get_info(self):
        """Return Account Info."""
        return self.session.get(ENDPOINT["info"])
