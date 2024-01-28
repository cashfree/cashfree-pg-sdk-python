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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from cashfree_pg.models.upi_authorize_details import UPIAuthorizeDetails

class Upi(BaseModel):
    """
    UPI collect payment method object
    """
    channel: StrictStr = Field(..., description="Specify the channel through which the payment must be processed. Can be one of [\"link\", \"collect\", \"qrcode\"]")
    upi_id: Optional[StrictStr] = Field(None, description="Customer UPI VPA to process payment.  ### Important This is a required parameter for channel = `collect` ")
    upi_redirect_url: Optional[StrictBool] = Field(None, description="use this if you want cashfree to show a loader. Sample response below. It is only supported for collect `action:collect` will be returned with `data.url` having the link for redirection ")
    upi_expiry_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The UPI request will be valid for this expiry minutes. This parameter is only applicable for a UPI collect payment. The default value is 5 minutes. You should keep the minimum as 5 minutes, and maximum as 15 minutes")
    authorize_only: Optional[StrictBool] = Field(None, description="For one time mandate on UPI. Set this as authorize_only = true. Please note that you can only use the \"collect\" channel if you are sending a one time mandate request")
    authorization: Optional[UPIAuthorizeDetails] = None
    __properties = ["channel", "upi_id", "upi_redirect_url", "upi_expiry_minutes", "authorize_only", "authorization"]

    @validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('link', 'collect', 'qrcode'):
            raise ValueError("must be one of enum values ('link', 'collect', 'qrcode')")
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
    def from_json(cls, json_str: str) -> Upi:
        """Create an instance of Upi from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> Upi:
        """Create an instance of Upi from a JSON string"""
        if "channelupi_idupi_redirect_urlupi_expiry_minutesauthorize_onlyauthorization" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of authorization
        if self.authorization:
            _dict['authorization'] = self.authorization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Upi:
        """Create an instance of Upi from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Upi.parse_obj(obj)

        _obj = Upi.parse_obj({
            "channel": obj.get("channel"),
            "upi_id": obj.get("upi_id"),
            "upi_redirect_url": obj.get("upi_redirect_url"),
            "upi_expiry_minutes": obj.get("upi_expiry_minutes"),
            "authorize_only": obj.get("authorize_only"),
            "authorization": UPIAuthorizeDetails.from_dict(obj.get("authorization")) if obj.get("authorization") is not None else None
        })
        return _obj


