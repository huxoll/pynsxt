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

from swagger_client.models.ns_group_expression import NSGroupExpression  # noqa: F401,E501


class NSGroupTagExpression(object):
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
        'tag_op': 'str',
        'scope': 'str',
        'scope_op': 'str',
        'tag': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'tag_op': 'tag_op',
        'scope': 'scope',
        'scope_op': 'scope_op',
        'tag': 'tag',
        'target_type': 'target_type'
    }

    def __init__(self, tag_op='EQUALS', scope=None, scope_op='EQUALS', tag=None, target_type=None):  # noqa: E501
        """NSGroupTagExpression - a model defined in Swagger"""  # noqa: E501

        self._tag_op = None
        self._scope = None
        self._scope_op = None
        self._tag = None
        self._target_type = None
        self.discriminator = None

        if tag_op is not None:
            self.tag_op = tag_op
        if scope is not None:
            self.scope = scope
        if scope_op is not None:
            self.scope_op = scope_op
        if tag is not None:
            self.tag = tag
        self.target_type = target_type

    @property
    def tag_op(self):
        """Gets the tag_op of this NSGroupTagExpression.  # noqa: E501

        Operator of the tag expression eg- tag.tag = \"Production\"  # noqa: E501

        :return: The tag_op of this NSGroupTagExpression.  # noqa: E501
        :rtype: str
        """
        return self._tag_op

    @tag_op.setter
    def tag_op(self, tag_op):
        """Sets the tag_op of this NSGroupTagExpression.

        Operator of the tag expression eg- tag.tag = \"Production\"  # noqa: E501

        :param tag_op: The tag_op of this NSGroupTagExpression.  # noqa: E501
        :type: str
        """
        allowed_values = ["EQUALS"]  # noqa: E501
        if tag_op not in allowed_values:
            raise ValueError(
                "Invalid value for `tag_op` ({0}), must be one of {1}"  # noqa: E501
                .format(tag_op, allowed_values)
            )

        self._tag_op = tag_op

    @property
    def scope(self):
        """Gets the scope of this NSGroupTagExpression.  # noqa: E501

        The tag.scope attribute of the object  # noqa: E501

        :return: The scope of this NSGroupTagExpression.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this NSGroupTagExpression.

        The tag.scope attribute of the object  # noqa: E501

        :param scope: The scope of this NSGroupTagExpression.  # noqa: E501
        :type: str
        """
        if scope is not None and len(scope) > 20:
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `20`")  # noqa: E501

        self._scope = scope

    @property
    def scope_op(self):
        """Gets the scope_op of this NSGroupTagExpression.  # noqa: E501

        Operator of the scope expression eg- tag.scope = \"S1\".  # noqa: E501

        :return: The scope_op of this NSGroupTagExpression.  # noqa: E501
        :rtype: str
        """
        return self._scope_op

    @scope_op.setter
    def scope_op(self, scope_op):
        """Sets the scope_op of this NSGroupTagExpression.

        Operator of the scope expression eg- tag.scope = \"S1\".  # noqa: E501

        :param scope_op: The scope_op of this NSGroupTagExpression.  # noqa: E501
        :type: str
        """
        allowed_values = ["EQUALS"]  # noqa: E501
        if scope_op not in allowed_values:
            raise ValueError(
                "Invalid value for `scope_op` ({0}), must be one of {1}"  # noqa: E501
                .format(scope_op, allowed_values)
            )

        self._scope_op = scope_op

    @property
    def tag(self):
        """Gets the tag of this NSGroupTagExpression.  # noqa: E501

        The tag.tag attribute of the object  # noqa: E501

        :return: The tag of this NSGroupTagExpression.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NSGroupTagExpression.

        The tag.tag attribute of the object  # noqa: E501

        :param tag: The tag of this NSGroupTagExpression.  # noqa: E501
        :type: str
        """
        if tag is not None and len(tag) > 40:
            raise ValueError("Invalid value for `tag`, length must be less than or equal to `40`")  # noqa: E501

        self._tag = tag

    @property
    def target_type(self):
        """Gets the target_type of this NSGroupTagExpression.  # noqa: E501

        Type of the resource on which this expression is evaluated  # noqa: E501

        :return: The target_type of this NSGroupTagExpression.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this NSGroupTagExpression.

        Type of the resource on which this expression is evaluated  # noqa: E501

        :param target_type: The target_type of this NSGroupTagExpression.  # noqa: E501
        :type: str
        """
        if target_type is None:
            raise ValueError("Invalid value for `target_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LogicalSwitch", "LogicalPort", "VirtualMachine"]  # noqa: E501
        if target_type not in allowed_values:
            raise ValueError(
                "Invalid value for `target_type` ({0}), must be one of {1}"  # noqa: E501
                .format(target_type, allowed_values)
            )

        self._target_type = target_type

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
        if not isinstance(other, NSGroupTagExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other