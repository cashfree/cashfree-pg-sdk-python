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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from cashfree_pg.models.card import CARD
from cashfree_pg.models.enach import ENACH
from cashfree_pg.models.pnach import PNACH
from cashfree_pg.models.upi import UPI
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

CREATESUBSCRIPTIONPAYMENTREQUESTPAYMENTMETHOD_ONE_OF_SCHEMAS = ["CARD", "ENACH", "PNACH", "UPI"]

class CreateSubscriptionPaymentRequestPaymentMethod(BaseModel):
    """
    Payment method. Can be one of [\"upi\", \"enach\", \"pnach\", \"card\"]
    """
    # data type: UPI
    oneof_schema_1_validator: Optional[UPI] = None
    # data type: ENACH
    oneof_schema_2_validator: Optional[ENACH] = None
    # data type: PNACH
    oneof_schema_3_validator: Optional[PNACH] = None
    # data type: CARD
    oneof_schema_4_validator: Optional[CARD] = None
    if TYPE_CHECKING:
        actual_instance: Union[CARD, ENACH, PNACH, UPI]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(CREATESUBSCRIPTIONPAYMENTREQUESTPAYMENTMETHOD_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CreateSubscriptionPaymentRequestPaymentMethod.construct()
        error_messages = []
        match = 0
        # validate data type: UPI
        if not isinstance(v, UPI):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UPI`")
        else:
            match += 1
        # validate data type: ENACH
        if not isinstance(v, ENACH):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ENACH`")
        else:
            match += 1
        # validate data type: PNACH
        if not isinstance(v, PNACH):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PNACH`")
        else:
            match += 1
        # validate data type: CARD
        if not isinstance(v, CARD):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CARD`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateSubscriptionPaymentRequestPaymentMethod with oneOf schemas: CARD, ENACH, PNACH, UPI. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateSubscriptionPaymentRequestPaymentMethod with oneOf schemas: CARD, ENACH, PNACH, UPI. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSubscriptionPaymentRequestPaymentMethod:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> CreateSubscriptionPaymentRequestPaymentMethod:
        """Returns the object represented by the json string"""
        instance = CreateSubscriptionPaymentRequestPaymentMethod.construct()
        error_messages = []
        match = 0

        # deserialize data into UPI
        try:
            instance.actual_instance = UPI.from_json_for_one_of(json_str)
            match += 1
            if (instance.actual_instance is not None):
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ENACH
        try:
            instance.actual_instance = ENACH.from_json_for_one_of(json_str)
            match += 1
            if (instance.actual_instance is not None):
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PNACH
        try:
            instance.actual_instance = PNACH.from_json_for_one_of(json_str)
            match += 1
            if (instance.actual_instance is not None):
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CARD
        try:
            instance.actual_instance = CARD.from_json_for_one_of(json_str)
            match += 1
            if (instance.actual_instance is not None):
                return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateSubscriptionPaymentRequestPaymentMethod with oneOf schemas: CARD, ENACH, PNACH, UPI. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateSubscriptionPaymentRequestPaymentMethod with oneOf schemas: CARD, ENACH, PNACH, UPI. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

