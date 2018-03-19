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

from swagger_client.models.lb_pool_member_status import LbPoolMemberStatus  # noqa: F401,E501


class LbPoolStatus(object):
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
        'status': 'str',
        'last_update_timestamp': 'int',
        'pool_id': 'str',
        'members': 'list[LbPoolMemberStatus]'
    }

    attribute_map = {
        'status': 'status',
        'last_update_timestamp': 'last_update_timestamp',
        'pool_id': 'pool_id',
        'members': 'members'
    }

    def __init__(self, status=None, last_update_timestamp=None, pool_id=None, members=None):  # noqa: E501
        """LbPoolStatus - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._last_update_timestamp = None
        self._pool_id = None
        self._members = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        self.pool_id = pool_id
        if members is not None:
            self.members = members

    @property
    def status(self):
        """Gets the status of this LbPoolStatus.  # noqa: E501

        UP means that all primary members are in UP status. PARTIALLY_UP means that some(not all) primary members are in UP status, the number of these active members is larger or equal to certain number(min_active_members) which is defined in LbPool. PRIMARY_DOWN means that less than certain(min_active_members) primary members are in UP status but backup members are in UP status, connections to this pool would be dispatched to backup members. DOWN means that all primary and backup members are DOWN. DETACHED means that the pool is not bound to any virtual server.   # noqa: E501

        :return: The status of this LbPoolStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LbPoolStatus.

        UP means that all primary members are in UP status. PARTIALLY_UP means that some(not all) primary members are in UP status, the number of these active members is larger or equal to certain number(min_active_members) which is defined in LbPool. PRIMARY_DOWN means that less than certain(min_active_members) primary members are in UP status but backup members are in UP status, connections to this pool would be dispatched to backup members. DOWN means that all primary and backup members are DOWN. DETACHED means that the pool is not bound to any virtual server.   # noqa: E501

        :param status: The status of this LbPoolStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "PARTIALLY_UP", "PRIMARY_DOWN", "DOWN", "DETACHED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this LbPoolStatus.  # noqa: E501

        Timestamp when the data was last updated  # noqa: E501

        :return: The last_update_timestamp of this LbPoolStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this LbPoolStatus.

        Timestamp when the data was last updated  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this LbPoolStatus.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def pool_id(self):
        """Gets the pool_id of this LbPoolStatus.  # noqa: E501

        Load balancer pool identifier  # noqa: E501

        :return: The pool_id of this LbPoolStatus.  # noqa: E501
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this LbPoolStatus.

        Load balancer pool identifier  # noqa: E501

        :param pool_id: The pool_id of this LbPoolStatus.  # noqa: E501
        :type: str
        """
        if pool_id is None:
            raise ValueError("Invalid value for `pool_id`, must not be `None`")  # noqa: E501

        self._pool_id = pool_id

    @property
    def members(self):
        """Gets the members of this LbPoolStatus.  # noqa: E501

        Status of load balancer pool members  # noqa: E501

        :return: The members of this LbPoolStatus.  # noqa: E501
        :rtype: list[LbPoolMemberStatus]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this LbPoolStatus.

        Status of load balancer pool members  # noqa: E501

        :param members: The members of this LbPoolStatus.  # noqa: E501
        :type: list[LbPoolMemberStatus]
        """

        self._members = members

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
        if not isinstance(other, LbPoolStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other