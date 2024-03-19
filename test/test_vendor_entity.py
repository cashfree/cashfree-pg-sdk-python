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
from cashfree_pg.models.vendor_entity import VendorEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestVendorEntity(unittest.TestCase):
    """VendorEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VendorEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VendorEntity`
        """
        model = cashfree_pg.models.vendor_entity.VendorEntity()  # noqa: E501
        if include_optional :
            return VendorEntity(
                email = '', 
                status = '', 
                phone = '', 
                name = '', 
                vendor_id = '', 
                added_on = '', 
                updated_on = '', 
                bank = [
                    {"account_number":11219276360,"account_holder":"JOHNDOE","ifsc":"YESB0000262"}
                    ], 
                upi = '', 
                schedule_option = [
                    {"settlement_schedule_message":"T+1 settlement at 11:00 AM","schedule_id":1,"merchant_default":true}
                    ], 
                vendor_type = '', 
                account_type = '', 
                business_type = '', 
                related_docs = [
                    cashfree_pg.models.vendor_entity_related_docs_inner.VendorEntity_related_docs_inner(
                        vendor_id = '', 
                        doc_type = '', 
                        doc_value = '', 
                        status = '', 
                        remarks = '', )
                    ]
            )
        else :
            return VendorEntity(
        )
        """

    def testVendorEntity(self):
        """Test VendorEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
