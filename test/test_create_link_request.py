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
from cashfree_pg.models.create_link_request import CreateLinkRequest  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCreateLinkRequest(unittest.TestCase):
    """CreateLinkRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateLinkRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateLinkRequest`
        """
        model = cashfree_pg.models.create_link_request.CreateLinkRequest()  # noqa: E501
        if include_optional :
            return CreateLinkRequest(
                link_id = '', 
                link_amount = 1.337, 
                link_currency = '', 
                link_purpose = '', 
                customer_details = {"customer_name":"John Doe","customer_phone":"9999999999","customer_email":"john@cashfree.com"}, 
                link_partial_payments = True, 
                link_minimum_partial_amount = 1.337, 
                link_expiry_time = '', 
                link_notify = {"send_sms":false,"send_email":true}, 
                link_auto_reminders = True, 
                link_notes = {"key_1":"value_1","key_2":"value_2"}, 
                link_meta = {"notify_url":"https://ee08e626ecd88c61c85f5c69c0418cb5.m.pipedream.net","upi_intent":false,"return_url":"https://b8af79f41056.eu.ngrok.io"}
            )
        else :
            return CreateLinkRequest(
                link_id = '',
                link_amount = 1.337,
                link_currency = '',
                link_purpose = '',
                customer_details = {"customer_name":"John Doe","customer_phone":"9999999999","customer_email":"john@cashfree.com"},
        )
        """

    def testCreateLinkRequest(self):
        """Test CreateLinkRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
