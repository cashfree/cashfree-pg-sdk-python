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
from cashfree_pg.api.disputes_api import DisputesApi  # noqa: E501
from cashfree_pg.rest import ApiException


class TestDisputesApi(unittest.TestCase):
    """DisputesApi unit test stubs"""

    def setUp(self):
        self.api = cashfree_pg.api.disputes_api.DisputesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_p_g_accept_dispute_by_id(self):
        """Test case for p_g_accept_dispute_by_id

        Accept Dispute by Dispute ID  # noqa: E501
        """
        pass

    def test_p_g_fetch_dispute_by_id(self):
        """Test case for p_g_fetch_dispute_by_id

        Get Disputes by Dispute ID  # noqa: E501
        """
        pass

    def test_p_g_fetch_order_disputes(self):
        """Test case for p_g_fetch_order_disputes

        Get Disputes by Order Id  # noqa: E501
        """
        pass

    def test_p_g_fetch_payment_disputes(self):
        """Test case for p_g_fetch_payment_disputes

        Get Disputes by Payment ID  # noqa: E501
        """
        pass

    def test_p_g_upload_disputes_documents(self):
        """Test case for p_g_upload_disputes_documents

        Submit Evidence to contest the Dispute by Dispute ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
