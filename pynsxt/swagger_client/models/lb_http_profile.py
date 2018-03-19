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

from swagger_client.models.lb_app_profile import LbAppProfile  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class LbHttpProfile(object):
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
        'idle_timeout': 'int',
        'ntlm': 'bool',
        'request_header_size': 'int',
        'http_redirect_to_https': 'bool',
        'x_forwarded_for': 'str',
        'http_redirect_to': 'str'
    }

    attribute_map = {
        'idle_timeout': 'idle_timeout',
        'ntlm': 'ntlm',
        'request_header_size': 'request_header_size',
        'http_redirect_to_https': 'http_redirect_to_https',
        'x_forwarded_for': 'x_forwarded_for',
        'http_redirect_to': 'http_redirect_to'
    }

    def __init__(self, idle_timeout=15, ntlm=False, request_header_size=1024, http_redirect_to_https=False, x_forwarded_for=None, http_redirect_to=None):  # noqa: E501
        """LbHttpProfile - a model defined in Swagger"""  # noqa: E501

        self._idle_timeout = None
        self._ntlm = None
        self._request_header_size = None
        self._http_redirect_to_https = None
        self._x_forwarded_for = None
        self._http_redirect_to = None
        self.discriminator = None

        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if ntlm is not None:
            self.ntlm = ntlm
        if request_header_size is not None:
            self.request_header_size = request_header_size
        if http_redirect_to_https is not None:
            self.http_redirect_to_https = http_redirect_to_https
        if x_forwarded_for is not None:
            self.x_forwarded_for = x_forwarded_for
        if http_redirect_to is not None:
            self.http_redirect_to = http_redirect_to

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this LbHttpProfile.  # noqa: E501

        It is used to specify the HTTP application idle time out, instead of TCP socket setting which should be configured in TCP profile.   # noqa: E501

        :return: The idle_timeout of this LbHttpProfile.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this LbHttpProfile.

        It is used to specify the HTTP application idle time out, instead of TCP socket setting which should be configured in TCP profile.   # noqa: E501

        :param idle_timeout: The idle_timeout of this LbHttpProfile.  # noqa: E501
        :type: int
        """
        if idle_timeout is not None and idle_timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `idle_timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._idle_timeout = idle_timeout

    @property
    def ntlm(self):
        """Gets the ntlm of this LbHttpProfile.  # noqa: E501

        NTLM is an authentication protocol that can be used over HTTP. If the flag is set to true, LB will use NTLM challenge/response methodology.   # noqa: E501

        :return: The ntlm of this LbHttpProfile.  # noqa: E501
        :rtype: bool
        """
        return self._ntlm

    @ntlm.setter
    def ntlm(self, ntlm):
        """Sets the ntlm of this LbHttpProfile.

        NTLM is an authentication protocol that can be used over HTTP. If the flag is set to true, LB will use NTLM challenge/response methodology.   # noqa: E501

        :param ntlm: The ntlm of this LbHttpProfile.  # noqa: E501
        :type: bool
        """

        self._ntlm = ntlm

    @property
    def request_header_size(self):
        """Gets the request_header_size of this LbHttpProfile.  # noqa: E501

        A request with header larger than request_header_size will be processed as best effort whereas a request with header below this specified size is guaranteed to be processed.   # noqa: E501

        :return: The request_header_size of this LbHttpProfile.  # noqa: E501
        :rtype: int
        """
        return self._request_header_size

    @request_header_size.setter
    def request_header_size(self, request_header_size):
        """Sets the request_header_size of this LbHttpProfile.

        A request with header larger than request_header_size will be processed as best effort whereas a request with header below this specified size is guaranteed to be processed.   # noqa: E501

        :param request_header_size: The request_header_size of this LbHttpProfile.  # noqa: E501
        :type: int
        """
        if request_header_size is not None and request_header_size > 65536:  # noqa: E501
            raise ValueError("Invalid value for `request_header_size`, must be a value less than or equal to `65536`")  # noqa: E501
        if request_header_size is not None and request_header_size < 1:  # noqa: E501
            raise ValueError("Invalid value for `request_header_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._request_header_size = request_header_size

    @property
    def http_redirect_to_https(self):
        """Gets the http_redirect_to_https of this LbHttpProfile.  # noqa: E501

        Certain secure applications may want to force communication over SSL, but instead of rejecting non-SSL connections, they may choose to redirect the client automatically to use SSL.   # noqa: E501

        :return: The http_redirect_to_https of this LbHttpProfile.  # noqa: E501
        :rtype: bool
        """
        return self._http_redirect_to_https

    @http_redirect_to_https.setter
    def http_redirect_to_https(self, http_redirect_to_https):
        """Sets the http_redirect_to_https of this LbHttpProfile.

        Certain secure applications may want to force communication over SSL, but instead of rejecting non-SSL connections, they may choose to redirect the client automatically to use SSL.   # noqa: E501

        :param http_redirect_to_https: The http_redirect_to_https of this LbHttpProfile.  # noqa: E501
        :type: bool
        """

        self._http_redirect_to_https = http_redirect_to_https

    @property
    def x_forwarded_for(self):
        """Gets the x_forwarded_for of this LbHttpProfile.  # noqa: E501

        insert or replace x_forwarded_for  # noqa: E501

        :return: The x_forwarded_for of this LbHttpProfile.  # noqa: E501
        :rtype: str
        """
        return self._x_forwarded_for

    @x_forwarded_for.setter
    def x_forwarded_for(self, x_forwarded_for):
        """Sets the x_forwarded_for of this LbHttpProfile.

        insert or replace x_forwarded_for  # noqa: E501

        :param x_forwarded_for: The x_forwarded_for of this LbHttpProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["INSERT", "REPLACE"]  # noqa: E501
        if x_forwarded_for not in allowed_values:
            raise ValueError(
                "Invalid value for `x_forwarded_for` ({0}), must be one of {1}"  # noqa: E501
                .format(x_forwarded_for, allowed_values)
            )

        self._x_forwarded_for = x_forwarded_for

    @property
    def http_redirect_to(self):
        """Gets the http_redirect_to of this LbHttpProfile.  # noqa: E501

        If a website is temporarily down or has moved, incoming requests for that virtual server can be temporarily redirected to a URL   # noqa: E501

        :return: The http_redirect_to of this LbHttpProfile.  # noqa: E501
        :rtype: str
        """
        return self._http_redirect_to

    @http_redirect_to.setter
    def http_redirect_to(self, http_redirect_to):
        """Sets the http_redirect_to of this LbHttpProfile.

        If a website is temporarily down or has moved, incoming requests for that virtual server can be temporarily redirected to a URL   # noqa: E501

        :param http_redirect_to: The http_redirect_to of this LbHttpProfile.  # noqa: E501
        :type: str
        """

        self._http_redirect_to = http_redirect_to

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
        if not isinstance(other, LbHttpProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other