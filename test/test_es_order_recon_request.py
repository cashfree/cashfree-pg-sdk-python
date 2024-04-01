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
from cashfree_pg.models.es_order_recon_request import ESOrderReconRequest  # noqa: E501
from cashfree_pg.rest import ApiException

class TestESOrderReconRequest(unittest.TestCase):
    """ESOrderReconRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ESOrderReconRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ESOrderReconRequest`
        """
        model = cashfree_pg.models.es_order_recon_request.ESOrderReconRequest()  # noqa: E501
        if include_optional :
            return ESOrderReconRequest(
                filters = cashfree_pg.models.es_order_recon_request_filters.ESOrderReconRequest_filters(
                    start_date = '', 
                    end_date = '', 
                    order_ids = [
                        ''
                        ], ), 
                pagination = cashfree_pg.models.es_order_recon_request_pagination.ESOrderReconRequest_pagination(
                    cursor = '', 
                    limit = 56, )
            )
        else :
            return ESOrderReconRequest(
                filters = cashfree_pg.models.es_order_recon_request_filters.ESOrderReconRequest_filters(
                    start_date = '', 
                    end_date = '', 
                    order_ids = [
                        ''
                        ], ),
                pagination = cashfree_pg.models.es_order_recon_request_pagination.ESOrderReconRequest_pagination(
                    cursor = '', 
                    limit = 56, ),
        )
        """

    def testESOrderReconRequest(self):
        """Test ESOrderReconRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()