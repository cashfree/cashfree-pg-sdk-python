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
from pydantic import BaseModel, Field, StrictStr

class FetchTerminalQRCodesEntity(BaseModel):
    """
    Fetch Static QR Codes using terminal ID or phone number
    """
    bank: Optional[StrictStr] = Field(None, description="Name of the bank that is linked to the Static QR.")
    qr_code: Optional[StrictStr] = Field(None, alias="qrCode", description="Base-64 Encoded QR Code URL")
    qr_code_url: Optional[StrictStr] = Field(None, alias="qrCodeUrl", description="URL of the qr Code.")
    status: Optional[StrictStr] = Field(None, description="Status of the static QR.")
    __properties = ["bank", "qrCode", "qrCodeUrl", "status"]

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
    def from_json(cls, json_str: str) -> FetchTerminalQRCodesEntity:
        """Create an instance of FetchTerminalQRCodesEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> FetchTerminalQRCodesEntity:
        """Create an instance of FetchTerminalQRCodesEntity from a JSON string"""
        if "bank, qrCode, qrCodeUrl, status" not in json_str:
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
    def from_dict(cls, obj: dict) -> FetchTerminalQRCodesEntity:
        """Create an instance of FetchTerminalQRCodesEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FetchTerminalQRCodesEntity.parse_obj(obj)

        _obj = FetchTerminalQRCodesEntity.parse_obj({
            "bank": obj.get("bank"),
            "qr_code": obj.get("qrCode"),
            "qr_code_url": obj.get("qrCodeUrl"),
            "status": obj.get("status")
        })
        return _obj


