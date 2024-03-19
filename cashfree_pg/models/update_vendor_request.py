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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from cashfree_pg.models.bank_details import BankDetails
from cashfree_pg.models.kyc_details import KycDetails
from cashfree_pg.models.upi_details import UpiDetails

class UpdateVendorRequest(BaseModel):
    """
    Update Vendor Request
    """
    status: StrictStr = Field(..., description="Specify the status of vendor that should be updated. Possible values: ACTIVE,BLOCKED, DELETED")
    name: StrictStr = Field(..., description="Specify the name of the vendor to be updated. Name should not have any special character except . / - &")
    email: StrictStr = Field(..., description="Specify the vendor email ID that should be updated. String in email ID format (Ex:johndoe_1@cashfree.com) should contain @ and dot (.)")
    phone: StrictStr = Field(..., description="Specify the beneficiaries phone number to be updated. Phone number registered in India (only digits, 8 - 12 characters after excluding +91).")
    verify_account: Optional[StrictBool] = Field(None, description="Specify if the vendor bank account details should be verified. Possible values: true or false")
    dashboard_access: Optional[StrictBool] = Field(None, description="Update if the vendor will have dashboard access or not. Possible values are: true or false")
    schedule_option: Union[StrictFloat, StrictInt] = Field(..., description="Specify the settlement cycle to be updated. View the settlement cycle details from the \"Settlement Cycles Supported\" table. If no schedule option is configured, the settlement cycle ID \"1\" will be in effect. Select \"8\" or \"9\" if you want to schedule instant vendor settlements.")
    bank: Optional[conlist(BankDetails)] = Field(None, description="Specify the vendor bank account details to be updated.")
    upi: Optional[conlist(UpiDetails)] = Field(None, description="Updated beneficiary upi vpa. Alphanumeric, dot (.), hyphen (-), at sign (@), and underscore allowed (100 character limit). Note: underscore and dot (.) gets accepted before and after @, but hyphen (-) is only accepted before @ sign.")
    kyc_details: conlist(KycDetails) = Field(..., description="Specify the kyc details that should be updated.")
    __properties = ["status", "name", "email", "phone", "verify_account", "dashboard_access", "schedule_option", "bank", "upi", "kyc_details"]

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
    def from_json(cls, json_str: str) -> UpdateVendorRequest:
        """Create an instance of UpdateVendorRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> UpdateVendorRequest:
        """Create an instance of UpdateVendorRequest from a JSON string"""
        temp_dict = json.loads(json_str)
        if "status, name, email, phone, verify_account, dashboard_access, schedule_option, bank, upi, kyc_details" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in bank (list)
        _items = []
        if self.bank:
            for _item in self.bank:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bank'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in upi (list)
        _items = []
        if self.upi:
            for _item in self.upi:
                if _item:
                    _items.append(_item.to_dict())
            _dict['upi'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in kyc_details (list)
        _items = []
        if self.kyc_details:
            for _item in self.kyc_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['kyc_details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateVendorRequest:
        """Create an instance of UpdateVendorRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateVendorRequest.parse_obj(obj)

        _obj = UpdateVendorRequest.parse_obj({
            "status": obj.get("status"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "verify_account": obj.get("verify_account"),
            "dashboard_access": obj.get("dashboard_access"),
            "schedule_option": obj.get("schedule_option"),
            "bank": [BankDetails.from_dict(_item) for _item in obj.get("bank")] if obj.get("bank") is not None else None,
            "upi": [UpiDetails.from_dict(_item) for _item in obj.get("upi")] if obj.get("upi") is not None else None,
            "kyc_details": [KycDetails.from_dict(_item) for _item in obj.get("kyc_details")] if obj.get("kyc_details") is not None else None
        })
        return _obj


