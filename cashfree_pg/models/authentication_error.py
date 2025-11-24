from __future__ import annotations
import pprint
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ConfigDict

class AuthenticationError(BaseModel):
    """
    Error if api keys are wrong
    """
    message: Optional[StrictStr] = None
    code: Optional[StrictStr] = None
    type: Optional[StrictStr] = Field(None, description="authentication_error")
    __properties = ["message", "code", "type"]

    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)
    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AuthenticationError:
        """Create an instance of AuthenticationError from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> AuthenticationError:
        """Create an instance of AuthenticationError from a JSON string"""
        temp_dict = json.loads(json_str)
        if "message, code, type" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthenticationError:
        """Create an instance of AuthenticationError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthenticationError.model_validate(obj)

        _obj = AuthenticationError.model_validate({
            "message": obj.get("message"),
            "code": obj.get("code"),
            "type": obj.get("type")
        })
        return _obj
