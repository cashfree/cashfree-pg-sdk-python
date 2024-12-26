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
from pydantic import BaseModel, Field, StrictStr

class LinkMetaResponseEntity(BaseModel):
    """
    Payment link meta information object
    """
    notify_url: Optional[StrictStr] = Field(None, description="Notification URL for server-server communication. It should be an https URL.")
    upi_intent: Optional[StrictStr] = Field(None, description="If \"true\", link will directly open UPI Intent flow on mobile, and normal link flow elsewhere")
    return_url: Optional[StrictStr] = Field(None, description="The URL to which user will be redirected to after the payment is done on the link. Maximum length: 250.")
    payment_methods: Optional[StrictStr] = Field(None, description="Allowed payment modes for this link. Pass comma-separated values among following options - \"cc\", \"dc\", \"ccc\", \"ppc\", \"nb\", \"upi\", \"paypal\", \"app\". Leave it blank to show all available payment methods")
    __properties = ["notify_url", "upi_intent", "return_url", "payment_methods"]

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
    def from_json(cls, json_str: str) -> LinkMetaResponseEntity:
        """Create an instance of LinkMetaResponseEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> LinkMetaResponseEntity:
        """Create an instance of LinkMetaResponseEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "notify_url, upi_intent, return_url, payment_methods" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LinkMetaResponseEntity:
        """Create an instance of LinkMetaResponseEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LinkMetaResponseEntity.parse_obj(obj)

        _obj = LinkMetaResponseEntity.parse_obj({
            "notify_url": obj.get("notify_url"),
            "upi_intent": obj.get("upi_intent"),
            "return_url": obj.get("return_url"),
            "payment_methods": obj.get("payment_methods")
        })
        return _obj


