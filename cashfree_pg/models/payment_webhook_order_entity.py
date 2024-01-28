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


from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr

class PaymentWebhookOrderEntity(BaseModel):
    """
    order entity in webhook
    """
    order_id: Optional[StrictStr] = None
    order_amount: Optional[Union[StrictFloat, StrictInt]] = None
    order_currency: Optional[StrictStr] = None
    order_tags: Optional[Dict[str, constr(strict=True, max_length=255, min_length=1)]] = Field(None, description="Custom Tags in thr form of {\"key\":\"value\"} which can be passed for an order. A maximum of 10 tags can be added")
    __properties = ["order_id", "order_amount", "order_currency", "order_tags"]

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
    def from_json(cls, json_str: str) -> PaymentWebhookOrderEntity:
        """Create an instance of PaymentWebhookOrderEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentWebhookOrderEntity:
        """Create an instance of PaymentWebhookOrderEntity from a JSON string"""
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
    def from_dict(cls, obj: dict) -> PaymentWebhookOrderEntity:
        """Create an instance of PaymentWebhookOrderEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentWebhookOrderEntity.parse_obj(obj)

        _obj = PaymentWebhookOrderEntity.parse_obj({
            "order_id": obj.get("order_id"),
            "order_amount": obj.get("order_amount"),
            "order_currency": obj.get("order_currency"),
            "order_tags": obj.get("order_tags")
        })
        return _obj


