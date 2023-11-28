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
from cashfree_pg.models.pay_order_request_payment_method import PayOrderRequestPaymentMethod  # noqa: E501
from cashfree_pg.rest import ApiException

class TestPayOrderRequestPaymentMethod(unittest.TestCase):
    """PayOrderRequestPaymentMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PayOrderRequestPaymentMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayOrderRequestPaymentMethod`
        """
        model = cashfree_pg.models.pay_order_request_payment_method.PayOrderRequestPaymentMethod()  # noqa: E501
        if include_optional :
            return PayOrderRequestPaymentMethod(
                card = {"channel":"link","card_number":"4111111111111111","card_holder_name":"Tushar Gupta","card_expiry_mm":"06","card_expiry_yy":"22","card_cvv":"900"}, 
                upi = {"channel":"collect","upi_id":"john@okxdfcbak","upi_expiry_minutes":10}, 
                netbanking = {"channel":"link","netbanking_bank_code":3022}, 
                app = {"channel":"link","provider":"gpay","phone":"8474090552"}, 
                emi = {"channel":"link","card_number":"4111111111111111","card_holder_name":"Tushar Gupta","card_expiry_mm":"06","card_expiry_yy":"22","card_cvv":"900","card_bank_name":"hdfc","emi_tenure":3}, 
                cardless_emi = {"channel":"link","provider":"kotak","phone":"7768913241","emi_tenure":3}, 
                paylater = {"channel":"link","provider":"kotak","phone":"7789112345"}
            )
        else :
            return PayOrderRequestPaymentMethod(
                card = {"channel":"link","card_number":"4111111111111111","card_holder_name":"Tushar Gupta","card_expiry_mm":"06","card_expiry_yy":"22","card_cvv":"900"},
                upi = {"channel":"collect","upi_id":"john@okxdfcbak","upi_expiry_minutes":10},
                netbanking = {"channel":"link","netbanking_bank_code":3022},
                app = {"channel":"link","provider":"gpay","phone":"8474090552"},
                emi = {"channel":"link","card_number":"4111111111111111","card_holder_name":"Tushar Gupta","card_expiry_mm":"06","card_expiry_yy":"22","card_cvv":"900","card_bank_name":"hdfc","emi_tenure":3},
                cardless_emi = {"channel":"link","provider":"kotak","phone":"7768913241","emi_tenure":3},
                paylater = {"channel":"link","provider":"kotak","phone":"7789112345"},
        )
        """

    def testPayOrderRequestPaymentMethod(self):
        """Test PayOrderRequestPaymentMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
