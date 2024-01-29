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
from pydantic import BaseModel
from cashfree_pg.models.payment_method_app_in_payments_entity_app import PaymentMethodAppInPaymentsEntityApp

class PaymentMethodAppInPaymentsEntity(BaseModel):
    """
    payment method app object in payment entity
    """
    app: Optional[PaymentMethodAppInPaymentsEntityApp] = None
    __properties = ["app"]

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
    def from_json(cls, json_str: str) -> PaymentMethodAppInPaymentsEntity:
        """Create an instance of PaymentMethodAppInPaymentsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentMethodAppInPaymentsEntity:
        """Create an instance of PaymentMethodAppInPaymentsEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if temp_dict["app"] in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['app'] = self.app.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodAppInPaymentsEntity:
        """Create an instance of PaymentMethodAppInPaymentsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentMethodAppInPaymentsEntity.parse_obj(obj)

        _obj = PaymentMethodAppInPaymentsEntity.parse_obj({
            "app": PaymentMethodAppInPaymentsEntityApp.from_dict(obj.get("app")) if obj.get("app") is not None else None
        })
        return _obj


