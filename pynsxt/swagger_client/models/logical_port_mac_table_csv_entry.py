# coding: utf-8

"""
    NSX API

    VMware NSX REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.csv_record import CsvRecord  # noqa: F401,E501


class LogicalPortMacTableCsvEntry(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mac_type': 'str',
        'mac_address': 'str'
    }

    attribute_map = {
        'mac_type': 'mac_type',
        'mac_address': 'mac_address'
    }

    def __init__(self, mac_type=None, mac_address=None):  # noqa: E501
        """LogicalPortMacTableCsvEntry - a model defined in Swagger"""  # noqa: E501

        self._mac_type = None
        self._mac_address = None
        self.discriminator = None

        self.mac_type = mac_type
        self.mac_address = mac_address

    @property
    def mac_type(self):
        """Gets the mac_type of this LogicalPortMacTableCsvEntry.  # noqa: E501

        The type of the MAC address  # noqa: E501

        :return: The mac_type of this LogicalPortMacTableCsvEntry.  # noqa: E501
        :rtype: str
        """
        return self._mac_type

    @mac_type.setter
    def mac_type(self, mac_type):
        """Sets the mac_type of this LogicalPortMacTableCsvEntry.

        The type of the MAC address  # noqa: E501

        :param mac_type: The mac_type of this LogicalPortMacTableCsvEntry.  # noqa: E501
        :type: str
        """
        if mac_type is None:
            raise ValueError("Invalid value for `mac_type`, must not be `None`")  # noqa: E501
        allowed_values = ["STATIC", "LEARNED"]  # noqa: E501
        if mac_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mac_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mac_type, allowed_values)
            )

        self._mac_type = mac_type

    @property
    def mac_address(self):
        """Gets the mac_address of this LogicalPortMacTableCsvEntry.  # noqa: E501

        The MAC address  # noqa: E501

        :return: The mac_address of this LogicalPortMacTableCsvEntry.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this LogicalPortMacTableCsvEntry.

        The MAC address  # noqa: E501

        :param mac_address: The mac_address of this LogicalPortMacTableCsvEntry.  # noqa: E501
        :type: str
        """
        if mac_address is None:
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LogicalPortMacTableCsvEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
