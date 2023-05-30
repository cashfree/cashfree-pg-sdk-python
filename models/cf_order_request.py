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


class CFOrderRequest(object):
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
        'order_id': 'str',
        'order_amount': 'float',
        'order_currency': 'str',
        'customer_details': 'CFCustomerDetails',
        'order_meta': 'CFOrderMeta',
        'order_expiry_time': 'str',
        'order_note': 'str',
        'order_tags': 'dict[str, str]',
        'order_splits': 'list[CFVendorSplit]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'order_amount': 'order_amount',
        'order_currency': 'order_currency',
        'customer_details': 'customer_details',
        'order_meta': 'order_meta',
        'order_expiry_time': 'order_expiry_time',
        'order_note': 'order_note',
        'order_tags': 'order_tags',
        'order_splits': 'order_splits'
    }

    def __init__(self, order_id=None, order_amount=None, order_currency=None, customer_details=None, order_meta=None, order_expiry_time=None, order_note=None, order_tags=None, order_splits=None, local_vars_configuration=None):  # noqa: E501
        """CFOrderRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._order_id = None
        self._order_amount = None
        self._order_currency = None
        self._customer_details = None
        self._order_meta = None
        self._order_expiry_time = None
        self._order_note = None
        self._order_tags = None
        self._order_splits = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        self.order_amount = order_amount
        self.order_currency = order_currency
        self.customer_details = customer_details
        if order_meta is not None:
            self.order_meta = order_meta
        if order_expiry_time is not None:
            self.order_expiry_time = order_expiry_time
        if order_note is not None:
            self.order_note = order_note
        if order_tags is not None:
            self.order_tags = order_tags
        if order_splits is not None:
            self.order_splits = order_splits

    @property
    def order_id(self):
        """Gets the order_id of this CFOrderRequest.  # noqa: E501

        Order identifier present in your system. Alphanumeric and only - and _ allowed.  # noqa: E501

        :return: The order_id of this CFOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CFOrderRequest.

        Order identifier present in your system. Alphanumeric and only - and _ allowed.  # noqa: E501

        :param order_id: The order_id of this CFOrderRequest.  # noqa: E501
        :type order_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                order_id is not None and len(order_id) > 45):
            raise ValueError("Invalid value for `order_id`, length must be less than or equal to `45`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                order_id is not None and len(order_id) < 3):
            raise ValueError("Invalid value for `order_id`, length must be greater than or equal to `3`")  # noqa: E501

        self._order_id = order_id

    @property
    def order_amount(self):
        """Gets the order_amount of this CFOrderRequest.  # noqa: E501

        Bill amount for the order. Provide upto two decimals. 10.15 means Rs 10 and 15 paisa  # noqa: E501

        :return: The order_amount of this CFOrderRequest.  # noqa: E501
        :rtype: float
        """
        return self._order_amount

    @order_amount.setter
    def order_amount(self, order_amount):
        """Sets the order_amount of this CFOrderRequest.

        Bill amount for the order. Provide upto two decimals. 10.15 means Rs 10 and 15 paisa  # noqa: E501

        :param order_amount: The order_amount of this CFOrderRequest.  # noqa: E501
        :type order_amount: float
        """
        if self.local_vars_configuration.client_side_validation and order_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `order_amount`, must not be `None`")  # noqa: E501

        self._order_amount = order_amount

    @property
    def order_currency(self):
        """Gets the order_currency of this CFOrderRequest.  # noqa: E501

        Currency for the order. INR if left empty. Contact care@cashfree.com to enable new currencies.   # noqa: E501

        :return: The order_currency of this CFOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_currency

    @order_currency.setter
    def order_currency(self, order_currency):
        """Sets the order_currency of this CFOrderRequest.

        Currency for the order. INR if left empty. Contact care@cashfree.com to enable new currencies.   # noqa: E501

        :param order_currency: The order_currency of this CFOrderRequest.  # noqa: E501
        :type order_currency: str
        """
        if self.local_vars_configuration.client_side_validation and order_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `order_currency`, must not be `None`")  # noqa: E501

        self._order_currency = order_currency

    @property
    def customer_details(self):
        """Gets the customer_details of this CFOrderRequest.  # noqa: E501


        :return: The customer_details of this CFOrderRequest.  # noqa: E501
        :rtype: CFCustomerDetails
        """
        return self._customer_details

    @customer_details.setter
    def customer_details(self, customer_details):
        """Sets the customer_details of this CFOrderRequest.


        :param customer_details: The customer_details of this CFOrderRequest.  # noqa: E501
        :type customer_details: CFCustomerDetails
        """
        if self.local_vars_configuration.client_side_validation and customer_details is None:  # noqa: E501
            raise ValueError("Invalid value for `customer_details`, must not be `None`")  # noqa: E501

        self._customer_details = customer_details

    @property
    def order_meta(self):
        """Gets the order_meta of this CFOrderRequest.  # noqa: E501


        :return: The order_meta of this CFOrderRequest.  # noqa: E501
        :rtype: CFOrderMeta
        """
        return self._order_meta

    @order_meta.setter
    def order_meta(self, order_meta):
        """Sets the order_meta of this CFOrderRequest.


        :param order_meta: The order_meta of this CFOrderRequest.  # noqa: E501
        :type order_meta: CFOrderMeta
        """

        self._order_meta = order_meta

    @property
    def order_expiry_time(self):
        """Gets the order_expiry_time of this CFOrderRequest.  # noqa: E501

        Time after which the order expires. Customers will not be able to make the payment beyond the time specified here. We store timestamps in IST, but you can provide them in a valid ISO 8601 time format.  # noqa: E501

        :return: The order_expiry_time of this CFOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_expiry_time

    @order_expiry_time.setter
    def order_expiry_time(self, order_expiry_time):
        """Sets the order_expiry_time of this CFOrderRequest.

        Time after which the order expires. Customers will not be able to make the payment beyond the time specified here. We store timestamps in IST, but you can provide them in a valid ISO 8601 time format.  # noqa: E501

        :param order_expiry_time: The order_expiry_time of this CFOrderRequest.  # noqa: E501
        :type order_expiry_time: str
        """

        self._order_expiry_time = order_expiry_time

    @property
    def order_note(self):
        """Gets the order_note of this CFOrderRequest.  # noqa: E501

        Order note for reference.  # noqa: E501

        :return: The order_note of this CFOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_note

    @order_note.setter
    def order_note(self, order_note):
        """Sets the order_note of this CFOrderRequest.

        Order note for reference.  # noqa: E501

        :param order_note: The order_note of this CFOrderRequest.  # noqa: E501
        :type order_note: str
        """
        if (self.local_vars_configuration.client_side_validation and
                order_note is not None and len(order_note) > 200):
            raise ValueError("Invalid value for `order_note`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                order_note is not None and len(order_note) < 3):
            raise ValueError("Invalid value for `order_note`, length must be greater than or equal to `3`")  # noqa: E501

        self._order_note = order_note

    @property
    def order_tags(self):
        """Gets the order_tags of this CFOrderRequest.  # noqa: E501

        Custom Tags which can be passed for an order. A maximum of 6 tags can be added  # noqa: E501

        :return: The order_tags of this CFOrderRequest.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._order_tags

    @order_tags.setter
    def order_tags(self, order_tags):
        """Sets the order_tags of this CFOrderRequest.

        Custom Tags which can be passed for an order. A maximum of 6 tags can be added  # noqa: E501

        :param order_tags: The order_tags of this CFOrderRequest.  # noqa: E501
        :type order_tags: dict[str, str]
        """

        self._order_tags = order_tags

    @property
    def order_splits(self):
        """Gets the order_splits of this CFOrderRequest.  # noqa: E501


        :return: The order_splits of this CFOrderRequest.  # noqa: E501
        :rtype: list[CFVendorSplit]
        """
        return self._order_splits

    @order_splits.setter
    def order_splits(self, order_splits):
        """Sets the order_splits of this CFOrderRequest.


        :param order_splits: The order_splits of this CFOrderRequest.  # noqa: E501
        :type order_splits: list[CFVendorSplit]
        """

        self._order_splits = order_splits

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
        if not isinstance(other, CFOrderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CFOrderRequest):
            return True

        return self.to_dict() != other.to_dict()