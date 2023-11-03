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
from cashfree_pg.models.settlement_url_object import SettlementURLObject  # noqa: E501
from cashfree_pg.rest import ApiException

class TestSettlementURLObject(unittest.TestCase):
    """SettlementURLObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SettlementURLObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettlementURLObject`
        """
        model = cashfree_pg.models.settlement_url_object.SettlementURLObject()  # noqa: E501
        if include_optional :
            return SettlementURLObject(
                url = 'https://sandbox.cashfree.com/pg/orders/order_271vovQ3PTZAx3fDI0xtZbC4jkPET/settlements'
            )
        else :
            return SettlementURLObject(
        )
        """

    def testSettlementURLObject(self):
        """Test SettlementURLObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
