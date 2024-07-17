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
from cashfree_pg.models.update_vendor_request import UpdateVendorRequest  # noqa: E501
from cashfree_pg.rest import ApiException

class TestUpdateVendorRequest(unittest.TestCase):
    """UpdateVendorRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateVendorRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateVendorRequest`
        """
        model = cashfree_pg.models.update_vendor_request.UpdateVendorRequest()  # noqa: E501
        if include_optional :
            return UpdateVendorRequest(
                status = '', 
                name = '', 
                email = '', 
                phone = '', 
                verify_account = True, 
                dashboard_access = True, 
                schedule_option = 1.337, 
                bank = [
                    {"account_number":11219276360,"account_holder":"JOHNDOE","ifsc":"YESB0000262"}
                    ], 
                upi = [
                    {"vpa":"success@upi","account_holder":"JOHN DOE"}
                    ], 
                kyc_details = [
                    {"account_type":"BUSINESS","business_type":"NBFC","uidai":753624181019,"gst":"11AAAAA1111A1Z0","cin":"L00000Aa0000AaA000000","pan":"BIAPA2934N","passport_number":"L6892603"}
                    ]
            )
        else :
            return UpdateVendorRequest(
                status = '',
                name = '',
                email = '',
                phone = '',
                schedule_option = 1.337,
                kyc_details = [
                    {"account_type":"BUSINESS","business_type":"NBFC","uidai":753624181019,"gst":"11AAAAA1111A1Z0","cin":"L00000Aa0000AaA000000","pan":"BIAPA2934N","passport_number":"L6892603"}
                    ],
        )
        """

    def testUpdateVendorRequest(self):
        """Test UpdateVendorRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
