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



from pydantic import BaseModel, Field
from cashfree_pg.models.cardless_emi_queries import CardlessEMIQueries

class EligibilityFetchCardlessEMIRequest(BaseModel):
    """
    eligibilty request for cardless
    """
    queries: CardlessEMIQueries = Field(...)
    __properties = ["queries"]

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
    def from_json(cls, json_str: str) -> EligibilityFetchCardlessEMIRequest:
        """Create an instance of EligibilityFetchCardlessEMIRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of queries
        if self.queries:
            _dict['queries'] = self.queries.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EligibilityFetchCardlessEMIRequest:
        """Create an instance of EligibilityFetchCardlessEMIRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EligibilityFetchCardlessEMIRequest.parse_obj(obj)

        _obj = EligibilityFetchCardlessEMIRequest.parse_obj({
            "queries": CardlessEMIQueries.from_dict(obj.get("queries")) if obj.get("queries") is not None else None
        })
        return _obj


