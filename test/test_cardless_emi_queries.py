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
from cashfree_pg.models.cardless_emi_queries import CardlessEMIQueries  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCardlessEMIQueries(unittest.TestCase):
    """CardlessEMIQueries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CardlessEMIQueries
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CardlessEMIQueries`
        """
        model = cashfree_pg.models.cardless_emi_queries.CardlessEMIQueries()  # noqa: E501
        if include_optional :
            return CardlessEMIQueries(
                order_id = 'orderYB1X69LgzUQWiSxYDF', 
                amount = 100, 
                customer_details = {"customer_phone":"9898989898"}
            )
        else :
            return CardlessEMIQueries(
        )
        """

    def testCardlessEMIQueries(self):
        """Test CardlessEMIQueries"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()