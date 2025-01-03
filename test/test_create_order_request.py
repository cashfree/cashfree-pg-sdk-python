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
from cashfree_pg.models.create_order_request import CreateOrderRequest  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCreateOrderRequest(unittest.TestCase):
    """CreateOrderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateOrderRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOrderRequest`
        """
        model = cashfree_pg.models.create_order_request.CreateOrderRequest()  # noqa: E501
        if include_optional :
            return CreateOrderRequest(
                order_id = 'your-order-id', 
                order_amount = 10.15, 
                order_currency = 'INR', 
                cart_details = cashfree_pg.models.cart_details.CartDetails(
                    shipping_charge = 1.337, 
                    cart_name = '', 
                    cart_items = [
                        cashfree_pg.models.cart_item.CartItem(
                            item_id = '', 
                            item_name = '', 
                            item_description = '', 
                            item_tags = [
                                ''
                                ], 
                            item_details_url = '', 
                            item_image_url = '', 
                            item_original_unit_price = 1.337, 
                            item_discounted_unit_price = 1.337, 
                            item_currency = '', 
                            item_quantity = 1.337, )
                        ], ), 
                customer_details = {"customer_id":"7112AAA812234","customer_email":"john@cashfree.com","customer_phone":"9908734801","customer_name":"John Doe","customer_bank_account_number":"1518121112","customer_bank_ifsc":"XITI0000001","customer_bank_code":3333,"customer_uid":"54deabb4-ba45-4a60-9e6a-9c016fe7ab10"}, 
                terminal = {"added_on":"2023-08-04T13:12:58+05:30","cf_terminal_id":"31051123","last_updated_on":"2023-09-06T14:07:00+05:30","terminal_address":"Banglore","terminal_id":"terminal-123","terminal_name":"test","terminal_note":"POS vertical","terminal_phone_no":"6309291183","terminal_status":"ACTIVE","terminal_type":"SPOS"}, 
                order_meta = cashfree_pg.models.order_meta.OrderMeta(
                    return_url = 'https://www.cashfree.com/devstudio/thankyou', 
                    notify_url = 'https://example.com/cf_notify', 
                    payment_methods = cc,dc,upi, ), 
                order_expiry_time = '2021-07-02T10:20:12+05:30', 
                order_note = 'Test order', 
                order_tags = {"product":"Laptop","shipping_address":"123 Main St"}, 
                order_splits = [{"amount":10,"vendor":"john"}]
            )
        else :
            return CreateOrderRequest(
                order_amount = 10.15,
                order_currency = 'INR',
                customer_details = {"customer_id":"7112AAA812234","customer_email":"john@cashfree.com","customer_phone":"9908734801","customer_name":"John Doe","customer_bank_account_number":"1518121112","customer_bank_ifsc":"XITI0000001","customer_bank_code":3333,"customer_uid":"54deabb4-ba45-4a60-9e6a-9c016fe7ab10"},
        )
        """

    def testCreateOrderRequest(self):
        """Test CreateOrderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
