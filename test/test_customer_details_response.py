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
from cashfree_pg.models.customer_details_response import CustomerDetailsResponse  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCustomerDetailsResponse(unittest.TestCase):
    """CustomerDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CustomerDetailsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerDetailsResponse`
        """
        model = cashfree_pg.models.customer_details_response.CustomerDetailsResponse()  # noqa: E501
        if include_optional :
            return CustomerDetailsResponse(
                customer_id = '012', 
                customer_email = '012', 
                customer_phone = '0123456789', 
                customer_name = '012', 
                customer_bank_account_number = '012', 
                customer_bank_ifsc = '', 
                customer_bank_code = 1.337, 
                customer_uid = ''
            )
        else :
            return CustomerDetailsResponse(
        )
        """

    def testCustomerDetailsResponse(self):
        """Test CustomerDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()