# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import cashfree_pg
from cashfree_pg.models.create_terminal_transaction_request import CreateTerminalTransactionRequest  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCreateTerminalTransactionRequest(unittest.TestCase):
    """CreateTerminalTransactionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTerminalTransactionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTerminalTransactionRequest`
        """
        model = cashfree_pg.models.create_terminal_transaction_request.CreateTerminalTransactionRequest()  # noqa: E501
        if include_optional :
            return CreateTerminalTransactionRequest(
                cf_order_id = 56, 
                cf_terminal_id = 56, 
                payment_method = '012', 
                terminal_phone_no = '0123456789'
            )
        else :
            return CreateTerminalTransactionRequest(
                cf_order_id = 56,
                payment_method = '012',
        )
        """

    def testCreateTerminalTransactionRequest(self):
        """Test CreateTerminalTransactionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()