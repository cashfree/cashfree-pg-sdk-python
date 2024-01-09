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
from cashfree_pg.models.settlement_webhook_data_entity import SettlementWebhookDataEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestSettlementWebhookDataEntity(unittest.TestCase):
    """SettlementWebhookDataEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SettlementWebhookDataEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettlementWebhookDataEntity`
        """
        model = cashfree_pg.models.settlement_webhook_data_entity.SettlementWebhookDataEntity()  # noqa: E501
        if include_optional :
            return SettlementWebhookDataEntity(
                settlement = {"cf_payment_id":553338,"order_id":"order-12-127","entity":"settlement","order_amount":100,"payment_time":"2021-07-13T13:13:59+05:30","service_charge":10,"service_tax":1.8,"settlement_amount":88.2,"cf_settlement_id":6121238,"transfer_id":238,"transfer_time":"2021-07-25T12:57:52+05:30","transfer_utr":"N87912312","order_currency":"INR","settlement_currency":"INR"}
            )
        else :
            return SettlementWebhookDataEntity(
        )
        """

    def testSettlementWebhookDataEntity(self):
        """Test SettlementWebhookDataEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
