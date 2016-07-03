"""mailup basic configuration."""

DEFAULT_ALIAS = "default"
BASE_URL = "https://services.mailup.com/"
API_VERSION = "API/v1.1/Rest/"
AUTHORIZATION = "Authorization/OAuth/"
AUTHORIZE = "{}{}".format(BASE_URL, AUTHORIZATION)
REST_URL = "{}{}".format(BASE_URL, API_VERSION)

CONSOLE = "{}ConsoleService.svc/Console/".format(REST_URL)
MAIL_STATISTICS = "{}MailStatisticsService.svc".format(REST_URL)

ENDPOINT = {
    "authorize": "{}LogOn".format(AUTHORIZE),
    "token": "{}Token".format(AUTHORIZE),
    "info": "{}Authentication/Info".format(CONSOLE),
}

DEFAULTS = {
    "attempts": 20,
    "page_size": 50,
    "timeout": 60,
    "timeout_403": 60,
    "attempt_wait": 2,
}
