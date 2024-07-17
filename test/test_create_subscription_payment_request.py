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
from cashfree_pg.models.create_subscription_payment_request import CreateSubscriptionPaymentRequest  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCreateSubscriptionPaymentRequest(unittest.TestCase):
    """CreateSubscriptionPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSubscriptionPaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSubscriptionPaymentRequest`
        """
        model = cashfree_pg.models.create_subscription_payment_request.CreateSubscriptionPaymentRequest()  # noqa: E501
        if include_optional :
            return CreateSubscriptionPaymentRequest(
                subscription_id = '', 
                subscription_session_id = '', 
                payment_id = '', 
                payment_amount = 1.337, 
                payment_schedule_date = '', 
                payment_remarks = '', 
                payment_type = '', 
                payment_method = cashfree_pg.models.create_subscription_payment_request_payment_method.CreateSubscriptionPaymentRequest_payment_method()
            )
        else :
            return CreateSubscriptionPaymentRequest(
                subscription_id = '',
                payment_id = '',
                payment_type = '',
        )
        """

    def testCreateSubscriptionPaymentRequest(self):
        """Test CreateSubscriptionPaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
