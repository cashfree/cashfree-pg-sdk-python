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
from cashfree_pg.models.offer_validations_payment_method import OfferValidationsPaymentMethod  # noqa: E501
from cashfree_pg.rest import ApiException

class TestOfferValidationsPaymentMethod(unittest.TestCase):
    """OfferValidationsPaymentMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferValidationsPaymentMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferValidationsPaymentMethod`
        """
        model = cashfree_pg.models.offer_validations_payment_method.OfferValidationsPaymentMethod()  # noqa: E501
        if include_optional :
            return OfferValidationsPaymentMethod(
                all = cashfree_pg.models.all_offers.All Offers(), 
                card = cashfree_pg.models.card_offer.Card Offer(
                    type = [
                        'dc'
                        ], 
                    bank_name = 'hdfc bank', 
                    scheme_name = [
                        'visa'
                        ], ), 
                netbanking = cashfree_pg.models.offer_nb_netbanking.OfferNB_netbanking(
                    bank_name = 'all', ), 
                app = cashfree_pg.models.wallet_offer.Wallet Offer(
                    provider = 'paytm', ), 
                upi = cashfree_pg.models.upi_offer.UPI Offer(), 
                paylater = cashfree_pg.models.paylater_offer.Paylater Offer(
                    provider = 'simpl', ), 
                emi = cashfree_pg.models.emi_offer.EMI Offer(
                    type = 'cardless_emi', 
                    issuer = 'hdfc bank', 
                    tenures = [
                        3
                        ], )
            )
        else :
            return OfferValidationsPaymentMethod(
                all = cashfree_pg.models.all_offers.All Offers(),
                card = cashfree_pg.models.card_offer.Card Offer(
                    type = [
                        'dc'
                        ], 
                    bank_name = 'hdfc bank', 
                    scheme_name = [
                        'visa'
                        ], ),
                netbanking = cashfree_pg.models.offer_nb_netbanking.OfferNB_netbanking(
                    bank_name = 'all', ),
                upi = cashfree_pg.models.upi_offer.UPI Offer(),
                paylater = cashfree_pg.models.paylater_offer.Paylater Offer(
                    provider = 'simpl', ),
                emi = cashfree_pg.models.emi_offer.EMI Offer(
                    type = 'cardless_emi', 
                    issuer = 'hdfc bank', 
                    tenures = [
                        3
                        ], ),
        )
        """

    def testOfferValidationsPaymentMethod(self):
        """Test OfferValidationsPaymentMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
