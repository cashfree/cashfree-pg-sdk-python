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
from cashfree_pg.models.instrument_entity import InstrumentEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestInstrumentEntity(unittest.TestCase):
    """InstrumentEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InstrumentEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstrumentEntity`
        """
        model = cashfree_pg.models.instrument_entity.InstrumentEntity()  # noqa: E501
        if include_optional :
            return InstrumentEntity(
                customer_id = '', 
                afa_reference = '', 
                instrument_id = '', 
                instrument_type = 'card', 
                instrument_uid = '', 
                instrument_display = '', 
                instrument_status = 'ACTIVE', 
                created_at = '', 
                instrument_meta = cashfree_pg.models.instrument_meta.InstrumentMeta(
                    card_network = 'VISA', 
                    card_bank_name = 'HDFC Bank', 
                    card_country = 'IN', 
                    card_type = 'DEBIT_CARD', 
                    card_token_details = {"par":"somepar","expiry_month":"12","expiry_year":"23"}, )
            )
        else :
            return InstrumentEntity(
        )
        """

    def testInstrumentEntity(self):
        """Test InstrumentEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
