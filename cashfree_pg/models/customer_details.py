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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr

class CustomerDetails(BaseModel):
    """
    The customer details that are necessary. Note that you can pass dummy details if your use case does not require the customer details.
    """
    customer_id: constr(strict=True, max_length=50, min_length=3) = Field(..., description="A unique identifier for the customer. Use alphanumeric values only.")
    customer_email: Optional[constr(strict=True, max_length=100, min_length=3)] = Field(None, description="Customer email address.")
    customer_phone: constr(strict=True, max_length=10, min_length=10) = Field(..., description="Customer phone number.")
    customer_name: Optional[constr(strict=True, max_length=100, min_length=3)] = Field(None, description="Name of the customer.")
    customer_bank_account_number: Optional[constr(strict=True, max_length=20, min_length=3)] = Field(None, description="Customer bank account. Required if you want to do a bank account check (TPV)")
    customer_bank_ifsc: Optional[StrictStr] = Field(None, description="Customer bank IFSC. Required if you want to do a bank account check (TPV)")
    customer_bank_code: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Customer bank code. Required for net banking payments, if you want to do a bank account check (TPV)")
    __properties = ["customer_id", "customer_email", "customer_phone", "customer_name", "customer_bank_account_number", "customer_bank_ifsc", "customer_bank_code"]

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
    def from_json(cls, json_str: str) -> CustomerDetails:
        """Create an instance of CustomerDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CustomerDetails:
        """Create an instance of CustomerDetails from a JSON string"""
        if "customer_id, customer_email, customer_phone, customer_name, customer_bank_account_number, customer_bank_ifsc, customer_bank_code" not in json_str:
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
    def from_dict(cls, obj: dict) -> CustomerDetails:
        """Create an instance of CustomerDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomerDetails.parse_obj(obj)

        _obj = CustomerDetails.parse_obj({
            "customer_id": obj.get("customer_id"),
            "customer_email": obj.get("customer_email"),
            "customer_phone": obj.get("customer_phone"),
            "customer_name": obj.get("customer_name"),
            "customer_bank_account_number": obj.get("customer_bank_account_number"),
            "customer_bank_ifsc": obj.get("customer_bank_ifsc"),
            "customer_bank_code": obj.get("customer_bank_code")
        })
        return _obj


