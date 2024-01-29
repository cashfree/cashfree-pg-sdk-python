# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, conlist
from cashfree_pg.models.offer_entity import OfferEntity
from cashfree_pg.models.payment_entity import PaymentEntity
from cashfree_pg.models.payment_webhook_customer_entity import PaymentWebhookCustomerEntity
from cashfree_pg.models.payment_webhook_error_entity import PaymentWebhookErrorEntity
from cashfree_pg.models.payment_webhook_gateway_details_entity import PaymentWebhookGatewayDetailsEntity
from cashfree_pg.models.payment_webhook_order_entity import PaymentWebhookOrderEntity

class PaymentWebhookDataEntity(BaseModel):
    """
    data entity in webhook
    """
    order: Optional[PaymentWebhookOrderEntity] = None
    payment: Optional[PaymentEntity] = None
    customer_details: Optional[PaymentWebhookCustomerEntity] = None
    error_details: Optional[PaymentWebhookErrorEntity] = None
    payment_gateway_details: Optional[PaymentWebhookGatewayDetailsEntity] = None
    payment_offers: Optional[conlist(OfferEntity)] = None
    __properties = ["order", "payment", "customer_details", "error_details", "payment_gateway_details", "payment_offers"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PaymentWebhookDataEntity:
        """Create an instance of PaymentWebhookDataEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentWebhookDataEntity:
        """Create an instance of PaymentWebhookDataEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if temp_dict["order, payment, customer_details, error_details, payment_gateway_details, payment_offers"] in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_details
        if self.customer_details:
            _dict['customer_details'] = self.customer_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error_details
        if self.error_details:
            _dict['error_details'] = self.error_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_gateway_details
        if self.payment_gateway_details:
            _dict['payment_gateway_details'] = self.payment_gateway_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payment_offers (list)
        _items = []
        if self.payment_offers:
            for _item in self.payment_offers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payment_offers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentWebhookDataEntity:
        """Create an instance of PaymentWebhookDataEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentWebhookDataEntity.parse_obj(obj)

        _obj = PaymentWebhookDataEntity.parse_obj({
            "order": PaymentWebhookOrderEntity.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "payment": PaymentEntity.from_dict(obj.get("payment")) if obj.get("payment") is not None else None,
            "customer_details": PaymentWebhookCustomerEntity.from_dict(obj.get("customer_details")) if obj.get("customer_details") is not None else None,
            "error_details": PaymentWebhookErrorEntity.from_dict(obj.get("error_details")) if obj.get("error_details") is not None else None,
            "payment_gateway_details": PaymentWebhookGatewayDetailsEntity.from_dict(obj.get("payment_gateway_details")) if obj.get("payment_gateway_details") is not None else None,
            "payment_offers": [OfferEntity.from_dict(_item) for _item in obj.get("payment_offers")] if obj.get("payment_offers") is not None else None
        })
        return _obj


