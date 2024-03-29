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
from cashfree_pg.models.es_order_recon_response_data_inner import ESOrderReconResponseDataInner  # noqa: E501
from cashfree_pg.rest import ApiException

class TestESOrderReconResponseDataInner(unittest.TestCase):
    """ESOrderReconResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ESOrderReconResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ESOrderReconResponseDataInner`
        """
        model = cashfree_pg.models.es_order_recon_response_data_inner.ESOrderReconResponseDataInner()  # noqa: E501
        if include_optional :
            return ESOrderReconResponseDataInner(
                amount = 1.337, 
                settlement_eligibility_time = '', 
                merchant_order_id = '', 
                tx_time = '', 
                settled = '', 
                entity_id = '', 
                merchant_settlement_utr = '', 
                currency = '', 
                sale_type = '', 
                customer_name = '', 
                customer_email = '', 
                customer_phone = '', 
                merchant_vendor_commission = '', 
                split_service_charge = '', 
                split_service_tax = '', 
                pg_service_tax = '', 
                pg_service_charge = '', 
                pg_charge_postpaid = '', 
                merchant_settlement_id = '', 
                added_on = '', 
                tags = '', 
                entity_type = '', 
                settlement_initiated_on = '', 
                settlement_time = '', 
                order_splits = [
                    cashfree_pg.models.es_order_recon_response_data_inner_order_splits_inner.ESOrderReconResponse_data_inner_order_splits_inner(
                        split = [
                            cashfree_pg.models.es_order_recon_response_data_inner_order_splits_inner_split_inner.ESOrderReconResponse_data_inner_order_splits_inner_split_inner(
                                merchant_vendor_id = '', 
                                percentage = 1.337, 
                                tags = cashfree_pg.models.tags.tags(), )
                            ], 
                        created_at = '', )
                    ], 
                eligible_split_balance = ''
            )
        else :
            return ESOrderReconResponseDataInner(
        )
        """

    def testESOrderReconResponseDataInner(self):
        """Test ESOrderReconResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
