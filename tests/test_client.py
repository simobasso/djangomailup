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


class TestAuthenticateSession(TestCase):

    @override_settings(MAILUP=None)
    def test_missing_configuration(self):
        self.assertRaises(ImproperlyConfigured, MailUpClient)

    @override_settings(MAILUP={"missing": {}})
    def test_missing_default(self):
        self.assertRaises(ImproperlyConfigured, MailUpClient)

    @override_settings(MAILUP={"default": {
        "client_secret": "12345",
        "username": "username",
        "password": "password"
    }})
    def test_missing_client_id(self):
        self.assertRaisesRegexp(
            ImproperlyConfigured,
            "Missing 'client_id' in 'default' configuration",
            MailUpClient
        )

    def test_invalid_credentials(self):
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
                "Client credentials are invalid",
                MailUpClient
            )

    def test_a_nonjson_response(self):
        url = "https://services.mailup.com/Authorization/OAuth/Token"
        with requests_mock.mock() as m:
            m.post(url, text=(
                '"error":"invalid_client",'
                '"error_description":"Client credentials are invalid"'
            ))

            self.assertRaisesRegexp(
                Exception,
                "'response' is not JSON serializable: ",
                MailUpClient
            )


class TestDjangoMailupApi(TestCase):
    def setUp(self):
        url = "https://services.mailup.com/Authorization/OAuth/Token"
        with requests_mock.mock() as m:
            m.post(url, text=(
                '{'
                '"access_token": "token",'
                '"refresh_token": "refresh_token"'
                '}'
            ))
            self.client = MailUpClient()

    def test_get_info(self):
        url = (
            "https://services.mailup.com/API/v1.1/Rest/"
            "ConsoleService.svc/Console/"
            "Authentication/Info"
        )
        with requests_mock.mock() as m:
            m.get(url, json={
                "Company": "test",
                "IsTrial": False,
                "UID": "12345",
                "Username": "mtest",
                "Version": "8.9.4"
            })
            request = self.client.get_info()
        self.assertEquals(request.status_code, 200)

    def test_read_list(self):
        url = (
            "https://services.mailup.com/API/v1.1/Rest/"
            "ConsoleService.svc/Console/"
            "Lists"
        )
        with requests_mock.mock() as m:
            m.get(url, json={
                "IsPaginated": False,
                "Items": [{
                    "Company": "",
                    "Description": "",
                    "Name": "Second List ",
                    "idList": 2,
                    "listGuid": "f34e5054-5555-4444-ffff-51acc36ae104"
                }, {
                    "Company": "",
                    "Description": "This is a description",
                    "Name": "Newsletter ",
                    "idList": 1,
                    "listGuid": "49494949-4444-9999-8888-185543409eb7"
                }],
                "PageNumber": 0,
                "PageSize": 5,
                "Skipped": 0,
                "TotalElementsCount": 2
            })
            request = self.client.read_lists()
        self.assertEquals(request.status_code, 200)

    def test_create_lists(self):
        url = (
            "https://services.mailup.com/API/v1.1/Rest/"
            "ConsoleService.svc/Console/"
            "Lists"
        )
        with requests_mock.mock() as m:
            m.post(url, json={
                "IdList": 2,
            })
            request = self.client.create_lists("New Arrivals")
        self.assertEquals(request.status_code, 200)

        with requests_mock.mock() as m:
            m.post(url, json={
                "IdList": 3,
            })
            request = self.client.create_lists("New Arrivals 2", extra={
                "public": False,
            })
        self.assertEquals(request.status_code, 200)

    def test_update_lists(self):
        url = (
            "https://services.mailup.com/API/v1.1/Rest/"
            "ConsoleService.svc/Console/"
            "Lists/2"
        )
        with requests_mock.mock() as m:
            m.post(url, json={
                "bouncedemail": "g1g7g@g1g7g.bounce.smtpnext.com",
                "charset": "UTF-8",
                "conversionlab_trackcode": "",
                "default_prefix": "001",
                "description": "Use this list to inform subscribers about new products",
                "disclaimer": "Safely Subscribe System",
                "displayas": "campo1,campo2,campo3",
                "format": "html",
                "frontendform": True,
                "kbmax": 100,
                "multi_optout_list": "2",
                "multipart_text": True,
                "nl_sendername": "John Smith",
                "notifyemail": None,
                "optout_type": 0,
                "owneremail": "john@example.com",
                "public": True,
                "replyto": "mary@example.com",
                "sendconfirmsms": False,
                "sendemailoptout": False,
                "senderfax": "",
                "senderfaxname": "",
                "sms_sendername": "SMSText",
                "subscribedemail": True,
                "tracking": True,
                "Customer": True,
                "IdList": 2,
                "Name": "New Arrivals",
                "business": True,
                "scope": "newsletters"
            })
            request = self.client.update_lists(2)
        self.assertEquals(request.status_code, 200)

        url = (
            "https://services.mailup.com/API/v1.1/Rest/"
            "ConsoleService.svc/Console/"
            "Lists/3"
        )
        with requests_mock.mock() as m:
            m.post(url, json={
                "bouncedemail": "g1g7g@g1g7g.bounce.smtpnext.com",
                "charset": "UTF-8",
                "conversionlab_trackcode": "",
                "default_prefix": "001",
                "description": "Use this list to inform subscribers about new products",
                "disclaimer": "Safely Subscribe System",
                "displayas": "campo1,campo2,campo3",
                "format": "html",
                "frontendform": True,
                "kbmax": 100,
                "multi_optout_list": "2",
                "multipart_text": True,
                "nl_sendername": "John Smith",
                "notifyemail": None,
                "optout_type": 0,
                "owneremail": "john@example.com",
                "public": False,
                "replyto": "mary@example.com",
                "sendconfirmsms": False,
                "sendemailoptout": False,
                "senderfax": "",
                "senderfaxname": "",
                "sms_sendername": "SMSText",
                "subscribedemail": True,
                "tracking": True,
                "Customer": True,
                "IdList": 3,
                "Name": "New Arrivals",
                "business": True,
                "scope": "newsletters"
            })
            request = self.client.update_lists(3, extra={
                "public": False,
            })
        self.assertEquals(request.status_code, 200)
