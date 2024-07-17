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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt

class CreateSubscriptionRequestAuthorizationDetails(BaseModel):
    """
    CreateSubscriptionRequestAuthorizationDetails
    """
    authorization_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Authorization amount for the auth payment.")
    authorization_amount_refund: Optional[StrictBool] = Field(None, description="Indicates whether the authorization amount should be refunded to the customer automatically. Merchants can use this field to specify if the authorized funds should be returned to the customer after authorization of the subscription.")
    __properties = ["authorization_amount", "authorization_amount_refund"]

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
    def from_json(cls, json_str: str) -> CreateSubscriptionRequestAuthorizationDetails:
        """Create an instance of CreateSubscriptionRequestAuthorizationDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CreateSubscriptionRequestAuthorizationDetails:
        """Create an instance of CreateSubscriptionRequestAuthorizationDetails from a JSON string"""
        temp_dict = json.loads(json_str)
        if "authorization_amount, authorization_amount_refund" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> CreateSubscriptionRequestAuthorizationDetails:
        """Create an instance of CreateSubscriptionRequestAuthorizationDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSubscriptionRequestAuthorizationDetails.parse_obj(obj)

        _obj = CreateSubscriptionRequestAuthorizationDetails.parse_obj({
            "authorization_amount": obj.get("authorization_amount"),
            "authorization_amount_refund": obj.get("authorization_amount_refund")
        })
        return _obj

