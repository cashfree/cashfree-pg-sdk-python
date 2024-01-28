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
from pydantic import BaseModel, Field, StrictInt, constr

class CreateTerminalTransactionRequest(BaseModel):
    """
    Request body to create a terminal transaction
    """
    cf_order_id: StrictInt = Field(..., description="cashfree order ID that was returned while creating an order.")
    cf_terminal_id: Optional[StrictInt] = Field(None, description="cashfree terminal id. this is a required parameter when you do not provide the terminal phone number.")
    payment_method: constr(strict=True, max_length=100, min_length=3) = Field(..., description="mention the payment method used for the transaction. possible values - QR_CODE, LINK.")
    terminal_phone_no: Optional[constr(strict=True, max_length=10, min_length=10)] = Field(None, description="agent mobile number assigned to the terminal. this is a required parameter when you do not provide the cf_terminal_id.")
    __properties = ["cf_order_id", "cf_terminal_id", "payment_method", "terminal_phone_no"]

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
    def from_json(cls, json_str: str) -> CreateTerminalTransactionRequest:
        """Create an instance of CreateTerminalTransactionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CreateTerminalTransactionRequest:
        """Create an instance of CreateTerminalTransactionRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> CreateTerminalTransactionRequest:
        """Create an instance of CreateTerminalTransactionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTerminalTransactionRequest.parse_obj(obj)

        _obj = CreateTerminalTransactionRequest.parse_obj({
            "cf_order_id": obj.get("cf_order_id"),
            "cf_terminal_id": obj.get("cf_terminal_id"),
            "payment_method": obj.get("payment_method"),
            "terminal_phone_no": obj.get("terminal_phone_no")
        })
        return _obj


