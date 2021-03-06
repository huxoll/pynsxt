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

from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class DneKeyManager(object):
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
        'revision': 'int',
        'system_owned': 'bool',
        'display_name': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'create_user': 'str',
        'protection': 'str',
        'create_time': 'int',
        'last_modified_time': 'int',
        'last_modified_user': 'str',
        'id': 'str',
        'resource_type': 'str',
        'status': 'str',
        'host': 'str',
        'port': 'int',
        'certificate': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'revision': '_revision',
        'system_owned': '_system_owned',
        'display_name': 'display_name',
        'description': 'description',
        'tags': 'tags',
        'create_user': '_create_user',
        'protection': '_protection',
        'create_time': '_create_time',
        'last_modified_time': '_last_modified_time',
        'last_modified_user': '_last_modified_user',
        'id': 'id',
        'resource_type': 'resource_type',
        'status': 'status',
        'host': 'host',
        'port': 'port',
        'certificate': 'certificate'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, status=None, host=None, port=None, certificate=None):  # noqa: E501
        """DneKeyManager - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._revision = None
        self._system_owned = None
        self._display_name = None
        self._description = None
        self._tags = None
        self._create_user = None
        self._protection = None
        self._create_time = None
        self._last_modified_time = None
        self._last_modified_user = None
        self._id = None
        self._resource_type = None
        self._status = None
        self._host = None
        self._port = None
        self._certificate = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if revision is not None:
            self.revision = revision
        if system_owned is not None:
            self.system_owned = system_owned
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_user is not None:
            self.create_user = create_user
        if protection is not None:
            self.protection = protection
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_modified_user is not None:
            self.last_modified_user = last_modified_user
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        self.host = host
        self.port = port
        self.certificate = certificate

    @property
    def _self(self):
        """Gets the _self of this DneKeyManager.  # noqa: E501


        :return: The _self of this DneKeyManager.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this DneKeyManager.


        :param _self: The _self of this DneKeyManager.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this DneKeyManager.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this DneKeyManager.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DneKeyManager.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this DneKeyManager.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this DneKeyManager.  # noqa: E501


        :return: The schema of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this DneKeyManager.


        :param schema: The schema of this DneKeyManager.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this DneKeyManager.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this DneKeyManager.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this DneKeyManager.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this DneKeyManager.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def system_owned(self):
        """Gets the system_owned of this DneKeyManager.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this DneKeyManager.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this DneKeyManager.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this DneKeyManager.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this DneKeyManager.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DneKeyManager.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this DneKeyManager.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this DneKeyManager.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DneKeyManager.

        Description of this resource  # noqa: E501

        :param description: The description of this DneKeyManager.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this DneKeyManager.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this DneKeyManager.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DneKeyManager.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this DneKeyManager.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this DneKeyManager.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this DneKeyManager.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this DneKeyManager.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this DneKeyManager.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this DneKeyManager.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this DneKeyManager.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this DneKeyManager.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this DneKeyManager.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DneKeyManager.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this DneKeyManager.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this DneKeyManager.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this DneKeyManager.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this DneKeyManager.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this DneKeyManager.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this DneKeyManager.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this DneKeyManager.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this DneKeyManager.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this DneKeyManager.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DneKeyManager.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this DneKeyManager.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this DneKeyManager.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DneKeyManager.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this DneKeyManager.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this DneKeyManager.  # noqa: E501

        Health status check for the key manager server. The value is updated and displayed everytime an API call(GET/POST/PUT) is made on the key manager entity.  # noqa: E501

        :return: The status of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DneKeyManager.

        Health status check for the key manager server. The value is updated and displayed everytime an API call(GET/POST/PUT) is made on the key manager entity.  # noqa: E501

        :param status: The status of this DneKeyManager.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def host(self):
        """Gets the host of this DneKeyManager.  # noqa: E501

        Host server of key manager appliance. The value could be an IP address or a server name.  # noqa: E501

        :return: The host of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DneKeyManager.

        Host server of key manager appliance. The value could be an IP address or a server name.  # noqa: E501

        :param host: The host of this DneKeyManager.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this DneKeyManager.  # noqa: E501

        A port number of key manager instance.  # noqa: E501

        :return: The port of this DneKeyManager.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DneKeyManager.

        A port number of key manager instance.  # noqa: E501

        :param port: The port of this DneKeyManager.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 0:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port = port

    @property
    def certificate(self):
        """Gets the certificate of this DneKeyManager.  # noqa: E501

        The certificate of key manager appliance.  # noqa: E501

        :return: The certificate of this DneKeyManager.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this DneKeyManager.

        The certificate of key manager appliance.  # noqa: E501

        :param certificate: The certificate of this DneKeyManager.  # noqa: E501
        :type: str
        """
        if certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")  # noqa: E501

        self._certificate = certificate

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
        if not isinstance(other, DneKeyManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
