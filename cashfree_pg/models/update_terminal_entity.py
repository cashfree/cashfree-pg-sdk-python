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
from pydantic import BaseModel, StrictInt, StrictStr
from cashfree_pg.models.create_terminal_request_terminal_meta import CreateTerminalRequestTerminalMeta

class UpdateTerminalEntity(BaseModel):
    """
    Update terminal response
    """
    added_on: Optional[StrictStr] = None
    cf_terminal_id: Optional[StrictInt] = None
    last_updated_on: Optional[StrictStr] = None
    terminal_address: Optional[StrictStr] = None
    terminal_email: Optional[StrictStr] = None
    terminal_type: Optional[StrictStr] = None
    teminal_id: Optional[StrictStr] = None
    terminal_name: Optional[StrictStr] = None
    terminal_note: Optional[StrictStr] = None
    terminal_phone_no: Optional[StrictStr] = None
    terminal_status: Optional[StrictStr] = None
    terminal_meta: Optional[CreateTerminalRequestTerminalMeta] = None
    __properties = ["added_on", "cf_terminal_id", "last_updated_on", "terminal_address", "terminal_email", "terminal_type", "teminal_id", "terminal_name", "terminal_note", "terminal_phone_no", "terminal_status", "terminal_meta"]

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
    def from_json(cls, json_str: str) -> UpdateTerminalEntity:
        """Create an instance of UpdateTerminalEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> UpdateTerminalEntity:
        """Create an instance of UpdateTerminalEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "added_on, cf_terminal_id, last_updated_on, terminal_address, terminal_email, terminal_type, teminal_id, terminal_name, terminal_note, terminal_phone_no, terminal_status, terminal_meta" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of terminal_meta
        if self.terminal_meta:
            _dict['terminal_meta'] = self.terminal_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateTerminalEntity:
        """Create an instance of UpdateTerminalEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateTerminalEntity.parse_obj(obj)

        _obj = UpdateTerminalEntity.parse_obj({
            "added_on": obj.get("added_on"),
            "cf_terminal_id": obj.get("cf_terminal_id"),
            "last_updated_on": obj.get("last_updated_on"),
            "terminal_address": obj.get("terminal_address"),
            "terminal_email": obj.get("terminal_email"),
            "terminal_type": obj.get("terminal_type"),
            "teminal_id": obj.get("teminal_id"),
            "terminal_name": obj.get("terminal_name"),
            "terminal_note": obj.get("terminal_note"),
            "terminal_phone_no": obj.get("terminal_phone_no"),
            "terminal_status": obj.get("terminal_status"),
            "terminal_meta": CreateTerminalRequestTerminalMeta.from_dict(obj.get("terminal_meta")) if obj.get("terminal_meta") is not None else None
        })
        return _obj


