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


class CFLinkCancelledResponse(object):
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
        'cf_link_id': 'int',
        'link_id': 'str',
        'link_status': 'str',
        'link_currency': 'str',
        'link_amount': 'float',
        'link_amount_paid': 'float',
        'link_partial_payments': 'bool',
        'link_minimum_partial_amount': 'float',
        'link_purpose': 'str',
        'link_created_at': 'str',
        'customer_details': 'CFLinkCustomerDetailsEntity',
        'link_meta': 'CFLinkMetaEntity',
        'link_url': 'str',
        'link_expiry_time': 'str',
        'link_notes': 'dict[str, str]',
        'link_auto_reminders': 'bool',
        'link_notify': 'CFLinkNotifyEntity'
    }

    attribute_map = {
        'cf_link_id': 'cf_link_id',
        'link_id': 'link_id',
        'link_status': 'link_status',
        'link_currency': 'link_currency',
        'link_amount': 'link_amount',
        'link_amount_paid': 'link_amount_paid',
        'link_partial_payments': 'link_partial_payments',
        'link_minimum_partial_amount': 'link_minimum_partial_amount',
        'link_purpose': 'link_purpose',
        'link_created_at': 'link_created_at',
        'customer_details': 'customer_details',
        'link_meta': 'link_meta',
        'link_url': 'link_url',
        'link_expiry_time': 'link_expiry_time',
        'link_notes': 'link_notes',
        'link_auto_reminders': 'link_auto_reminders',
        'link_notify': 'link_notify'
    }

    def __init__(self, cf_link_id=None, link_id=None, link_status=None, link_currency=None, link_amount=None, link_amount_paid=None, link_partial_payments=None, link_minimum_partial_amount=None, link_purpose=None, link_created_at=None, customer_details=None, link_meta=None, link_url=None, link_expiry_time=None, link_notes=None, link_auto_reminders=None, link_notify=None, local_vars_configuration=None):  # noqa: E501
        """CFLinkCancelledResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cf_link_id = None
        self._link_id = None
        self._link_status = None
        self._link_currency = None
        self._link_amount = None
        self._link_amount_paid = None
        self._link_partial_payments = None
        self._link_minimum_partial_amount = None
        self._link_purpose = None
        self._link_created_at = None
        self._customer_details = None
        self._link_meta = None
        self._link_url = None
        self._link_expiry_time = None
        self._link_notes = None
        self._link_auto_reminders = None
        self._link_notify = None
        self.discriminator = None

        if cf_link_id is not None:
            self.cf_link_id = cf_link_id
        if link_id is not None:
            self.link_id = link_id
        if link_status is not None:
            self.link_status = link_status
        if link_currency is not None:
            self.link_currency = link_currency
        if link_amount is not None:
            self.link_amount = link_amount
        if link_amount_paid is not None:
            self.link_amount_paid = link_amount_paid
        if link_partial_payments is not None:
            self.link_partial_payments = link_partial_payments
        if link_minimum_partial_amount is not None:
            self.link_minimum_partial_amount = link_minimum_partial_amount
        if link_purpose is not None:
            self.link_purpose = link_purpose
        if link_created_at is not None:
            self.link_created_at = link_created_at
        if customer_details is not None:
            self.customer_details = customer_details
        if link_meta is not None:
            self.link_meta = link_meta
        if link_url is not None:
            self.link_url = link_url
        if link_expiry_time is not None:
            self.link_expiry_time = link_expiry_time
        if link_notes is not None:
            self.link_notes = link_notes
        if link_auto_reminders is not None:
            self.link_auto_reminders = link_auto_reminders
        if link_notify is not None:
            self.link_notify = link_notify

    @property
    def cf_link_id(self):
        """Gets the cf_link_id of this CFLinkCancelledResponse.  # noqa: E501


        :return: The cf_link_id of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: int
        """
        return self._cf_link_id

    @cf_link_id.setter
    def cf_link_id(self, cf_link_id):
        """Sets the cf_link_id of this CFLinkCancelledResponse.


        :param cf_link_id: The cf_link_id of this CFLinkCancelledResponse.  # noqa: E501
        :type cf_link_id: int
        """

        self._cf_link_id = cf_link_id

    @property
    def link_id(self):
        """Gets the link_id of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_id of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """Sets the link_id of this CFLinkCancelledResponse.


        :param link_id: The link_id of this CFLinkCancelledResponse.  # noqa: E501
        :type link_id: str
        """

        self._link_id = link_id

    @property
    def link_status(self):
        """Gets the link_status of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_status of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_status

    @link_status.setter
    def link_status(self, link_status):
        """Sets the link_status of this CFLinkCancelledResponse.


        :param link_status: The link_status of this CFLinkCancelledResponse.  # noqa: E501
        :type link_status: str
        """

        self._link_status = link_status

    @property
    def link_currency(self):
        """Gets the link_currency of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_currency of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_currency

    @link_currency.setter
    def link_currency(self, link_currency):
        """Sets the link_currency of this CFLinkCancelledResponse.


        :param link_currency: The link_currency of this CFLinkCancelledResponse.  # noqa: E501
        :type link_currency: str
        """

        self._link_currency = link_currency

    @property
    def link_amount(self):
        """Gets the link_amount of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_amount of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: float
        """
        return self._link_amount

    @link_amount.setter
    def link_amount(self, link_amount):
        """Sets the link_amount of this CFLinkCancelledResponse.


        :param link_amount: The link_amount of this CFLinkCancelledResponse.  # noqa: E501
        :type link_amount: float
        """

        self._link_amount = link_amount

    @property
    def link_amount_paid(self):
        """Gets the link_amount_paid of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_amount_paid of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: float
        """
        return self._link_amount_paid

    @link_amount_paid.setter
    def link_amount_paid(self, link_amount_paid):
        """Sets the link_amount_paid of this CFLinkCancelledResponse.


        :param link_amount_paid: The link_amount_paid of this CFLinkCancelledResponse.  # noqa: E501
        :type link_amount_paid: float
        """

        self._link_amount_paid = link_amount_paid

    @property
    def link_partial_payments(self):
        """Gets the link_partial_payments of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_partial_payments of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: bool
        """
        return self._link_partial_payments

    @link_partial_payments.setter
    def link_partial_payments(self, link_partial_payments):
        """Sets the link_partial_payments of this CFLinkCancelledResponse.


        :param link_partial_payments: The link_partial_payments of this CFLinkCancelledResponse.  # noqa: E501
        :type link_partial_payments: bool
        """

        self._link_partial_payments = link_partial_payments

    @property
    def link_minimum_partial_amount(self):
        """Gets the link_minimum_partial_amount of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_minimum_partial_amount of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: float
        """
        return self._link_minimum_partial_amount

    @link_minimum_partial_amount.setter
    def link_minimum_partial_amount(self, link_minimum_partial_amount):
        """Sets the link_minimum_partial_amount of this CFLinkCancelledResponse.


        :param link_minimum_partial_amount: The link_minimum_partial_amount of this CFLinkCancelledResponse.  # noqa: E501
        :type link_minimum_partial_amount: float
        """

        self._link_minimum_partial_amount = link_minimum_partial_amount

    @property
    def link_purpose(self):
        """Gets the link_purpose of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_purpose of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_purpose

    @link_purpose.setter
    def link_purpose(self, link_purpose):
        """Sets the link_purpose of this CFLinkCancelledResponse.


        :param link_purpose: The link_purpose of this CFLinkCancelledResponse.  # noqa: E501
        :type link_purpose: str
        """

        self._link_purpose = link_purpose

    @property
    def link_created_at(self):
        """Gets the link_created_at of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_created_at of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_created_at

    @link_created_at.setter
    def link_created_at(self, link_created_at):
        """Sets the link_created_at of this CFLinkCancelledResponse.


        :param link_created_at: The link_created_at of this CFLinkCancelledResponse.  # noqa: E501
        :type link_created_at: str
        """

        self._link_created_at = link_created_at

    @property
    def customer_details(self):
        """Gets the customer_details of this CFLinkCancelledResponse.  # noqa: E501


        :return: The customer_details of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: CFLinkCustomerDetailsEntity
        """
        return self._customer_details

    @customer_details.setter
    def customer_details(self, customer_details):
        """Sets the customer_details of this CFLinkCancelledResponse.


        :param customer_details: The customer_details of this CFLinkCancelledResponse.  # noqa: E501
        :type customer_details: CFLinkCustomerDetailsEntity
        """

        self._customer_details = customer_details

    @property
    def link_meta(self):
        """Gets the link_meta of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_meta of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: CFLinkMetaEntity
        """
        return self._link_meta

    @link_meta.setter
    def link_meta(self, link_meta):
        """Sets the link_meta of this CFLinkCancelledResponse.


        :param link_meta: The link_meta of this CFLinkCancelledResponse.  # noqa: E501
        :type link_meta: CFLinkMetaEntity
        """

        self._link_meta = link_meta

    @property
    def link_url(self):
        """Gets the link_url of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_url of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this CFLinkCancelledResponse.


        :param link_url: The link_url of this CFLinkCancelledResponse.  # noqa: E501
        :type link_url: str
        """

        self._link_url = link_url

    @property
    def link_expiry_time(self):
        """Gets the link_expiry_time of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_expiry_time of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_expiry_time

    @link_expiry_time.setter
    def link_expiry_time(self, link_expiry_time):
        """Sets the link_expiry_time of this CFLinkCancelledResponse.


        :param link_expiry_time: The link_expiry_time of this CFLinkCancelledResponse.  # noqa: E501
        :type link_expiry_time: str
        """

        self._link_expiry_time = link_expiry_time

    @property
    def link_notes(self):
        """Gets the link_notes of this CFLinkCancelledResponse.  # noqa: E501

        Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs  # noqa: E501

        :return: The link_notes of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._link_notes

    @link_notes.setter
    def link_notes(self, link_notes):
        """Sets the link_notes of this CFLinkCancelledResponse.

        Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs  # noqa: E501

        :param link_notes: The link_notes of this CFLinkCancelledResponse.  # noqa: E501
        :type link_notes: dict[str, str]
        """

        self._link_notes = link_notes

    @property
    def link_auto_reminders(self):
        """Gets the link_auto_reminders of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_auto_reminders of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: bool
        """
        return self._link_auto_reminders

    @link_auto_reminders.setter
    def link_auto_reminders(self, link_auto_reminders):
        """Sets the link_auto_reminders of this CFLinkCancelledResponse.


        :param link_auto_reminders: The link_auto_reminders of this CFLinkCancelledResponse.  # noqa: E501
        :type link_auto_reminders: bool
        """

        self._link_auto_reminders = link_auto_reminders

    @property
    def link_notify(self):
        """Gets the link_notify of this CFLinkCancelledResponse.  # noqa: E501


        :return: The link_notify of this CFLinkCancelledResponse.  # noqa: E501
        :rtype: CFLinkNotifyEntity
        """
        return self._link_notify

    @link_notify.setter
    def link_notify(self, link_notify):
        """Sets the link_notify of this CFLinkCancelledResponse.


        :param link_notify: The link_notify of this CFLinkCancelledResponse.  # noqa: E501
        :type link_notify: CFLinkNotifyEntity
        """

        self._link_notify = link_notify

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
        if not isinstance(other, CFLinkCancelledResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CFLinkCancelledResponse):
            return True

        return self.to_dict() != other.to_dict()