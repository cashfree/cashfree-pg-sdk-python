# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2023-08-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import cashfree_pg
from cashfree_pg.api.soft_pos_api import SoftPOSApi  # noqa: E501
from cashfree_pg.rest import ApiException


class TestSoftPOSApi(unittest.TestCase):
    """SoftPOSApi unit test stubs"""

    def setUp(self):
        self.api = cashfree_pg.api.soft_pos_api.SoftPOSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_spos_create_terminal(self):
        """Test case for spos_create_terminal

        Create Terminal  # noqa: E501
        """
        pass

    def test_spos_create_terminal_transaction(self):
        """Test case for spos_create_terminal_transaction

        Create Terminal Transaction  # noqa: E501
        """
        pass

    def test_spos_demap_soundbox_vpa(self):
        """Test case for spos_demap_soundbox_vpa

        Demap Soundbox Vpa  # noqa: E501
        """
        pass

    def test_spos_fetch_terminal(self):
        """Test case for spos_fetch_terminal

        Get Terminal Status using Phone Number  # noqa: E501
        """
        pass

    def test_spos_fetch_terminal_qr_codes(self):
        """Test case for spos_fetch_terminal_qr_codes

        Fetch Terminal QR Codes  # noqa: E501
        """
        pass

    def test_spos_fetch_terminal_soundbox_vpa(self):
        """Test case for spos_fetch_terminal_soundbox_vpa

        Fetch Terminal Soundbox vpa  # noqa: E501
        """
        pass

    def test_spos_fetch_terminal_transaction(self):
        """Test case for spos_fetch_terminal_transaction

        Get Terminal Transaction  # noqa: E501
        """
        pass

    def test_spos_onboard_soundbox_vpa(self):
        """Test case for spos_onboard_soundbox_vpa

        Onboard Soundbox Vpa  # noqa: E501
        """
        pass

    def test_spos_update_soundbox_vpa(self):
        """Test case for spos_update_soundbox_vpa

        Update Soundbox Vpa  # noqa: E501
        """
        pass

    def test_spos_update_terminal(self):
        """Test case for spos_update_terminal

        Update Terminal  # noqa: E501
        """
        pass

    def test_spos_update_terminal_status(self):
        """Test case for spos_update_terminal_status

        Update Terminal Status  # noqa: E501
        """
        pass

    def test_spos_upload_terminal_docs(self):
        """Test case for spos_upload_terminal_docs

        Upload Terminal Docs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
