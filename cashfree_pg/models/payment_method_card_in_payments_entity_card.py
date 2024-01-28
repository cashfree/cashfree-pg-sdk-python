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
from pydantic import BaseModel, StrictStr

class PaymentMethodCardInPaymentsEntityCard(BaseModel):
    """
    PaymentMethodCardInPaymentsEntityCard
    """
    channel: Optional[StrictStr] = None
    card_number: Optional[StrictStr] = None
    card_network: Optional[StrictStr] = None
    card_type: Optional[StrictStr] = None
    card_country: Optional[StrictStr] = None
    card_bank_name: Optional[StrictStr] = None
    card_network_reference_id: Optional[StrictStr] = None
    __properties = ["channel", "card_number", "card_network", "card_type", "card_country", "card_bank_name", "card_network_reference_id"]

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
    def from_json(cls, json_str: str) -> PaymentMethodCardInPaymentsEntityCard:
        """Create an instance of PaymentMethodCardInPaymentsEntityCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentMethodCardInPaymentsEntityCard:
        """Create an instance of PaymentMethodCardInPaymentsEntityCard from a JSON string"""
        if "channelcard_numbercard_networkcard_typecard_countrycard_bank_namecard_network_reference_id" not in json_str:
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
    def from_dict(cls, obj: dict) -> PaymentMethodCardInPaymentsEntityCard:
        """Create an instance of PaymentMethodCardInPaymentsEntityCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentMethodCardInPaymentsEntityCard.parse_obj(obj)

        _obj = PaymentMethodCardInPaymentsEntityCard.parse_obj({
            "channel": obj.get("channel"),
            "card_number": obj.get("card_number"),
            "card_network": obj.get("card_network"),
            "card_type": obj.get("card_type"),
            "card_country": obj.get("card_country"),
            "card_bank_name": obj.get("card_bank_name"),
            "card_network_reference_id": obj.get("card_network_reference_id")
        })
        return _obj


