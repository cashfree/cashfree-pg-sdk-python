# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2023-08-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from cashfree_pg.models.pay_order_request_payment_method import PayOrderRequestPaymentMethod

class PayOrderRequest(BaseModel):
    """
    Complete object for the pay api that uses payment method objects
    """
    payment_session_id: StrictStr = Field(...)
    payment_method: PayOrderRequestPaymentMethod = Field(...)
    save_instrument: Optional[StrictBool] = None
    offer_id: Optional[StrictStr] = Field(None, description="This is required if any offers needs to be applied to the order.")
    __properties = ["payment_session_id", "payment_method", "save_instrument", "offer_id"]

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
    def from_json(cls, json_str: str) -> PayOrderRequest:
        """Create an instance of PayOrderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['payment_method'] = self.payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PayOrderRequest:
        """Create an instance of PayOrderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PayOrderRequest.parse_obj(obj)

        _obj = PayOrderRequest.parse_obj({
            "payment_session_id": obj.get("payment_session_id"),
            "payment_method": PayOrderRequestPaymentMethod.from_dict(obj.get("payment_method")) if obj.get("payment_method") is not None else None,
            "save_instrument": obj.get("save_instrument"),
            "offer_id": obj.get("offer_id")
        })
        return _obj


