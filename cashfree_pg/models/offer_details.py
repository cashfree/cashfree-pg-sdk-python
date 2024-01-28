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
from pydantic import BaseModel, Field, constr, validator
from cashfree_pg.models.cashback_details import CashbackDetails
from cashfree_pg.models.discount_details import DiscountDetails

class OfferDetails(BaseModel):
    """
    Offer details and type
    """
    offer_type: constr(strict=True, max_length=50, min_length=3) = Field(..., description="Offer Type for the Offer.")
    discount_details: Optional[DiscountDetails] = None
    cashback_details: Optional[CashbackDetails] = None
    __properties = ["offer_type", "discount_details", "cashback_details"]

    @validator('offer_type')
    def offer_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DISCOUNT', 'CASHBACK', 'DISCOUNT_AND_CASHBACK', 'NO_COST_EMI'):
            raise ValueError("must be one of enum values ('DISCOUNT', 'CASHBACK', 'DISCOUNT_AND_CASHBACK', 'NO_COST_EMI')")
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
    def from_json(cls, json_str: str) -> OfferDetails:
        """Create an instance of OfferDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OfferDetails:
        """Create an instance of OfferDetails from a JSON string"""
        if "" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of discount_details
        if self.discount_details:
            _dict['discount_details'] = self.discount_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cashback_details
        if self.cashback_details:
            _dict['cashback_details'] = self.cashback_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferDetails:
        """Create an instance of OfferDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferDetails.parse_obj(obj)

        _obj = OfferDetails.parse_obj({
            "offer_type": obj.get("offer_type"),
            "discount_details": DiscountDetails.from_dict(obj.get("discount_details")) if obj.get("discount_details") is not None else None,
            "cashback_details": CashbackDetails.from_dict(obj.get("cashback_details")) if obj.get("cashback_details") is not None else None
        })
        return _obj


