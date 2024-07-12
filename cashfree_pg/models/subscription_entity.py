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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from cashfree_pg.models.authorization_details import AuthorizationDetails
from cashfree_pg.models.plan_entity import PlanEntity
from cashfree_pg.models.subscription_customer_details import SubscriptionCustomerDetails
from cashfree_pg.models.subscription_entity_subscription_meta import SubscriptionEntitySubscriptionMeta
from cashfree_pg.models.subscription_payment_split_item import SubscriptionPaymentSplitItem

class SubscriptionEntity(BaseModel):
    """
    The response returned for Get, Create or Manage Subscription APIs.
    """
    authorisation_details: Optional[AuthorizationDetails] = None
    cf_subscription_id: Optional[StrictStr] = Field(None, description="Cashfree subscription reference number")
    customer_details: Optional[SubscriptionCustomerDetails] = None
    plan_details: Optional[PlanEntity] = None
    subscription_expiry_time: Optional[StrictStr] = Field(None, description="Time at which the subscription will expire.")
    subscription_first_charge_time: Optional[StrictStr] = Field(None, description="Time at which the first charge will be made for the subscription. Applicable only for PERIODIC plans.")
    subscription_id: Optional[StrictStr] = Field(None, description="A unique ID passed by merchant for identifying the subscription.")
    subscription_meta: Optional[SubscriptionEntitySubscriptionMeta] = None
    subscription_note: Optional[StrictStr] = Field(None, description="Note for the subscription.")
    subscription_payment_splits: Optional[conlist(SubscriptionPaymentSplitItem)] = Field(None, description="Payment splits for the subscription.")
    subscription_status: Optional[StrictStr] = Field(None, description="Status of the subscription.")
    subscription_tags: Optional[Dict[str, Any]] = Field(None, description="Tags for the subscription.")
    __properties = ["authorisation_details", "cf_subscription_id", "customer_details", "plan_details", "subscription_expiry_time", "subscription_first_charge_time", "subscription_id", "subscription_meta", "subscription_note", "subscription_payment_splits", "subscription_status", "subscription_tags"]

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
    def from_json(cls, json_str: str) -> SubscriptionEntity:
        """Create an instance of SubscriptionEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> SubscriptionEntity:
        """Create an instance of SubscriptionEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if "authorisation_details, cf_subscription_id, customer_details, plan_details, subscription_expiry_time, subscription_first_charge_time, subscription_id, subscription_meta, subscription_note, subscription_payment_splits, subscription_status, subscription_tags" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of authorisation_details
        if self.authorisation_details:
            _dict['authorisation_details'] = self.authorisation_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_details
        if self.customer_details:
            _dict['customer_details'] = self.customer_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan_details
        if self.plan_details:
            _dict['plan_details'] = self.plan_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscription_meta
        if self.subscription_meta:
            _dict['subscription_meta'] = self.subscription_meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subscription_payment_splits (list)
        _items = []
        if self.subscription_payment_splits:
            for _item in self.subscription_payment_splits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subscription_payment_splits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionEntity:
        """Create an instance of SubscriptionEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionEntity.parse_obj(obj)

        _obj = SubscriptionEntity.parse_obj({
            "authorisation_details": AuthorizationDetails.from_dict(obj.get("authorisation_details")) if obj.get("authorisation_details") is not None else None,
            "cf_subscription_id": obj.get("cf_subscription_id"),
            "customer_details": SubscriptionCustomerDetails.from_dict(obj.get("customer_details")) if obj.get("customer_details") is not None else None,
            "plan_details": PlanEntity.from_dict(obj.get("plan_details")) if obj.get("plan_details") is not None else None,
            "subscription_expiry_time": obj.get("subscription_expiry_time"),
            "subscription_first_charge_time": obj.get("subscription_first_charge_time"),
            "subscription_id": obj.get("subscription_id"),
            "subscription_meta": SubscriptionEntitySubscriptionMeta.from_dict(obj.get("subscription_meta")) if obj.get("subscription_meta") is not None else None,
            "subscription_note": obj.get("subscription_note"),
            "subscription_payment_splits": [SubscriptionPaymentSplitItem.from_dict(_item) for _item in obj.get("subscription_payment_splits")] if obj.get("subscription_payment_splits") is not None else None,
            "subscription_status": obj.get("subscription_status"),
            "subscription_tags": obj.get("subscription_tags")
        })
        return _obj


