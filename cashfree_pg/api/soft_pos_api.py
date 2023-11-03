# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import List, Optional

from cashfree_pg.models.create_terminal_request import CreateTerminalRequest
from cashfree_pg.models.create_terminal_transaction_request import CreateTerminalTransactionRequest
from cashfree_pg.models.fetch_terminal_qr_codes_entity import FetchTerminalQRCodesEntity
from cashfree_pg.models.terminal_entity import TerminalEntity
from cashfree_pg.models.terminal_transaction_entity import TerminalTransactionEntity
from cashfree_pg.configuration import Configuration
from cashfree_pg.api_client import ApiClient
from cashfree_pg.api_response import ApiResponse
from cashfree_pg.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)