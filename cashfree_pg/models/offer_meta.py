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



from pydantic import BaseModel, Field, StrictStr, constr

class OfferMeta(BaseModel):
    """
    Offer meta details object
    """
    offer_title: constr(strict=True, max_length=50, min_length=3) = Field(..., description="Title for the Offer.")
    offer_description: constr(strict=True, max_length=100, min_length=3) = Field(..., description="Description for the Offer.")
    offer_code: constr(strict=True, max_length=45, min_length=1) = Field(..., description="Unique identifier for the Offer.")
    offer_start_time: constr(strict=True, max_length=20, min_length=3) = Field(..., description="Start Time for the Offer")
    offer_end_time: StrictStr = Field(..., description="Expiry Time for the Offer")
    __properties = ["offer_title", "offer_description", "offer_code", "offer_start_time", "offer_end_time"]

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
    def from_json(cls, json_str: str) -> OfferMeta:
        """Create an instance of OfferMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OfferMeta:
        """Create an instance of OfferMeta from a JSON string"""
        temp_dict = json.loads(json_str)
        if temp_dict["offer_title, offer_description, offer_code, offer_start_time, offer_end_time"] in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferMeta:
        """Create an instance of OfferMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferMeta.parse_obj(obj)

        _obj = OfferMeta.parse_obj({
            "offer_title": obj.get("offer_title"),
            "offer_description": obj.get("offer_description"),
            "offer_code": obj.get("offer_code"),
            "offer_start_time": obj.get("offer_start_time"),
            "offer_end_time": obj.get("offer_end_time")
        })
        return _obj


