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
from cashfree_pg.models.payment_webhook_gateway_details_entity import PaymentWebhookGatewayDetailsEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestPaymentWebhookGatewayDetailsEntity(unittest.TestCase):
    """PaymentWebhookGatewayDetailsEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentWebhookGatewayDetailsEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentWebhookGatewayDetailsEntity`
        """
        model = cashfree_pg.models.payment_webhook_gateway_details_entity.PaymentWebhookGatewayDetailsEntity()  # noqa: E501
        if include_optional :
            return PaymentWebhookGatewayDetailsEntity(
                gateway_name = '', 
                gateway_order_id = '', 
                gateway_payment_id = '', 
                gateway_status_code = '', 
                gateway_settlement = ''
            )
        else :
            return PaymentWebhookGatewayDetailsEntity(
        )
        """

    def testPaymentWebhookGatewayDetailsEntity(self):
        """Test PaymentWebhookGatewayDetailsEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
