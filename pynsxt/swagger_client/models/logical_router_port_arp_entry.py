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


class LogicalRouterPortArpEntry(object):
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
        'ip': 'str',
        'mac_address': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'mac_address': 'mac_address'
    }

    def __init__(self, ip=None, mac_address=None):  # noqa: E501
        """LogicalRouterPortArpEntry - a model defined in Swagger"""  # noqa: E501

        self._ip = None
        self._mac_address = None
        self.discriminator = None

        self.ip = ip
        self.mac_address = mac_address

    @property
    def ip(self):
        """Gets the ip of this LogicalRouterPortArpEntry.  # noqa: E501

        The IP address  # noqa: E501

        :return: The ip of this LogicalRouterPortArpEntry.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this LogicalRouterPortArpEntry.

        The IP address  # noqa: E501

        :param ip: The ip of this LogicalRouterPortArpEntry.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def mac_address(self):
        """Gets the mac_address of this LogicalRouterPortArpEntry.  # noqa: E501

        The MAC address  # noqa: E501

        :return: The mac_address of this LogicalRouterPortArpEntry.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this LogicalRouterPortArpEntry.

        The MAC address  # noqa: E501

        :param mac_address: The mac_address of this LogicalRouterPortArpEntry.  # noqa: E501
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
        if not isinstance(other, LogicalRouterPortArpEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
