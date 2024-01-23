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
from cashfree_pg.models.card_payment_method import CardPaymentMethod  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCardPaymentMethod(unittest.TestCase):
    """CardPaymentMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CardPaymentMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CardPaymentMethod`
        """
        model = cashfree_pg.models.card_payment_method.CardPaymentMethod()  # noqa: E501
        if include_optional :
            return CardPaymentMethod(
                card = {"channel":"link","card_number":"4111111111111111","card_holder_name":"Tushar Gupta","card_expiry_mm":"06","card_expiry_yy":"22","card_cvv":"900"}
            )
        else :
            return CardPaymentMethod(
                card = {"channel":"link","card_number":"4111111111111111","card_holder_name":"Tushar Gupta","card_expiry_mm":"06","card_expiry_yy":"22","card_cvv":"900"},
        )
        """

    def testCardPaymentMethod(self):
        """Test CardPaymentMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
