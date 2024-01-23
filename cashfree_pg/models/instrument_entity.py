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
from pydantic import BaseModel, Field, StrictStr, validator
from cashfree_pg.models.saved_instrument_meta import SavedInstrumentMeta

class InstrumentEntity(BaseModel):
    """
    Saved card instrument object
    """
    customer_id: Optional[StrictStr] = Field(None, description="customer_id for which the instrument was saved")
    afa_reference: Optional[StrictStr] = Field(None, description="cf_payment_id of the successful transaction done while saving instrument")
    instrument_id: Optional[StrictStr] = Field(None, description="saved instrument id")
    instrument_type: Optional[StrictStr] = Field(None, description="Type of the saved instrument")
    instrument_uid: Optional[StrictStr] = Field(None, description="Unique id for the saved instrument")
    instrument_display: Optional[StrictStr] = Field(None, description="masked card number displayed to the customer")
    instrument_status: Optional[StrictStr] = Field(None, description="Status of the saved instrument.")
    created_at: Optional[StrictStr] = Field(None, description="Timestamp at which instrument was saved.")
    instrument_meta: Optional[SavedInstrumentMeta] = None
    __properties = ["customer_id", "afa_reference", "instrument_id", "instrument_type", "instrument_uid", "instrument_display", "instrument_status", "created_at", "instrument_meta"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('card'):
            raise ValueError("must be one of enum values ('card')")
        return value

    @validator('instrument_status')
    def instrument_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'INACTIVE'):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE')")
        return value

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
    def from_json(cls, json_str: str) -> InstrumentEntity:
        """Create an instance of InstrumentEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of instrument_meta
        if self.instrument_meta:
            _dict['instrument_meta'] = self.instrument_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstrumentEntity:
        """Create an instance of InstrumentEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstrumentEntity.parse_obj(obj)

        _obj = InstrumentEntity.parse_obj({
            "customer_id": obj.get("customer_id"),
            "afa_reference": obj.get("afa_reference"),
            "instrument_id": obj.get("instrument_id"),
            "instrument_type": obj.get("instrument_type"),
            "instrument_uid": obj.get("instrument_uid"),
            "instrument_display": obj.get("instrument_display"),
            "instrument_status": obj.get("instrument_status"),
            "created_at": obj.get("created_at"),
            "instrument_meta": SavedInstrumentMeta.from_dict(obj.get("instrument_meta")) if obj.get("instrument_meta") is not None else None
        })
        return _obj


