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
from cashfree_pg.models.split_order_recon_success_response_settlement import SplitOrderReconSuccessResponseSettlement  # noqa: E501
from cashfree_pg.rest import ApiException

class TestSplitOrderReconSuccessResponseSettlement(unittest.TestCase):
    """SplitOrderReconSuccessResponseSettlement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SplitOrderReconSuccessResponseSettlement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SplitOrderReconSuccessResponseSettlement`
        """
        model = cashfree_pg.models.split_order_recon_success_response_settlement.SplitOrderReconSuccessResponseSettlement()  # noqa: E501
        if include_optional :
            return SplitOrderReconSuccessResponseSettlement(
                entity = '', 
                cf_settlement_id = 56, 
                cf_payment_id = 56, 
                order_id = '', 
                order_currency = '', 
                transfer_id = '', 
                order_amount = 1.337, 
                service_charge = 1.337, 
                service_tax = 1.337, 
                settlement_amount = 1.337, 
                settlement_currency = '', 
                transfer_utr = '', 
                transfer_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                payment_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return SplitOrderReconSuccessResponseSettlement(
        )
        """

    def testSplitOrderReconSuccessResponseSettlement(self):
        """Test SplitOrderReconSuccessResponseSettlement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
