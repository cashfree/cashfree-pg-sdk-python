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
from pydantic import BaseModel, StrictStr

class CustomerDetailsInDisputesEntity(BaseModel):
    """
    CustomerDetailsInDisputesEntity
    """
    customer_name: Optional[StrictStr] = None
    customer_phone: Optional[StrictStr] = None
    customer_email: Optional[StrictStr] = None
    __properties = ["customer_name", "customer_phone", "customer_email"]

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
    def from_json(cls, json_str: str) -> CustomerDetailsInDisputesEntity:
        """Create an instance of CustomerDetailsInDisputesEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CustomerDetailsInDisputesEntity:
        """Create an instance of CustomerDetailsInDisputesEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "customer_name, customer_phone, customer_email" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> CustomerDetailsInDisputesEntity:
        """Create an instance of CustomerDetailsInDisputesEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomerDetailsInDisputesEntity.parse_obj(obj)

        _obj = CustomerDetailsInDisputesEntity.parse_obj({
            "customer_name": obj.get("customer_name"),
            "customer_phone": obj.get("customer_phone"),
            "customer_email": obj.get("customer_email")
        })
        return _obj

