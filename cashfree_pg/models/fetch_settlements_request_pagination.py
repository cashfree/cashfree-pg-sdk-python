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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class FetchSettlementsRequestPagination(BaseModel):
    """
    To fetch the next set of settlements, pass the cursor received in the response to the next API call.   To receive the data for the first time, pass the cursor as null.   Limit would be number of settlements that you want to receive.
    """
    limit: StrictInt = Field(..., description="The number of settlements you want to fetch. Maximum limit is 1000, default value is 10.")
    cursor: Optional[StrictStr] = Field(None, description="Specifies from where the next set of settlement details should be fetched.")
    __properties = ["limit", "cursor"]

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
    def from_json(cls, json_str: str) -> FetchSettlementsRequestPagination:
        """Create an instance of FetchSettlementsRequestPagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> FetchSettlementsRequestPagination:
        """Create an instance of FetchSettlementsRequestPagination from a JSON string"""
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
    def from_dict(cls, obj: dict) -> FetchSettlementsRequestPagination:
        """Create an instance of FetchSettlementsRequestPagination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FetchSettlementsRequestPagination.parse_obj(obj)

        _obj = FetchSettlementsRequestPagination.parse_obj({
            "limit": obj.get("limit"),
            "cursor": obj.get("cursor")
        })
        return _obj


