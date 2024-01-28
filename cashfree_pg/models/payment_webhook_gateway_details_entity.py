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


from typing import Optional
from pydantic import BaseModel, StrictStr

class PaymentWebhookGatewayDetailsEntity(BaseModel):
    """
    payment gatewat details present in the webhook response
    """
    gateway_name: Optional[StrictStr] = None
    gateway_order_id: Optional[StrictStr] = None
    gateway_payment_id: Optional[StrictStr] = None
    gateway_status_code: Optional[StrictStr] = None
    gateway_settlement: Optional[StrictStr] = None
    __properties = ["gateway_name", "gateway_order_id", "gateway_payment_id", "gateway_status_code", "gateway_settlement"]

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
    def from_json(cls, json_str: str) -> PaymentWebhookGatewayDetailsEntity:
        """Create an instance of PaymentWebhookGatewayDetailsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentWebhookGatewayDetailsEntity:
        """Create an instance of PaymentWebhookGatewayDetailsEntity from a JSON string"""
        if "gateway_name""gateway_order_id""gateway_payment_id""gateway_status_code""gateway_settlement" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentWebhookGatewayDetailsEntity:
        """Create an instance of PaymentWebhookGatewayDetailsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentWebhookGatewayDetailsEntity.parse_obj(obj)

        _obj = PaymentWebhookGatewayDetailsEntity.parse_obj({
            "gateway_name": obj.get("gateway_name"),
            "gateway_order_id": obj.get("gateway_order_id"),
            "gateway_payment_id": obj.get("gateway_payment_id"),
            "gateway_status_code": obj.get("gateway_status_code"),
            "gateway_settlement": obj.get("gateway_settlement")
        })
        return _obj


