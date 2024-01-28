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
from pydantic import BaseModel, Field, StrictStr, validator

class Paylater(BaseModel):
    """
    Paylater payment method
    """
    channel: Optional[StrictStr] = Field(None, description="The channel for cardless EMI is always `link`")
    provider: Optional[StrictStr] = Field(None, description="One of [\"kotak\", \"flexipay\", \"zestmoney\", \"lazypay\", \"olapostpaid\",\"simpl\", \"freechargepaylater\"]. Please note that Flexipay is offered by HDFC bank")
    phone: Optional[StrictStr] = Field(None, description="Customers phone number for this payment instrument. If the customer is not eligible you will receive a 400 error with type as 'invalid_request_error' and code as 'invalid_request_error'")
    __properties = ["channel", "provider", "phone"]

    @validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('kotak', 'flexipay', 'zestmoney', 'lazypay', 'olapostpaid', 'simpl', 'freechargepaylater'):
            raise ValueError("must be one of enum values ('kotak', 'flexipay', 'zestmoney', 'lazypay', 'olapostpaid', 'simpl', 'freechargepaylater')")
        return value

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
    def from_json(cls, json_str: str) -> Paylater:
        """Create an instance of Paylater from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> Paylater:
        """Create an instance of Paylater from a JSON string"""
        if "" not in json_str:
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
    def from_dict(cls, obj: dict) -> Paylater:
        """Create an instance of Paylater from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Paylater.parse_obj(obj)

        _obj = Paylater.parse_obj({
            "channel": obj.get("channel"),
            "provider": obj.get("provider"),
            "phone": obj.get("phone")
        })
        return _obj


