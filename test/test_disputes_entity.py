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
from cashfree_pg.models.disputes_entity import DisputesEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestDisputesEntity(unittest.TestCase):
    """DisputesEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DisputesEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputesEntity`
        """
        model = cashfree_pg.models.disputes_entity.DisputesEntity()  # noqa: E501
        if include_optional :
            return DisputesEntity(
                dispute_id = 56, 
                dispute_type = 'DISPUTE', 
                reason_code = '', 
                reason_description = '', 
                dispute_amount = 1.337, 
                created_at = '', 
                respond_by = '', 
                updated_at = '', 
                resolved_at = '', 
                dispute_status = 'DISPUTE_CREATED', 
                cf_dispute_remarks = '', 
                preferred_evidence = {"prefferred_evidence":[{"document_type":"Delivery/Service Proof","document_description":"Proof that the cardholder/customer received the goods or services."},{"document_type":"Statement of Service","document_description":"Account Statement of wallet where funds were loaded by customer."}]}, 
                dispute_evidence = [{"document_id":18150,"document_name":"disputeSampleFile.pdf","document_type":"DeliveryProof"}], 
                order_details = {"order_id":"Load_test_0103_FGA4HF12AC","order_currency":"INR","order_amount":10.0,"cf_payment_id":1489901523,"payment_currency":"INR","payment_amount":10.0}, 
                customer_details = {"customer_name":"Manideep Ellur","customer_phone":8281554863,"customer_email":"manideep.ellur@cashfree.com"}
            )
        else :
            return DisputesEntity(
        )
        """

    def testDisputesEntity(self):
        """Test DisputesEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
