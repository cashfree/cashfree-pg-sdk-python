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
import datetime

import cashfree_pg
from cashfree_pg.models.create_terminal_request import CreateTerminalRequest  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCreateTerminalRequest(unittest.TestCase):
    """CreateTerminalRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTerminalRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTerminalRequest`
        """
        model = cashfree_pg.models.create_terminal_request.CreateTerminalRequest()  # noqa: E501
        if include_optional :
            return CreateTerminalRequest(
                terminal_id = '012', 
                terminal_phone_no = '0123456789', 
                terminal_name = '012', 
                terminal_address = '0', 
                terminal_email = '0', 
                terminal_note = '0', 
                terminal_type = '0', 
                terminal_meta = cashfree_pg.models.create_terminal_request_terminal_meta.CreateTerminalRequest_terminal_meta(
                    terminal_operator = '', )
            )
        else :
            return CreateTerminalRequest(
                terminal_id = '012',
                terminal_phone_no = '0123456789',
                terminal_name = '012',
                terminal_email = '0',
                terminal_type = '0',
        )
        """

    def testCreateTerminalRequest(self):
        """Test CreateTerminalRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
