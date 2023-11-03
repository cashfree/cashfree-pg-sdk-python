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
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr

class CreateOrderRequestTerminal(BaseModel):
    """
    CreateOrderRequestTerminal
    """
    added_on: Optional[StrictStr] = Field(None, description="date time at which terminal is added")
    cf_terminal_id: Optional[StrictInt] = Field(None, description="cashfree terminal id")
    last_updated_on: Optional[StrictStr] = Field(None, description="last instant when this terminal was updated")
    terminal_address: Optional[StrictStr] = Field(None, description="location of terminal")
    terminal_id: constr(strict=True, max_length=100, min_length=3) = Field(..., description="terminal id for merchant reference")
    terminal_name: Optional[StrictStr] = Field(None, description="name of terminal/agent/storefront")
    terminal_note: Optional[StrictStr] = Field(None, description="note given by merchant while creating the terminal")
    terminal_phone_no: StrictStr = Field(..., description="mobile num of the terminal/agent/storefront")
    terminal_status: Optional[StrictStr] = Field(None, description="status of terminal active/inactive")
    terminal_type: constr(strict=True, max_length=10, min_length=4) = Field(..., description="To identify the type of terminal product in use, in this case it is SPOS.")
    __properties = ["added_on", "cf_terminal_id", "last_updated_on", "terminal_address", "terminal_id", "terminal_name", "terminal_note", "terminal_phone_no", "terminal_status", "terminal_type"]

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
    def from_json(cls, json_str: str) -> CreateOrderRequestTerminal:
        """Create an instance of CreateOrderRequestTerminal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateOrderRequestTerminal:
        """Create an instance of CreateOrderRequestTerminal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateOrderRequestTerminal.parse_obj(obj)

        _obj = CreateOrderRequestTerminal.parse_obj({
            "added_on": obj.get("added_on"),
            "cf_terminal_id": obj.get("cf_terminal_id"),
            "last_updated_on": obj.get("last_updated_on"),
            "terminal_address": obj.get("terminal_address"),
            "terminal_id": obj.get("terminal_id"),
            "terminal_name": obj.get("terminal_name"),
            "terminal_note": obj.get("terminal_note"),
            "terminal_phone_no": obj.get("terminal_phone_no"),
            "terminal_status": obj.get("terminal_status"),
            "terminal_type": obj.get("terminal_type")
        })
        return _obj


