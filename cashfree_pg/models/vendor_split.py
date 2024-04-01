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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class VendorSplit(BaseModel):
    """
    Use to split order when cashfree's Easy Split is enabled for your account.
    """
    vendor_id: StrictStr = Field(..., description="Vendor id created in Cashfree system")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Amount which will be associated with this vendor")
    percentage: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Percentage of order amount which shall get added to vendor account")
    tags: Optional[Dict[str, Dict[str, Any]]] = Field(None, description="Custom Tags in thr form of {\"key\":\"value\"} which can be passed for an order. A maximum of 10 tags can be added")
    __properties = ["vendor_id", "amount", "percentage", "tags"]

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
    def from_json(cls, json_str: str) -> VendorSplit:
        """Create an instance of VendorSplit from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> VendorSplit:
        """Create an instance of VendorSplit from a JSON string"""
        temp_dict = json.loads(json_str)
        if "vendor_id, amount, percentage, tags" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> VendorSplit:
        """Create an instance of VendorSplit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VendorSplit.parse_obj(obj)

        _obj = VendorSplit.parse_obj({
            "vendor_id": obj.get("vendor_id"),
            "amount": obj.get("amount"),
            "percentage": obj.get("percentage"),
            "tags": obj.get("tags")
        })
        return _obj


