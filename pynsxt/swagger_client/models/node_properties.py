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

from swagger_client.models.resource import Resource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class NodeProperties(object):
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
        '_self': 'SelfResourceLink',
        'links': 'list[ResourceLink]',
        'schema': 'str',
        'kernel_version': 'str',
        'system_time': 'int',
        'node_uuid': 'str',
        'cli_timeout': 'int',
        'bios_uuid': 'str',
        'timezone': 'str',
        'hostname': 'str',
        'node_version': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'kernel_version': 'kernel_version',
        'system_time': 'system_time',
        'node_uuid': 'node_uuid',
        'cli_timeout': 'cli_timeout',
        'bios_uuid': 'bios_uuid',
        'timezone': 'timezone',
        'hostname': 'hostname',
        'node_version': 'node_version'
    }

    def __init__(self, _self=None, links=None, schema=None, kernel_version=None, system_time=None, node_uuid=None, cli_timeout=None, bios_uuid=None, timezone=None, hostname=None, node_version=None):  # noqa: E501
        """NodeProperties - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._kernel_version = None
        self._system_time = None
        self._node_uuid = None
        self._cli_timeout = None
        self._bios_uuid = None
        self._timezone = None
        self._hostname = None
        self._node_version = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if system_time is not None:
            self.system_time = system_time
        if node_uuid is not None:
            self.node_uuid = node_uuid
        if cli_timeout is not None:
            self.cli_timeout = cli_timeout
        if bios_uuid is not None:
            self.bios_uuid = bios_uuid
        if timezone is not None:
            self.timezone = timezone
        if hostname is not None:
            self.hostname = hostname
        if node_version is not None:
            self.node_version = node_version

    @property
    def _self(self):
        """Gets the _self of this NodeProperties.  # noqa: E501


        :return: The _self of this NodeProperties.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this NodeProperties.


        :param _self: The _self of this NodeProperties.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this NodeProperties.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this NodeProperties.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NodeProperties.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this NodeProperties.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this NodeProperties.  # noqa: E501


        :return: The schema of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this NodeProperties.


        :param schema: The schema of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def kernel_version(self):
        """Gets the kernel_version of this NodeProperties.  # noqa: E501

        Kernel version  # noqa: E501

        :return: The kernel_version of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this NodeProperties.

        Kernel version  # noqa: E501

        :param kernel_version: The kernel_version of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._kernel_version = kernel_version

    @property
    def system_time(self):
        """Gets the system_time of this NodeProperties.  # noqa: E501

        Current time expressed in milliseconds since epoch  # noqa: E501

        :return: The system_time of this NodeProperties.  # noqa: E501
        :rtype: int
        """
        return self._system_time

    @system_time.setter
    def system_time(self, system_time):
        """Sets the system_time of this NodeProperties.

        Current time expressed in milliseconds since epoch  # noqa: E501

        :param system_time: The system_time of this NodeProperties.  # noqa: E501
        :type: int
        """

        self._system_time = system_time

    @property
    def node_uuid(self):
        """Gets the node_uuid of this NodeProperties.  # noqa: E501

        Node Unique Identifier  # noqa: E501

        :return: The node_uuid of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._node_uuid

    @node_uuid.setter
    def node_uuid(self, node_uuid):
        """Sets the node_uuid of this NodeProperties.

        Node Unique Identifier  # noqa: E501

        :param node_uuid: The node_uuid of this NodeProperties.  # noqa: E501
        :type: str
        """
        if node_uuid is not None and len(node_uuid) > 36:
            raise ValueError("Invalid value for `node_uuid`, length must be less than or equal to `36`")  # noqa: E501

        self._node_uuid = node_uuid

    @property
    def cli_timeout(self):
        """Gets the cli_timeout of this NodeProperties.  # noqa: E501

        NSX CLI inactivity timeout, set to 0 to configure no timeout  # noqa: E501

        :return: The cli_timeout of this NodeProperties.  # noqa: E501
        :rtype: int
        """
        return self._cli_timeout

    @cli_timeout.setter
    def cli_timeout(self, cli_timeout):
        """Sets the cli_timeout of this NodeProperties.

        NSX CLI inactivity timeout, set to 0 to configure no timeout  # noqa: E501

        :param cli_timeout: The cli_timeout of this NodeProperties.  # noqa: E501
        :type: int
        """
        if cli_timeout is not None and cli_timeout < 0:  # noqa: E501
            raise ValueError("Invalid value for `cli_timeout`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cli_timeout = cli_timeout

    @property
    def bios_uuid(self):
        """Gets the bios_uuid of this NodeProperties.  # noqa: E501

        Node BIOS Unique Indentifier  # noqa: E501

        :return: The bios_uuid of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._bios_uuid

    @bios_uuid.setter
    def bios_uuid(self, bios_uuid):
        """Sets the bios_uuid of this NodeProperties.

        Node BIOS Unique Indentifier  # noqa: E501

        :param bios_uuid: The bios_uuid of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._bios_uuid = bios_uuid

    @property
    def timezone(self):
        """Gets the timezone of this NodeProperties.  # noqa: E501

        Timezone  # noqa: E501

        :return: The timezone of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this NodeProperties.

        Timezone  # noqa: E501

        :param timezone: The timezone of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def hostname(self):
        """Gets the hostname of this NodeProperties.  # noqa: E501

        Host name or fully qualified domain name of node  # noqa: E501

        :return: The hostname of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NodeProperties.

        Host name or fully qualified domain name of node  # noqa: E501

        :param hostname: The hostname of this NodeProperties.  # noqa: E501
        :type: str
        """
        if hostname is not None and not re.search('^(?=.{1,255}$)[0-9A-Za-z](?:(?:[0-9A-Za-z]|-){0,61}[0-9A-Za-z])?(?:\\.[0-9A-Za-z](?:(?:[0-9A-Za-z]|-){0,61}[0-9A-Za-z])?)*\\.?$', hostname):  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must be a follow pattern or equal to `/^(?=.{1,255}$)[0-9A-Za-z](?:(?:[0-9A-Za-z]|-){0,61}[0-9A-Za-z])?(?:\\.[0-9A-Za-z](?:(?:[0-9A-Za-z]|-){0,61}[0-9A-Za-z])?)*\\.?$/`")  # noqa: E501

        self._hostname = hostname

    @property
    def node_version(self):
        """Gets the node_version of this NodeProperties.  # noqa: E501

        Node version  # noqa: E501

        :return: The node_version of this NodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._node_version

    @node_version.setter
    def node_version(self, node_version):
        """Sets the node_version of this NodeProperties.

        Node version  # noqa: E501

        :param node_version: The node_version of this NodeProperties.  # noqa: E501
        :type: str
        """

        self._node_version = node_version

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
        if not isinstance(other, NodeProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
