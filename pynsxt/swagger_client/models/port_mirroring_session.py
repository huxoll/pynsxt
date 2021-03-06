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
from swagger_client.models.mirror_destination import MirrorDestination  # noqa: F401,E501
from swagger_client.models.mirror_source import MirrorSource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class PortMirroringSession(object):
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
        'direction': 'str',
        'encapsulation_vlan_id': 'int',
        'snap_length': 'int',
        'mirror_sources': 'list[MirrorSource]',
        'preserve_original_vlan': 'bool',
        'mirror_destination': 'MirrorDestination'
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
        'direction': 'direction',
        'encapsulation_vlan_id': 'encapsulation_vlan_id',
        'snap_length': 'snap_length',
        'mirror_sources': 'mirror_sources',
        'preserve_original_vlan': 'preserve_original_vlan',
        'mirror_destination': 'mirror_destination'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, direction=None, encapsulation_vlan_id=None, snap_length=None, mirror_sources=None, preserve_original_vlan=False, mirror_destination=None):  # noqa: E501
        """PortMirroringSession - a model defined in Swagger"""  # noqa: E501

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
        self._direction = None
        self._encapsulation_vlan_id = None
        self._snap_length = None
        self._mirror_sources = None
        self._preserve_original_vlan = None
        self._mirror_destination = None
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
        self.direction = direction
        if encapsulation_vlan_id is not None:
            self.encapsulation_vlan_id = encapsulation_vlan_id
        if snap_length is not None:
            self.snap_length = snap_length
        self.mirror_sources = mirror_sources
        if preserve_original_vlan is not None:
            self.preserve_original_vlan = preserve_original_vlan
        self.mirror_destination = mirror_destination

    @property
    def _self(self):
        """Gets the _self of this PortMirroringSession.  # noqa: E501


        :return: The _self of this PortMirroringSession.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this PortMirroringSession.


        :param _self: The _self of this PortMirroringSession.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this PortMirroringSession.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this PortMirroringSession.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortMirroringSession.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this PortMirroringSession.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this PortMirroringSession.  # noqa: E501


        :return: The schema of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this PortMirroringSession.


        :param schema: The schema of this PortMirroringSession.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this PortMirroringSession.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this PortMirroringSession.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PortMirroringSession.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this PortMirroringSession.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def system_owned(self):
        """Gets the system_owned of this PortMirroringSession.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this PortMirroringSession.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this PortMirroringSession.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this PortMirroringSession.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this PortMirroringSession.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PortMirroringSession.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this PortMirroringSession.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PortMirroringSession.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortMirroringSession.

        Description of this resource  # noqa: E501

        :param description: The description of this PortMirroringSession.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this PortMirroringSession.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this PortMirroringSession.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PortMirroringSession.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this PortMirroringSession.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this PortMirroringSession.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this PortMirroringSession.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this PortMirroringSession.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this PortMirroringSession.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this PortMirroringSession.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this PortMirroringSession.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this PortMirroringSession.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this PortMirroringSession.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PortMirroringSession.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this PortMirroringSession.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this PortMirroringSession.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this PortMirroringSession.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this PortMirroringSession.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this PortMirroringSession.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this PortMirroringSession.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this PortMirroringSession.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this PortMirroringSession.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this PortMirroringSession.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortMirroringSession.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this PortMirroringSession.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this PortMirroringSession.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PortMirroringSession.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this PortMirroringSession.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def direction(self):
        """Gets the direction of this PortMirroringSession.  # noqa: E501

        Port mirroring session direction  # noqa: E501

        :return: The direction of this PortMirroringSession.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this PortMirroringSession.

        Port mirroring session direction  # noqa: E501

        :param direction: The direction of this PortMirroringSession.  # noqa: E501
        :type: str
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501
        allowed_values = ["INGRESS", "EGRESS", "BIDIRECTIONAL"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def encapsulation_vlan_id(self):
        """Gets the encapsulation_vlan_id of this PortMirroringSession.  # noqa: E501

        Only for Remote SPAN Port Mirror.  # noqa: E501

        :return: The encapsulation_vlan_id of this PortMirroringSession.  # noqa: E501
        :rtype: int
        """
        return self._encapsulation_vlan_id

    @encapsulation_vlan_id.setter
    def encapsulation_vlan_id(self, encapsulation_vlan_id):
        """Sets the encapsulation_vlan_id of this PortMirroringSession.

        Only for Remote SPAN Port Mirror.  # noqa: E501

        :param encapsulation_vlan_id: The encapsulation_vlan_id of this PortMirroringSession.  # noqa: E501
        :type: int
        """

        self._encapsulation_vlan_id = encapsulation_vlan_id

    @property
    def snap_length(self):
        """Gets the snap_length of this PortMirroringSession.  # noqa: E501

        If this property is unset, entire package will be mirrored  # noqa: E501

        :return: The snap_length of this PortMirroringSession.  # noqa: E501
        :rtype: int
        """
        return self._snap_length

    @snap_length.setter
    def snap_length(self, snap_length):
        """Sets the snap_length of this PortMirroringSession.

        If this property is unset, entire package will be mirrored  # noqa: E501

        :param snap_length: The snap_length of this PortMirroringSession.  # noqa: E501
        :type: int
        """
        if snap_length is not None and snap_length > 65535:  # noqa: E501
            raise ValueError("Invalid value for `snap_length`, must be a value less than or equal to `65535`")  # noqa: E501
        if snap_length is not None and snap_length < 60:  # noqa: E501
            raise ValueError("Invalid value for `snap_length`, must be a value greater than or equal to `60`")  # noqa: E501

        self._snap_length = snap_length

    @property
    def mirror_sources(self):
        """Gets the mirror_sources of this PortMirroringSession.  # noqa: E501

        Mirror sources  # noqa: E501

        :return: The mirror_sources of this PortMirroringSession.  # noqa: E501
        :rtype: list[MirrorSource]
        """
        return self._mirror_sources

    @mirror_sources.setter
    def mirror_sources(self, mirror_sources):
        """Sets the mirror_sources of this PortMirroringSession.

        Mirror sources  # noqa: E501

        :param mirror_sources: The mirror_sources of this PortMirroringSession.  # noqa: E501
        :type: list[MirrorSource]
        """
        if mirror_sources is None:
            raise ValueError("Invalid value for `mirror_sources`, must not be `None`")  # noqa: E501

        self._mirror_sources = mirror_sources

    @property
    def preserve_original_vlan(self):
        """Gets the preserve_original_vlan of this PortMirroringSession.  # noqa: E501

        Only for Remote SPAN Port Mirror. Whether to preserve original VLAN.  # noqa: E501

        :return: The preserve_original_vlan of this PortMirroringSession.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_original_vlan

    @preserve_original_vlan.setter
    def preserve_original_vlan(self, preserve_original_vlan):
        """Sets the preserve_original_vlan of this PortMirroringSession.

        Only for Remote SPAN Port Mirror. Whether to preserve original VLAN.  # noqa: E501

        :param preserve_original_vlan: The preserve_original_vlan of this PortMirroringSession.  # noqa: E501
        :type: bool
        """

        self._preserve_original_vlan = preserve_original_vlan

    @property
    def mirror_destination(self):
        """Gets the mirror_destination of this PortMirroringSession.  # noqa: E501

        Mirror destination  # noqa: E501

        :return: The mirror_destination of this PortMirroringSession.  # noqa: E501
        :rtype: MirrorDestination
        """
        return self._mirror_destination

    @mirror_destination.setter
    def mirror_destination(self, mirror_destination):
        """Sets the mirror_destination of this PortMirroringSession.

        Mirror destination  # noqa: E501

        :param mirror_destination: The mirror_destination of this PortMirroringSession.  # noqa: E501
        :type: MirrorDestination
        """
        if mirror_destination is None:
            raise ValueError("Invalid value for `mirror_destination`, must not be `None`")  # noqa: E501

        self._mirror_destination = mirror_destination

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
        if not isinstance(other, PortMirroringSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
