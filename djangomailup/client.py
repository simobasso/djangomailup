"""mailup client."""
from .conf import ENDPOINT
from .oauth2 import AuthenticateSession


class MailUpClient(AuthenticateSession):
    """
    MailUp client for django.

    A requests authenticated :py:class:`Session <requests.Session>`.

    :param using: name of MAILUP configuration (default: 'default')
    :type using: string

    Same of :py:class:`Session <requests.Session>`,
    with oAuth2 logic.

    Usage::

        >>> form djangomailup import MailUpClient()
        >>> s = MailUpClient()
        >>> s.get_info()
        <Response [200]>

    To use a different configuration use ``using`` argument::

        ...
        >>> s = MailUpClient(using='myotherconfiguration')
        ...
    """

    def get_info(self):
        """
        Return MailUp Account Info.

        Take a look at MailUp's documentation
        if you want know more about Account Info

        Reference: `Account Info <http://help.mailup.com/display/mailupapi/Accounts#Accounts-ObtainingMailUpaccountdetailsfortheconnectedaccount>`_
        """
        return self.get(ENDPOINT["info"])

    def read_lists(self):
        """
        Return the lists that are visible for authenticated user.

        Take a look at MailUp's documentation
        if you want know more about Read Lists

        Reference: `Read Lists
        <http://help.mailup.com/display/mailupapi/Manage+Lists+and+Groups#ManageListsandGroups-Lists/#ManageListsandGroups-ReadLists>`_
        """
        return self.get(ENDPOINT["lists"])
