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
from cashfree_pg.models.refund_entity import RefundEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestRefundEntity(unittest.TestCase):
    """RefundEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RefundEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefundEntity`
        """
        model = cashfree_pg.models.refund_entity.RefundEntity()  # noqa: E501
        if include_optional :
            return RefundEntity(
                cf_payment_id = '', 
                cf_refund_id = '', 
                order_id = '', 
                refund_id = '', 
                entity = 'refund', 
                refund_amount = 1.337, 
                refund_currency = '', 
                refund_note = '', 
                refund_status = 'SUCCESS', 
                refund_arn = '', 
                refund_charge = 1.337, 
                status_description = '', 
                metadata = None, 
                refund_splits = [
                    {"vendor_id":"Vendor01","amount":100.12,"description":"order amount should be more than equal to 100.12"}
                    ], 
                refund_type = 'PAYMENT_AUTO_REFUND', 
                refund_mode = '', 
                created_at = '', 
                processed_at = '', 
                refund_speed = {"requested":"STANDARD","accepted":"STANDARD","processed":"STANDARD","message":"Error message, if any"}
            )
        else :
            return RefundEntity(
        )
        """

    def testRefundEntity(self):
        """Test RefundEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
