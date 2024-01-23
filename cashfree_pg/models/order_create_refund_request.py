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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from cashfree_pg.models.vendor_split import VendorSplit

class OrderCreateRefundRequest(BaseModel):
    """
    create refund request object
    """
    refund_amount: Union[StrictFloat, StrictInt] = Field(..., description="Amount to be refunded. Should be lesser than or equal to the transaction amount. (Decimals allowed)")
    refund_id: constr(strict=True, max_length=40, min_length=3) = Field(..., description="An unique ID to associate the refund with. Provie alphanumeric values")
    refund_note: Optional[constr(strict=True, max_length=100, min_length=3)] = Field(None, description="A refund note for your reference.")
    refund_speed: Optional[StrictStr] = Field(None, description="Speed at which the refund is processed. It's an optional field with default being STANDARD")
    refund_splits: Optional[conlist(VendorSplit)] = None
    __properties = ["refund_amount", "refund_id", "refund_note", "refund_speed", "refund_splits"]

    @validator('refund_speed')
    def refund_speed_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('STANDARD', 'INSTANT'):
            raise ValueError("must be one of enum values ('STANDARD', 'INSTANT')")
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
    def from_json(cls, json_str: str) -> OrderCreateRefundRequest:
        """Create an instance of OrderCreateRefundRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in refund_splits (list)
        _items = []
        if self.refund_splits:
            for _item in self.refund_splits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['refund_splits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderCreateRefundRequest:
        """Create an instance of OrderCreateRefundRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderCreateRefundRequest.parse_obj(obj)

        _obj = OrderCreateRefundRequest.parse_obj({
            "refund_amount": obj.get("refund_amount"),
            "refund_id": obj.get("refund_id"),
            "refund_note": obj.get("refund_note"),
            "refund_speed": obj.get("refund_speed"),
            "refund_splits": [VendorSplit.from_dict(_item) for _item in obj.get("refund_splits")] if obj.get("refund_splits") is not None else None
        })
        return _obj


