#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
test_djangomailup
------------

Tests for `djangomailup` client module.
"""

import requests_mock
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings

from djangomailup import MailUpClient


class TestDjangoMailupClient(TestCase):

    @override_settings(MAILUP=None)
    def test_missing_configuration(self):
        self.assertRaises(ImproperlyConfigured, MailUpClient)

    @override_settings(MAILUP={"missing": {}})
    def test_missing_default(self):
        self.assertRaises(ImproperlyConfigured, MailUpClient)

    @override_settings(MAILUP={"default": {
        "client_id": "12345"
    }})
    def test_missing_client_id(self):
        url = "https://services.mailup.com/Authorization/OAuth/Token"
        with requests_mock.mock() as m:
            m.post(url, text=(
                '{'
                '"error":"invalid_client",'
                '"error_description":"Client credentials are invalid"'
                '}'
            ))
            self.assertRaisesRegexp(
                Exception,
                "Client credentials are invalid$",
                MailUpClient
            )

    def test_wrong_token_key(self):
        url = "https://services.mailup.com/Authorization/OAuth/Token"
        with requests_mock.mock() as m:
            m.post(url, text=(
                '{"token":"token"}'
            ))
            self.assertRaisesRegexp(
                KeyError,
                "Key access_token not in",
                MailUpClient
            )


class TestDjangoMailupApi(TestCase):
    def setUp(self):
        url = "https://services.mailup.com/Authorization/OAuth/Token"
        with requests_mock.mock() as m:
            m.post(url, text=(
                '{"access_token":"token"}'
            ))
            self.client = MailUpClient()

    def test_get_info(self):
        url = (
            "https://services.mailup.com/API/v1.1/Rest/"
            "ConsoleService.svc/Console/"
            "Authentication/Info"
        )
        with requests_mock.mock() as m:
            m.get(url, text=(
                "{"
                "u'Company': u'test',"
                "u'IsTrial': False,"
                "u'UID': u'12345',"
                "u'Username': u'mtest',"
                "u'Version': u'8.9.4'"
                "}"
            ))
            request = self.client.get_info()
        self.assertEquals(request.status_code, 200)
