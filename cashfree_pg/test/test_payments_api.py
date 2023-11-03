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

import cashfree_pg
from cashfree_pg.api.payments_api import PaymentsApi  # noqa: E501
from cashfree_pg.rest import ApiException


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    def setUp(self):
        self.api = cashfree_pg.api.payments_api.PaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_p_g_authorize_order(self):
        """Test case for p_g_authorize_order

        Preauthorization  # noqa: E501
        """
        pass

    def test_p_g_order_authenticate_payment(self):
        """Test case for p_g_order_authenticate_payment

        Submit or Resend OTP  # noqa: E501
        """
        pass

    def test_p_g_order_fetch_payment(self):
        """Test case for p_g_order_fetch_payment

        Get Payment by ID  # noqa: E501
        """
        pass

    def test_p_g_order_fetch_payments(self):
        """Test case for p_g_order_fetch_payments

        Get Payments for an Order  # noqa: E501
        """
        pass

    def test_p_g_pay_order(self):
        """Test case for p_g_pay_order

        Order Pay  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()