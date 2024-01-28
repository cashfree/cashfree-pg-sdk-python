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


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictStr

class OrderMeta(BaseModel):
    """
    Optional meta details to control how the customer pays and how payment journey completes
    """
    return_url: Optional[StrictStr] = Field(None, description="The URL to which user will be redirected to after the payment on bank OTP page. Maximum length: 250. The return_url must contain placeholder {order_id}. When redirecting the customer back to the return url from the bank’s OTP page, Cashfree will replace this placeholder with the actual value for that order.")
    notify_url: Optional[StrictStr] = Field(None, description="Notification URL for server-server communication. Useful when user's connection drops while re-directing. NotifyUrl should be an https URL. Maximum length: 250.")
    payment_methods: Optional[Any] = Field(None, description="Allowed payment modes for this order. Pass comma-separated values among following options - \"cc\", \"dc\", \"ccc\", \"ppc\",\"nb\",\"upi\",\"paypal\",\"app\",\"paylater\",\"cardlessemi\",\"dcemi\",\"ccemi\",\"banktransfer\". Leave it blank to show all available payment methods")
    __properties = ["return_url", "notify_url", "payment_methods"]

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
    def from_json(cls, json_str: str) -> OrderMeta:
        """Create an instance of OrderMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OrderMeta:
        """Create an instance of OrderMeta from a JSON string"""
        if "return_url", "notify_url", "payment_methods" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if payment_methods (nullable) is None
        # and __fields_set__ contains the field
        if self.payment_methods is None and "payment_methods" in self.__fields_set__:
            _dict['payment_methods'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderMeta:
        """Create an instance of OrderMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderMeta.parse_obj(obj)

        _obj = OrderMeta.parse_obj({
            "return_url": obj.get("return_url"),
            "notify_url": obj.get("notify_url"),
            "payment_methods": obj.get("payment_methods")
        })
        return _obj


