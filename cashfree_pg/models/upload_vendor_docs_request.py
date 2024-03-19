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
from pydantic import BaseModel, Field, StrictBytes, StrictStr

class UploadVendorDocsRequest(BaseModel):
    """
    Update Vendor Request
    """
    doc_type: Optional[StrictStr] = Field(None, description="Mention the type of the document you are uploading. Possible values: UIDAI_FRONT, UIDAI_BACK, UIDAI_NUMBER, DL, DL_NUMBER, PASSPORT_FRONT, PASSPORT_BACK, PASSPORT_NUMBER, VOTER_ID, VOTER_ID_NUMBER, PAN, PAN_NUMBER, GST, GSTIN_NUMBER, CIN, CIN_NUMBER, NBFC_CERTIFICATE. If the doc type ends with a number you should add the doc value else upload the doc file.")
    doc_value: Optional[Union[StrictBytes, StrictStr]] = Field(None, description="Enter the display name of the uploaded file.")
    file: Optional[StrictStr] = Field(None, description="Select the document that should be uploaded or provide the path of that file. You cannot upload a file that is more than 2MB in size.")
    __properties = ["doc_type", "doc_value", "file"]

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
    def from_json(cls, json_str: str) -> UploadVendorDocsRequest:
        """Create an instance of UploadVendorDocsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> UploadVendorDocsRequest:
        """Create an instance of UploadVendorDocsRequest from a JSON string"""
        temp_dict = json.loads(json_str)
        if "doc_type, doc_value, file" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> UploadVendorDocsRequest:
        """Create an instance of UploadVendorDocsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UploadVendorDocsRequest.parse_obj(obj)

        _obj = UploadVendorDocsRequest.parse_obj({
            "doc_type": obj.get("doc_type"),
            "doc_value": obj.get("doc_value"),
            "file": obj.get("file")
        })
        return _obj


