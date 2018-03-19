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

from swagger_client.models.file import File  # noqa: F401,E501


class ApplianceFileUsage(object):
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
        'files': 'list[File]',
        'type': 'str',
        'build': 'str'
    }

    attribute_map = {
        'files': 'files',
        'type': 'type',
        'build': 'build'
    }

    def __init__(self, files=None, type=None, build=None):  # noqa: E501
        """ApplianceFileUsage - a model defined in Swagger"""  # noqa: E501

        self._files = None
        self._type = None
        self._build = None
        self.discriminator = None

        self.files = files
        self.type = type
        self.build = build

    @property
    def files(self):
        """Gets the files of this ApplianceFileUsage.  # noqa: E501

        list of files  # noqa: E501

        :return: The files of this ApplianceFileUsage.  # noqa: E501
        :rtype: list[File]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ApplianceFileUsage.

        list of files  # noqa: E501

        :param files: The files of this ApplianceFileUsage.  # noqa: E501
        :type: list[File]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    @property
    def type(self):
        """Gets the type of this ApplianceFileUsage.  # noqa: E501

        Appliance type  # noqa: E501

        :return: The type of this ApplianceFileUsage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApplianceFileUsage.

        Appliance type  # noqa: E501

        :param type: The type of this ApplianceFileUsage.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def build(self):
        """Gets the build of this ApplianceFileUsage.  # noqa: E501

        Appliance build number  # noqa: E501

        :return: The build of this ApplianceFileUsage.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ApplianceFileUsage.

        Appliance build number  # noqa: E501

        :param build: The build of this ApplianceFileUsage.  # noqa: E501
        :type: str
        """
        if build is None:
            raise ValueError("Invalid value for `build`, must not be `None`")  # noqa: E501

        self._build = build

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
        if not isinstance(other, ApplianceFileUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other