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


from typing import Optional, Union
from pydantic import BaseModel, Field, confloat, conint, constr

class PaymentMethodsQueries(BaseModel):
    """
    Payment Method Query Object
    """
    amount: Optional[Union[confloat(ge=1, strict=True), conint(ge=1, strict=True)]] = Field(None, description="Amount of the order.")
    order_id: Optional[constr(strict=True, max_length=50, min_length=3)] = Field(None, description="OrderId of the order. Either of `order_id` or `order_amount` is mandatory.")
    __properties = ["amount", "order_id"]

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
    def from_json(cls, json_str: str) -> PaymentMethodsQueries:
        """Create an instance of PaymentMethodsQueries from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentMethodsQueries:
        """Create an instance of PaymentMethodsQueries from a JSON string"""
        if "amount""order_id" not in json_str:
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
    def from_dict(cls, obj: dict) -> PaymentMethodsQueries:
        """Create an instance of PaymentMethodsQueries from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentMethodsQueries.parse_obj(obj)

        _obj = PaymentMethodsQueries.parse_obj({
            "amount": obj.get("amount"),
            "order_id": obj.get("order_id")
        })
        return _obj


