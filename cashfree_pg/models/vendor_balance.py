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


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class VendorBalance(BaseModel):
    """
    Vendor Balance entity object
    """
    merchant_id: Optional[Union[StrictFloat, StrictInt]] = None
    vendor_id: Optional[StrictStr] = None
    merchant_unsettled: Optional[Union[StrictFloat, StrictInt]] = None
    vendor_unsettled: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["merchant_id", "vendor_id", "merchant_unsettled", "vendor_unsettled"]

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
    def from_json(cls, json_str: str) -> VendorBalance:
        """Create an instance of VendorBalance from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> VendorBalance:
        """Create an instance of VendorBalance from a JSON string"""
        temp_dict = json.loads(json_str)
        if "merchant_id, vendor_id, merchant_unsettled, vendor_unsettled" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> VendorBalance:
        """Create an instance of VendorBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VendorBalance.parse_obj(obj)

        _obj = VendorBalance.parse_obj({
            "merchant_id": obj.get("merchant_id"),
            "vendor_id": obj.get("vendor_id"),
            "merchant_unsettled": obj.get("merchant_unsettled"),
            "vendor_unsettled": obj.get("vendor_unsettled")
        })
        return _obj

