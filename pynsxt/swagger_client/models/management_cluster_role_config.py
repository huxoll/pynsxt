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

from swagger_client.models.cluster_role_config import ClusterRoleConfig  # noqa: F401,E501
from swagger_client.models.msg_client_info import MsgClientInfo  # noqa: F401,E501
from swagger_client.models.service_endpoint import ServiceEndpoint  # noqa: F401,E501


class ManagementClusterRoleConfig(object):
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
        'type': 'str',
        'mgmt_cluster_listen_addr': 'ServiceEndpoint',
        'mpa_msg_client_info': 'MsgClientInfo',
        'api_listen_addr': 'ServiceEndpoint',
        'mgmt_plane_listen_addr': 'ServiceEndpoint'
    }

    attribute_map = {
        'type': 'type',
        'mgmt_cluster_listen_addr': 'mgmt_cluster_listen_addr',
        'mpa_msg_client_info': 'mpa_msg_client_info',
        'api_listen_addr': 'api_listen_addr',
        'mgmt_plane_listen_addr': 'mgmt_plane_listen_addr'
    }

    def __init__(self, type=None, mgmt_cluster_listen_addr=None, mpa_msg_client_info=None, api_listen_addr=None, mgmt_plane_listen_addr=None):  # noqa: E501
        """ManagementClusterRoleConfig - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._mgmt_cluster_listen_addr = None
        self._mpa_msg_client_info = None
        self._api_listen_addr = None
        self._mgmt_plane_listen_addr = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if mgmt_cluster_listen_addr is not None:
            self.mgmt_cluster_listen_addr = mgmt_cluster_listen_addr
        if mpa_msg_client_info is not None:
            self.mpa_msg_client_info = mpa_msg_client_info
        if api_listen_addr is not None:
            self.api_listen_addr = api_listen_addr
        if mgmt_plane_listen_addr is not None:
            self.mgmt_plane_listen_addr = mgmt_plane_listen_addr

    @property
    def type(self):
        """Gets the type of this ManagementClusterRoleConfig.  # noqa: E501

        Type of this role configuration  # noqa: E501

        :return: The type of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ManagementClusterRoleConfig.

        Type of this role configuration  # noqa: E501

        :param type: The type of this ManagementClusterRoleConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["ManagementClusterRoleConfig", "ControllerClusterRoleConfig"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def mgmt_cluster_listen_addr(self):
        """Gets the mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501

        The IP and port for the management cluster service on this node  # noqa: E501

        :return: The mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return self._mgmt_cluster_listen_addr

    @mgmt_cluster_listen_addr.setter
    def mgmt_cluster_listen_addr(self, mgmt_cluster_listen_addr):
        """Sets the mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.

        The IP and port for the management cluster service on this node  # noqa: E501

        :param mgmt_cluster_listen_addr: The mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :type: ServiceEndpoint
        """

        self._mgmt_cluster_listen_addr = mgmt_cluster_listen_addr

    @property
    def mpa_msg_client_info(self):
        """Gets the mpa_msg_client_info of this ManagementClusterRoleConfig.  # noqa: E501


        :return: The mpa_msg_client_info of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: MsgClientInfo
        """
        return self._mpa_msg_client_info

    @mpa_msg_client_info.setter
    def mpa_msg_client_info(self, mpa_msg_client_info):
        """Sets the mpa_msg_client_info of this ManagementClusterRoleConfig.


        :param mpa_msg_client_info: The mpa_msg_client_info of this ManagementClusterRoleConfig.  # noqa: E501
        :type: MsgClientInfo
        """

        self._mpa_msg_client_info = mpa_msg_client_info

    @property
    def api_listen_addr(self):
        """Gets the api_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501

        The IP and port for the public API service on this node  # noqa: E501

        :return: The api_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return self._api_listen_addr

    @api_listen_addr.setter
    def api_listen_addr(self, api_listen_addr):
        """Sets the api_listen_addr of this ManagementClusterRoleConfig.

        The IP and port for the public API service on this node  # noqa: E501

        :param api_listen_addr: The api_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :type: ServiceEndpoint
        """

        self._api_listen_addr = api_listen_addr

    @property
    def mgmt_plane_listen_addr(self):
        """Gets the mgmt_plane_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501

        The IP and port for the management plane service on this node  # noqa: E501

        :return: The mgmt_plane_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return self._mgmt_plane_listen_addr

    @mgmt_plane_listen_addr.setter
    def mgmt_plane_listen_addr(self, mgmt_plane_listen_addr):
        """Sets the mgmt_plane_listen_addr of this ManagementClusterRoleConfig.

        The IP and port for the management plane service on this node  # noqa: E501

        :param mgmt_plane_listen_addr: The mgmt_plane_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :type: ServiceEndpoint
        """

        self._mgmt_plane_listen_addr = mgmt_plane_listen_addr

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
        if not isinstance(other, ManagementClusterRoleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
