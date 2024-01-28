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


from typing import Optional, Union
from pydantic import BaseModel, Field, confloat, conint
from cashfree_pg.models.offer_validations_payment_method import OfferValidationsPaymentMethod

class OfferValidations(BaseModel):
    """
    Offer validation object
    """
    min_amount: Optional[Union[confloat(ge=1, strict=True), conint(ge=1, strict=True)]] = Field(None, description="Minimum Amount for Offer to be Applicable")
    payment_method: OfferValidationsPaymentMethod = Field(...)
    max_allowed: Union[confloat(ge=1, strict=True), conint(ge=1, strict=True)] = Field(..., description="Maximum amount of Offer that can be availed.")
    __properties = ["min_amount", "payment_method", "max_allowed"]

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
    def from_json(cls, json_str: str) -> OfferValidations:
        """Create an instance of OfferValidations from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OfferValidations:
        """Create an instance of OfferValidations from a JSON string"""
        if "min_amount""payment_method""max_allowed" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['payment_method'] = self.payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferValidations:
        """Create an instance of OfferValidations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferValidations.parse_obj(obj)

        _obj = OfferValidations.parse_obj({
            "min_amount": obj.get("min_amount"),
            "payment_method": OfferValidationsPaymentMethod.from_dict(obj.get("payment_method")) if obj.get("payment_method") is not None else None,
            "max_allowed": obj.get("max_allowed")
        })
        return _obj


