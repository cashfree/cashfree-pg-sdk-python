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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from cashfree_pg.models.app_payment_method import AppPaymentMethod
from cashfree_pg.models.card_emi_payment_method import CardEMIPaymentMethod
from cashfree_pg.models.card_payment_method import CardPaymentMethod
from cashfree_pg.models.cardless_emi_payment_method import CardlessEMIPaymentMethod
from cashfree_pg.models.net_banking_payment_method import NetBankingPaymentMethod
from cashfree_pg.models.paylater_payment_method import PaylaterPaymentMethod
from cashfree_pg.models.upi_payment_method import UPIPaymentMethod
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

PAYORDERREQUESTPAYMENTMETHOD_ONE_OF_SCHEMAS = ["AppPaymentMethod", "CardEMIPaymentMethod", "CardPaymentMethod", "CardlessEMIPaymentMethod", "NetBankingPaymentMethod", "PaylaterPaymentMethod", "UPIPaymentMethod"]

class PayOrderRequestPaymentMethod(BaseModel):
    """
    PayOrderRequestPaymentMethod
    """
    # data type: CardPaymentMethod
    oneof_schema_1_validator: Optional[CardPaymentMethod] = None
    # data type: UPIPaymentMethod
    oneof_schema_2_validator: Optional[UPIPaymentMethod] = None
    # data type: NetBankingPaymentMethod
    oneof_schema_3_validator: Optional[NetBankingPaymentMethod] = None
    # data type: AppPaymentMethod
    oneof_schema_4_validator: Optional[AppPaymentMethod] = None
    # data type: CardEMIPaymentMethod
    oneof_schema_5_validator: Optional[CardEMIPaymentMethod] = None
    # data type: CardlessEMIPaymentMethod
    oneof_schema_6_validator: Optional[CardlessEMIPaymentMethod] = None
    # data type: PaylaterPaymentMethod
    oneof_schema_7_validator: Optional[PaylaterPaymentMethod] = None
    if TYPE_CHECKING:
        actual_instance: Union[AppPaymentMethod, CardEMIPaymentMethod, CardPaymentMethod, CardlessEMIPaymentMethod, NetBankingPaymentMethod, PaylaterPaymentMethod, UPIPaymentMethod]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(PAYORDERREQUESTPAYMENTMETHOD_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

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
        instance = PayOrderRequestPaymentMethod.construct()
        error_messages = []
        match = 0
        # validate data type: CardPaymentMethod
        if not isinstance(v, CardPaymentMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CardPaymentMethod`")
        else:
            match += 1
        # validate data type: UPIPaymentMethod
        if not isinstance(v, UPIPaymentMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UPIPaymentMethod`")
        else:
            match += 1
        # validate data type: NetBankingPaymentMethod
        if not isinstance(v, NetBankingPaymentMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NetBankingPaymentMethod`")
        else:
            match += 1
        # validate data type: AppPaymentMethod
        if not isinstance(v, AppPaymentMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AppPaymentMethod`")
        else:
            match += 1
        # validate data type: CardEMIPaymentMethod
        if not isinstance(v, CardEMIPaymentMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CardEMIPaymentMethod`")
        else:
            match += 1
        # validate data type: CardlessEMIPaymentMethod
        if not isinstance(v, CardlessEMIPaymentMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CardlessEMIPaymentMethod`")
        else:
            match += 1
        # validate data type: PaylaterPaymentMethod
        if not isinstance(v, PaylaterPaymentMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaylaterPaymentMethod`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PayOrderRequestPaymentMethod with oneOf schemas: AppPaymentMethod, CardEMIPaymentMethod, CardPaymentMethod, CardlessEMIPaymentMethod, NetBankingPaymentMethod, PaylaterPaymentMethod, UPIPaymentMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PayOrderRequestPaymentMethod with oneOf schemas: AppPaymentMethod, CardEMIPaymentMethod, CardPaymentMethod, CardlessEMIPaymentMethod, NetBankingPaymentMethod, PaylaterPaymentMethod, UPIPaymentMethod. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> PayOrderRequestPaymentMethod:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> PayOrderRequestPaymentMethod:
        """Returns the object represented by the json string"""
        instance = PayOrderRequestPaymentMethod.construct()
        error_messages = []
        match = 0

        # deserialize data into CardPaymentMethod
        try:
            instance.actual_instance = CardPaymentMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UPIPaymentMethod
        try:
            instance.actual_instance = UPIPaymentMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NetBankingPaymentMethod
        try:
            instance.actual_instance = NetBankingPaymentMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AppPaymentMethod
        try:
            instance.actual_instance = AppPaymentMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CardEMIPaymentMethod
        try:
            instance.actual_instance = CardEMIPaymentMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CardlessEMIPaymentMethod
        try:
            instance.actual_instance = CardlessEMIPaymentMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaylaterPaymentMethod
        try:
            instance.actual_instance = PaylaterPaymentMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PayOrderRequestPaymentMethod with oneOf schemas: AppPaymentMethod, CardEMIPaymentMethod, CardPaymentMethod, CardlessEMIPaymentMethod, NetBankingPaymentMethod, PaylaterPaymentMethod, UPIPaymentMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PayOrderRequestPaymentMethod with oneOf schemas: AppPaymentMethod, CardEMIPaymentMethod, CardPaymentMethod, CardlessEMIPaymentMethod, NetBankingPaymentMethod, PaylaterPaymentMethod, UPIPaymentMethod. Details: " + ", ".join(error_messages))
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


