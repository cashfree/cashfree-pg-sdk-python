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

import cashfree_pg
from cashfree_pg.api.orders_api import OrdersApi  # noqa: E501
from cashfree_pg.rest import ApiException


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self):
        self.api = cashfree_pg.api.orders_api.OrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_p_g_create_order(self):
        """Test case for p_g_create_order

        Create Order  # noqa: E501
        """
        pass

    def test_p_g_fetch_order(self):
        """Test case for p_g_fetch_order

        Get Order  # noqa: E501
        """
        pass

    def test_p_g_fetch_order_extended_data(self):
        """Test case for p_g_fetch_order_extended_data

        Get Order Extended  # noqa: E501
        """
        pass

    def test_p_g_terminate_order(self):
        """Test case for p_g_terminate_order

        Terminate Order  # noqa: E501
        """
        pass

    def test_p_g_update_order_extended_data(self):
        """Test case for p_g_update_order_extended_data

        Update Order Extended  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
