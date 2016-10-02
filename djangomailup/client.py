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

    def create_lists(self, name, default=1, scope="newsletters", extra=None):
        """
        Create a new list.

        :param str name: Name of new list
        :param int default: list as a template
        :param scope: Type of list
        :type scope: newsletters or Direct_Advertising or Transactional
        :param extra: override default params
        :type extra: dict or None

        Take a look at MailUp's documentation
        if you want know more about Create list

        Reference: `Create Lists
        <http://help.mailup.com/display/mailupapi/Manage+Lists+and+Groups#ManageListsandGroups-Lists/#ManageListsandGroups-CreateList>`_
        """
        data = {
            "Name": name,
            "useDefaultSettings": bool(default),
            "idSettings": default,
            "scope": scope,
        }

        if extra:
            data.update(**extra)

        return self.post(ENDPOINT["lists"], data=data)

    def update_lists(self, list_id, extra=None):
        """
        Update an existing list.

        :param str list_id: id of the list
        :param extra: override default params
        :type extra: dict or None
        Take a look at MailUp's documentation
        if you want know more about Update list

        Reference: `Update Lists
        <http://help.mailup.com/display/mailupapi/Manage+Lists+and+Groups#ManageListsandGroups-UpdateList>`_
        """
        data = {}

        if extra:
            data.update(**extra)

        return self.post(
            "{}/{}".format(
                ENDPOINT["lists"],
                list_id,
            ),
            data=data
        )
