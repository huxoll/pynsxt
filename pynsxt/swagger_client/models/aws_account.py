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

from swagger_client.models.aws_account_status import AwsAccountStatus  # noqa: F401,E501
from swagger_client.models.cloud_account import CloudAccount  # noqa: F401,E501
from swagger_client.models.cloud_user_info import CloudUserInfo  # noqa: F401,E501
from swagger_client.models.instance_stats import InstanceStats  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501
from swagger_client.models.vpc_stats import VpcStats  # noqa: F401,E501


class AwsAccount(object):
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
        'tenant_id': 'str',
        'instance_stats': 'InstanceStats',
        'cloud_type': 'str',
        'auth_users': 'list[CloudUserInfo]',
        'status': 'AwsAccountStatus',
        'access_key': 'str',
        'regions_count': 'int',
        'auth_mechanism_iam': 'bool',
        'gateway_role_name': 'str',
        'vpc_stats': 'VpcStats',
        'has_managed_vpc': 'str',
        'secret_key': 'str',
        'external_id': 'str',
        'iam_role_arn': 'str'
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
        'tenant_id': 'tenant_id',
        'instance_stats': 'instance_stats',
        'cloud_type': 'cloud_type',
        'auth_users': 'auth_users',
        'status': 'status',
        'access_key': 'access_key',
        'regions_count': 'regions_count',
        'auth_mechanism_iam': 'auth_mechanism_iam',
        'gateway_role_name': 'gateway_role_name',
        'vpc_stats': 'vpc_stats',
        'has_managed_vpc': 'has_managed_vpc',
        'secret_key': 'secret_key',
        'external_id': 'external_id',
        'iam_role_arn': 'iam_role_arn'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, tenant_id=None, instance_stats=None, cloud_type=None, auth_users=None, status=None, access_key=None, regions_count=None, auth_mechanism_iam=None, gateway_role_name=None, vpc_stats=None, has_managed_vpc=None, secret_key=None, external_id=None, iam_role_arn=None):  # noqa: E501
        """AwsAccount - a model defined in Swagger"""  # noqa: E501

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
        self._tenant_id = None
        self._instance_stats = None
        self._cloud_type = None
        self._auth_users = None
        self._status = None
        self._access_key = None
        self._regions_count = None
        self._auth_mechanism_iam = None
        self._gateway_role_name = None
        self._vpc_stats = None
        self._has_managed_vpc = None
        self._secret_key = None
        self._external_id = None
        self._iam_role_arn = None
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
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if instance_stats is not None:
            self.instance_stats = instance_stats
        self.cloud_type = cloud_type
        if auth_users is not None:
            self.auth_users = auth_users
        if status is not None:
            self.status = status
        if access_key is not None:
            self.access_key = access_key
        if regions_count is not None:
            self.regions_count = regions_count
        if auth_mechanism_iam is not None:
            self.auth_mechanism_iam = auth_mechanism_iam
        if gateway_role_name is not None:
            self.gateway_role_name = gateway_role_name
        if vpc_stats is not None:
            self.vpc_stats = vpc_stats
        if has_managed_vpc is not None:
            self.has_managed_vpc = has_managed_vpc
        if secret_key is not None:
            self.secret_key = secret_key
        if external_id is not None:
            self.external_id = external_id
        if iam_role_arn is not None:
            self.iam_role_arn = iam_role_arn

    @property
    def _self(self):
        """Gets the _self of this AwsAccount.  # noqa: E501


        :return: The _self of this AwsAccount.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this AwsAccount.


        :param _self: The _self of this AwsAccount.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this AwsAccount.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this AwsAccount.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AwsAccount.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this AwsAccount.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this AwsAccount.  # noqa: E501


        :return: The schema of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this AwsAccount.


        :param schema: The schema of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this AwsAccount.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this AwsAccount.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this AwsAccount.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this AwsAccount.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def system_owned(self):
        """Gets the system_owned of this AwsAccount.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this AwsAccount.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this AwsAccount.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this AwsAccount.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this AwsAccount.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AwsAccount.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this AwsAccount.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this AwsAccount.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AwsAccount.

        Description of this resource  # noqa: E501

        :param description: The description of this AwsAccount.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this AwsAccount.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this AwsAccount.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AwsAccount.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this AwsAccount.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this AwsAccount.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this AwsAccount.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this AwsAccount.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this AwsAccount.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this AwsAccount.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this AwsAccount.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AwsAccount.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this AwsAccount.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this AwsAccount.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this AwsAccount.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this AwsAccount.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this AwsAccount.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this AwsAccount.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this AwsAccount.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this AwsAccount.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwsAccount.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this AwsAccount.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AwsAccount.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AwsAccount.  # noqa: E501

        Tenant ID of the cloud account  # noqa: E501

        :return: The tenant_id of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AwsAccount.

        Tenant ID of the cloud account  # noqa: E501

        :param tenant_id: The tenant_id of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def instance_stats(self):
        """Gets the instance_stats of this AwsAccount.  # noqa: E501

        Instance statistics  # noqa: E501

        :return: The instance_stats of this AwsAccount.  # noqa: E501
        :rtype: InstanceStats
        """
        return self._instance_stats

    @instance_stats.setter
    def instance_stats(self, instance_stats):
        """Sets the instance_stats of this AwsAccount.

        Instance statistics  # noqa: E501

        :param instance_stats: The instance_stats of this AwsAccount.  # noqa: E501
        :type: InstanceStats
        """

        self._instance_stats = instance_stats

    @property
    def cloud_type(self):
        """Gets the cloud_type of this AwsAccount.  # noqa: E501

        Cloud Type  # noqa: E501

        :return: The cloud_type of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this AwsAccount.

        Cloud Type  # noqa: E501

        :param cloud_type: The cloud_type of this AwsAccount.  # noqa: E501
        :type: str
        """
        if cloud_type is None:
            raise ValueError("Invalid value for `cloud_type`, must not be `None`")  # noqa: E501
        allowed_values = ["AWS", "AZURE", "GOOGLE"]  # noqa: E501
        if cloud_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cloud_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud_type, allowed_values)
            )

        self._cloud_type = cloud_type

    @property
    def auth_users(self):
        """Gets the auth_users of this AwsAccount.  # noqa: E501

        List of authorized users  # noqa: E501

        :return: The auth_users of this AwsAccount.  # noqa: E501
        :rtype: list[CloudUserInfo]
        """
        return self._auth_users

    @auth_users.setter
    def auth_users(self, auth_users):
        """Sets the auth_users of this AwsAccount.

        List of authorized users  # noqa: E501

        :param auth_users: The auth_users of this AwsAccount.  # noqa: E501
        :type: list[CloudUserInfo]
        """

        self._auth_users = auth_users

    @property
    def status(self):
        """Gets the status of this AwsAccount.  # noqa: E501

        Status of the account  # noqa: E501

        :return: The status of this AwsAccount.  # noqa: E501
        :rtype: AwsAccountStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AwsAccount.

        Status of the account  # noqa: E501

        :param status: The status of this AwsAccount.  # noqa: E501
        :type: AwsAccountStatus
        """

        self._status = status

    @property
    def access_key(self):
        """Gets the access_key of this AwsAccount.  # noqa: E501

        Access key of cloud account  # noqa: E501

        :return: The access_key of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AwsAccount.

        Access key of cloud account  # noqa: E501

        :param access_key: The access_key of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def regions_count(self):
        """Gets the regions_count of this AwsAccount.  # noqa: E501

        Count of the regions available  # noqa: E501

        :return: The regions_count of this AwsAccount.  # noqa: E501
        :rtype: int
        """
        return self._regions_count

    @regions_count.setter
    def regions_count(self, regions_count):
        """Sets the regions_count of this AwsAccount.

        Count of the regions available  # noqa: E501

        :param regions_count: The regions_count of this AwsAccount.  # noqa: E501
        :type: int
        """

        self._regions_count = regions_count

    @property
    def auth_mechanism_iam(self):
        """Gets the auth_mechanism_iam of this AwsAccount.  # noqa: E501

        Is the AWS authorization mechanism based on Identity and Access Management(IAM) service?   # noqa: E501

        :return: The auth_mechanism_iam of this AwsAccount.  # noqa: E501
        :rtype: bool
        """
        return self._auth_mechanism_iam

    @auth_mechanism_iam.setter
    def auth_mechanism_iam(self, auth_mechanism_iam):
        """Sets the auth_mechanism_iam of this AwsAccount.

        Is the AWS authorization mechanism based on Identity and Access Management(IAM) service?   # noqa: E501

        :param auth_mechanism_iam: The auth_mechanism_iam of this AwsAccount.  # noqa: E501
        :type: bool
        """

        self._auth_mechanism_iam = auth_mechanism_iam

    @property
    def gateway_role_name(self):
        """Gets the gateway_role_name of this AwsAccount.  # noqa: E501

        Service Role Name for IAM role csm needs to assume  # noqa: E501

        :return: The gateway_role_name of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._gateway_role_name

    @gateway_role_name.setter
    def gateway_role_name(self, gateway_role_name):
        """Sets the gateway_role_name of this AwsAccount.

        Service Role Name for IAM role csm needs to assume  # noqa: E501

        :param gateway_role_name: The gateway_role_name of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._gateway_role_name = gateway_role_name

    @property
    def vpc_stats(self):
        """Gets the vpc_stats of this AwsAccount.  # noqa: E501

        VPC statistics  # noqa: E501

        :return: The vpc_stats of this AwsAccount.  # noqa: E501
        :rtype: VpcStats
        """
        return self._vpc_stats

    @vpc_stats.setter
    def vpc_stats(self, vpc_stats):
        """Sets the vpc_stats of this AwsAccount.

        VPC statistics  # noqa: E501

        :param vpc_stats: The vpc_stats of this AwsAccount.  # noqa: E501
        :type: VpcStats
        """

        self._vpc_stats = vpc_stats

    @property
    def has_managed_vpc(self):
        """Gets the has_managed_vpc of this AwsAccount.  # noqa: E501

        Has a managed VPC?  # noqa: E501

        :return: The has_managed_vpc of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._has_managed_vpc

    @has_managed_vpc.setter
    def has_managed_vpc(self, has_managed_vpc):
        """Sets the has_managed_vpc of this AwsAccount.

        Has a managed VPC?  # noqa: E501

        :param has_managed_vpc: The has_managed_vpc of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._has_managed_vpc = has_managed_vpc

    @property
    def secret_key(self):
        """Gets the secret_key of this AwsAccount.  # noqa: E501

        Secret key of cloud account  # noqa: E501

        :return: The secret_key of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AwsAccount.

        Secret key of cloud account  # noqa: E501

        :param secret_key: The secret_key of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def external_id(self):
        """Gets the external_id of this AwsAccount.  # noqa: E501

        External id for the IAM role csm needs to assume  # noqa: E501

        :return: The external_id of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AwsAccount.

        External id for the IAM role csm needs to assume  # noqa: E501

        :param external_id: The external_id of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def iam_role_arn(self):
        """Gets the iam_role_arn of this AwsAccount.  # noqa: E501

        Amazon Resource Names (ARNs) uniquely identify AWS resources. We will use it here to identify the IAM role csm needs to assume.   # noqa: E501

        :return: The iam_role_arn of this AwsAccount.  # noqa: E501
        :rtype: str
        """
        return self._iam_role_arn

    @iam_role_arn.setter
    def iam_role_arn(self, iam_role_arn):
        """Sets the iam_role_arn of this AwsAccount.

        Amazon Resource Names (ARNs) uniquely identify AWS resources. We will use it here to identify the IAM role csm needs to assume.   # noqa: E501

        :param iam_role_arn: The iam_role_arn of this AwsAccount.  # noqa: E501
        :type: str
        """

        self._iam_role_arn = iam_role_arn

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
        if not isinstance(other, AwsAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
