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
from cashfree_pg.models.payment_webhook import PaymentWebhook  # noqa: E501
from cashfree_pg.rest import ApiException

class TestPaymentWebhook(unittest.TestCase):
    """PaymentWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentWebhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentWebhook`
        """
        model = cashfree_pg.models.payment_webhook.PaymentWebhook()  # noqa: E501
        if include_optional :
            return PaymentWebhook(
                data = cashfree_pg.models.payment_webhook_data_entity.PaymentWebhookDataEntity(
                    order = cashfree_pg.models.payment_webhook_order_entity.PaymentWebhookOrderEntity(
                        order_id = '', 
                        order_amount = 1.337, 
                        order_currency = '', 
                        order_tags = {
                            'key' : '0'
                            }, ), 
                    payment = null, 
                    customer_details = cashfree_pg.models.payment_webhook_customer_entity.PaymentWebhookCustomerEntity(
                        customer_name = 'Yogesh', 
                        customer_id = '12121212', 
                        customer_email = 'yogesh.miglani@gmail.com', 
                        customer_phone = '9666699999', ), 
                    error_details = cashfree_pg.models.payment_webhook_error_entity.PaymentWebhookErrorEntity(
                        error_code = '', 
                        error_description = '', 
                        error_reason = '', 
                        error_source = '', 
                        error_code_raw = '', 
                        error_description_raw = '', ), 
                    payment_gateway_details = cashfree_pg.models.payment_webhook_gateway_details_entity.PaymentWebhookGatewayDetailsEntity(
                        gateway_name = '', 
                        gateway_order_id = '', 
                        gateway_payment_id = '', 
                        gateway_status_code = '', 
                        gateway_settlement = '', ), 
                    payment_offers = [
                        cashfree_pg.models.offer_entity.OfferEntity(
                            offer_id = 'd2b430fb-1afe-455a-af31-66d00377b29a', 
                            offer_status = 'active', 
                            offer_meta = {"$ref":"#/components/schemas/OfferMeta/example"}, 
                            offer_tnc = {"$ref":"#/components/schemas/OfferTnc/example"}, 
                            offer_details = {"$ref":"#/components/schemas/OfferDetails/example"}, 
                            offer_validations = {"$ref":"#/components/schemas/OfferValidations/example"}, )
                        ], ), 
                event_time = '2021-10-07T19:42:44+05:30', 
                type = 'PAYMENT_SUCCESS_WEBHOOK'
            )
        else :
            return PaymentWebhook(
        )
        """

    def testPaymentWebhook(self):
        """Test PaymentWebhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
