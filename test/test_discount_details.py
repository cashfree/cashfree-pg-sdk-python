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
from cashfree_pg.models.discount_details import DiscountDetails  # noqa: E501
from cashfree_pg.rest import ApiException

class TestDiscountDetails(unittest.TestCase):
    """DiscountDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DiscountDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscountDetails`
        """
        model = cashfree_pg.models.discount_details.DiscountDetails()  # noqa: E501
        if include_optional :
            return DiscountDetails(
                discount_type = 'flat', 
                discount_value = '0', 
                max_discount_amount = '0'
            )
        else :
            return DiscountDetails(
                discount_type = 'flat',
                discount_value = '0',
                max_discount_amount = '0',
        )
        """

    def testDiscountDetails(self):
        """Test DiscountDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
