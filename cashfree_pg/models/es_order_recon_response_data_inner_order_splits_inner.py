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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from cashfree_pg.models.es_order_recon_response_data_inner_order_splits_inner_split_inner import ESOrderReconResponseDataInnerOrderSplitsInnerSplitInner

class ESOrderReconResponseDataInnerOrderSplitsInner(BaseModel):
    """
    ESOrderReconResponseDataInnerOrderSplitsInner
    """
    split: Optional[conlist(ESOrderReconResponseDataInnerOrderSplitsInnerSplitInner)] = None
    created_at: Optional[StrictStr] = None
    __properties = ["split", "created_at"]

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
    def from_json(cls, json_str: str) -> ESOrderReconResponseDataInnerOrderSplitsInner:
        """Create an instance of ESOrderReconResponseDataInnerOrderSplitsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> ESOrderReconResponseDataInnerOrderSplitsInner:
        """Create an instance of ESOrderReconResponseDataInnerOrderSplitsInner from a JSON string"""
        temp_dict = json.loads(json_str)
        if "split, created_at" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in split (list)
        _items = []
        if self.split:
            for _item in self.split:
                if _item:
                    _items.append(_item.to_dict())
            _dict['split'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ESOrderReconResponseDataInnerOrderSplitsInner:
        """Create an instance of ESOrderReconResponseDataInnerOrderSplitsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ESOrderReconResponseDataInnerOrderSplitsInner.parse_obj(obj)

        _obj = ESOrderReconResponseDataInnerOrderSplitsInner.parse_obj({
            "split": [ESOrderReconResponseDataInnerOrderSplitsInnerSplitInner.from_dict(_item) for _item in obj.get("split")] if obj.get("split") is not None else None,
            "created_at": obj.get("created_at")
        })
        return _obj

