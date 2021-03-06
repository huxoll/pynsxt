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

from swagger_client.models.aggregate_request import AggregateRequest  # noqa: F401,E501
from swagger_client.models.filter_request import FilterRequest  # noqa: F401,E501


class RelatedDataRequest(object):
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
        'included_fields': 'str',
        'alias': 'str',
        'filters': 'list[FilterRequest]',
        'resource_type': 'str',
        'join_condition': 'str',
        'size': 'int'
    }

    attribute_map = {
        'included_fields': 'included_fields',
        'alias': 'alias',
        'filters': 'filters',
        'resource_type': 'resource_type',
        'join_condition': 'join_condition',
        'size': 'size'
    }

    def __init__(self, included_fields=None, alias=None, filters=None, resource_type=None, join_condition=None, size=None):  # noqa: E501
        """RelatedDataRequest - a model defined in Swagger"""  # noqa: E501

        self._included_fields = None
        self._alias = None
        self._filters = None
        self._resource_type = None
        self._join_condition = None
        self._size = None
        self.discriminator = None

        if included_fields is not None:
            self.included_fields = included_fields
        if alias is not None:
            self.alias = alias
        if filters is not None:
            self.filters = filters
        self.resource_type = resource_type
        self.join_condition = join_condition
        if size is not None:
            self.size = size

    @property
    def included_fields(self):
        """Gets the included_fields of this RelatedDataRequest.  # noqa: E501

        Comma separated list of fields that should be included to result of query  # noqa: E501

        :return: The included_fields of this RelatedDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._included_fields

    @included_fields.setter
    def included_fields(self, included_fields):
        """Sets the included_fields of this RelatedDataRequest.

        Comma separated list of fields that should be included to result of query  # noqa: E501

        :param included_fields: The included_fields of this RelatedDataRequest.  # noqa: E501
        :type: str
        """

        self._included_fields = included_fields

    @property
    def alias(self):
        """Gets the alias of this RelatedDataRequest.  # noqa: E501

        Alias for the response  # noqa: E501

        :return: The alias of this RelatedDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this RelatedDataRequest.

        Alias for the response  # noqa: E501

        :param alias: The alias of this RelatedDataRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def filters(self):
        """Gets the filters of this RelatedDataRequest.  # noqa: E501

        An array of filter conditions  # noqa: E501

        :return: The filters of this RelatedDataRequest.  # noqa: E501
        :rtype: list[FilterRequest]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this RelatedDataRequest.

        An array of filter conditions  # noqa: E501

        :param filters: The filters of this RelatedDataRequest.  # noqa: E501
        :type: list[FilterRequest]
        """

        self._filters = filters

    @property
    def resource_type(self):
        """Gets the resource_type of this RelatedDataRequest.  # noqa: E501

        Resource type name  # noqa: E501

        :return: The resource_type of this RelatedDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RelatedDataRequest.

        Resource type name  # noqa: E501

        :param resource_type: The resource_type of this RelatedDataRequest.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def join_condition(self):
        """Gets the join_condition of this RelatedDataRequest.  # noqa: E501

        Join condition between the parent and the related object. This is to be specified in \"relatedObjectFieldName:ParentObjectFieldName\" format.   # noqa: E501

        :return: The join_condition of this RelatedDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._join_condition

    @join_condition.setter
    def join_condition(self, join_condition):
        """Sets the join_condition of this RelatedDataRequest.

        Join condition between the parent and the related object. This is to be specified in \"relatedObjectFieldName:ParentObjectFieldName\" format.   # noqa: E501

        :param join_condition: The join_condition of this RelatedDataRequest.  # noqa: E501
        :type: str
        """
        if join_condition is None:
            raise ValueError("Invalid value for `join_condition`, must not be `None`")  # noqa: E501

        self._join_condition = join_condition

    @property
    def size(self):
        """Gets the size of this RelatedDataRequest.  # noqa: E501

        Number of related objects to return. If not specified all the related objects will be returned. Should be set to 0 if only the count of related objects is desired.   # noqa: E501

        :return: The size of this RelatedDataRequest.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RelatedDataRequest.

        Number of related objects to return. If not specified all the related objects will be returned. Should be set to 0 if only the count of related objects is desired.   # noqa: E501

        :param size: The size of this RelatedDataRequest.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, RelatedDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
