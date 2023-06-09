# coding: utf-8

"""
    New Payment Gateway APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2022-01-01
    Contact: nextgenapi@cashfree.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cashfree_pg_sdk_python.configuration import Configuration


class CFAuthorizationInPaymentsEntity(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'action': 'str',
        'status': 'str',
        'captured_amount': 'float',
        'start_time': 'str',
        'end_time': 'str',
        'approve_by': 'str'
    }

    attribute_map = {
        'action': 'action',
        'status': 'status',
        'captured_amount': 'captured_amount',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'approve_by': 'approve_by'
    }

    def __init__(self, action=None, status=None, captured_amount=None, start_time=None, end_time=None, approve_by=None, local_vars_configuration=None):  # noqa: E501
        """CFAuthorizationInPaymentsEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._status = None
        self._captured_amount = None
        self._start_time = None
        self._end_time = None
        self._approve_by = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if status is not None:
            self.status = status
        if captured_amount is not None:
            self.captured_amount = captured_amount
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if approve_by is not None:
            self.approve_by = approve_by

    @property
    def action(self):
        """Gets the action of this CFAuthorizationInPaymentsEntity.  # noqa: E501

        One of CAPTURE or VOID  # noqa: E501

        :return: The action of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CFAuthorizationInPaymentsEntity.

        One of CAPTURE or VOID  # noqa: E501

        :param action: The action of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :type action: str
        """
        allowed_values = ["CAPTURE", "VOID"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def status(self):
        """Gets the status of this CFAuthorizationInPaymentsEntity.  # noqa: E501

        One of SUCCESS or PENDING  # noqa: E501

        :return: The status of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CFAuthorizationInPaymentsEntity.

        One of SUCCESS or PENDING  # noqa: E501

        :param status: The status of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :type status: str
        """
        allowed_values = ["SUCCESS", "PENDING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def captured_amount(self):
        """Gets the captured_amount of this CFAuthorizationInPaymentsEntity.  # noqa: E501

        The captured amount for this authorization request  # noqa: E501

        :return: The captured_amount of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :rtype: float
        """
        return self._captured_amount

    @captured_amount.setter
    def captured_amount(self, captured_amount):
        """Sets the captured_amount of this CFAuthorizationInPaymentsEntity.

        The captured amount for this authorization request  # noqa: E501

        :param captured_amount: The captured_amount of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :type captured_amount: float
        """

        self._captured_amount = captured_amount

    @property
    def start_time(self):
        """Gets the start_time of this CFAuthorizationInPaymentsEntity.  # noqa: E501

        Start time of this authorization hold (only for UPI)  # noqa: E501

        :return: The start_time of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CFAuthorizationInPaymentsEntity.

        Start time of this authorization hold (only for UPI)  # noqa: E501

        :param start_time: The start_time of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :type start_time: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CFAuthorizationInPaymentsEntity.  # noqa: E501

        End time of this authorization hold (only for UPI)  # noqa: E501

        :return: The end_time of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CFAuthorizationInPaymentsEntity.

        End time of this authorization hold (only for UPI)  # noqa: E501

        :param end_time: The end_time of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :type end_time: str
        """

        self._end_time = end_time

    @property
    def approve_by(self):
        """Gets the approve_by of this CFAuthorizationInPaymentsEntity.  # noqa: E501

        Approve by time as passed in the authorization request (only for UPI)  # noqa: E501

        :return: The approve_by of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :rtype: str
        """
        return self._approve_by

    @approve_by.setter
    def approve_by(self, approve_by):
        """Sets the approve_by of this CFAuthorizationInPaymentsEntity.

        Approve by time as passed in the authorization request (only for UPI)  # noqa: E501

        :param approve_by: The approve_by of this CFAuthorizationInPaymentsEntity.  # noqa: E501
        :type approve_by: str
        """

        self._approve_by = approve_by

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CFAuthorizationInPaymentsEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CFAuthorizationInPaymentsEntity):
            return True

        return self.to_dict() != other.to_dict()
