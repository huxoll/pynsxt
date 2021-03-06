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


class UpgradePlanSettings(object):
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
        'pause_after_each_group': 'bool',
        'pause_on_error': 'bool',
        'parallel': 'bool'
    }

    attribute_map = {
        'pause_after_each_group': 'pause_after_each_group',
        'pause_on_error': 'pause_on_error',
        'parallel': 'parallel'
    }

    def __init__(self, pause_after_each_group=False, pause_on_error=False, parallel=True):  # noqa: E501
        """UpgradePlanSettings - a model defined in Swagger"""  # noqa: E501

        self._pause_after_each_group = None
        self._pause_on_error = None
        self._parallel = None
        self.discriminator = None

        if pause_after_each_group is not None:
            self.pause_after_each_group = pause_after_each_group
        if pause_on_error is not None:
            self.pause_on_error = pause_on_error
        if parallel is not None:
            self.parallel = parallel

    @property
    def pause_after_each_group(self):
        """Gets the pause_after_each_group of this UpgradePlanSettings.  # noqa: E501

        Flag to indicate whether to pause the upgrade after upgrade of each group is completed  # noqa: E501

        :return: The pause_after_each_group of this UpgradePlanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._pause_after_each_group

    @pause_after_each_group.setter
    def pause_after_each_group(self, pause_after_each_group):
        """Sets the pause_after_each_group of this UpgradePlanSettings.

        Flag to indicate whether to pause the upgrade after upgrade of each group is completed  # noqa: E501

        :param pause_after_each_group: The pause_after_each_group of this UpgradePlanSettings.  # noqa: E501
        :type: bool
        """

        self._pause_after_each_group = pause_after_each_group

    @property
    def pause_on_error(self):
        """Gets the pause_on_error of this UpgradePlanSettings.  # noqa: E501

        Flag to indicate whether to pause the upgrade plan execution when an error occurs  # noqa: E501

        :return: The pause_on_error of this UpgradePlanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._pause_on_error

    @pause_on_error.setter
    def pause_on_error(self, pause_on_error):
        """Sets the pause_on_error of this UpgradePlanSettings.

        Flag to indicate whether to pause the upgrade plan execution when an error occurs  # noqa: E501

        :param pause_on_error: The pause_on_error of this UpgradePlanSettings.  # noqa: E501
        :type: bool
        """

        self._pause_on_error = pause_on_error

    @property
    def parallel(self):
        """Gets the parallel of this UpgradePlanSettings.  # noqa: E501

        Upgrade Method to specify whether the upgrade is to be performed serially or in parallel  # noqa: E501

        :return: The parallel of this UpgradePlanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this UpgradePlanSettings.

        Upgrade Method to specify whether the upgrade is to be performed serially or in parallel  # noqa: E501

        :param parallel: The parallel of this UpgradePlanSettings.  # noqa: E501
        :type: bool
        """

        self._parallel = parallel

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
        if not isinstance(other, UpgradePlanSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
