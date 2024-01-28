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
from pydantic import BaseModel, StrictInt, StrictStr

class TerminalTransactionEntity(BaseModel):
    """
    Create terminal response object
    """
    cf_payment_id: Optional[StrictInt] = None
    payment_amount: Optional[StrictInt] = None
    payment_method: Optional[StrictStr] = None
    payment_url: Optional[StrictStr] = None
    qrcode: Optional[StrictStr] = None
    timeout: Optional[StrictStr] = None
    __properties = ["cf_payment_id", "payment_amount", "payment_method", "payment_url", "qrcode", "timeout"]

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
    def from_json(cls, json_str: str) -> TerminalTransactionEntity:
        """Create an instance of TerminalTransactionEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> TerminalTransactionEntity:
        """Create an instance of TerminalTransactionEntity from a JSON string"""
        if "cf_payment_idpayment_amountpayment_methodpayment_urlqrcodetimeout" not in json_str:
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
    def from_dict(cls, obj: dict) -> TerminalTransactionEntity:
        """Create an instance of TerminalTransactionEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TerminalTransactionEntity.parse_obj(obj)

        _obj = TerminalTransactionEntity.parse_obj({
            "cf_payment_id": obj.get("cf_payment_id"),
            "payment_amount": obj.get("payment_amount"),
            "payment_method": obj.get("payment_method"),
            "payment_url": obj.get("payment_url"),
            "qrcode": obj.get("qrcode"),
            "timeout": obj.get("timeout")
        })
        return _obj


