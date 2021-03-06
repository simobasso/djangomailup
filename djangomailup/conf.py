"""mailup basic configuration."""

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
    "lists": "{}Lists".format(CONSOLE),
}
