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

from swagger_client.models.backup_file import BackupFile  # noqa: F401,E501


class RemoteFilestoreBackupFile(object):
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
        'passphrase': 'str',
        'file_store': 'str',
        'port': 'int',
        'uri': 'str',
        'server': 'str'
    }

    attribute_map = {
        'passphrase': 'passphrase',
        'file_store': 'file_store',
        'port': 'port',
        'uri': 'uri',
        'server': 'server'
    }

    def __init__(self, passphrase=None, file_store=None, port=None, uri=None, server=None):  # noqa: E501
        """RemoteFilestoreBackupFile - a model defined in Swagger"""  # noqa: E501

        self._passphrase = None
        self._file_store = None
        self._port = None
        self._uri = None
        self._server = None
        self.discriminator = None

        self.passphrase = passphrase
        self.file_store = file_store
        if port is not None:
            self.port = port
        self.uri = uri
        self.server = server

    @property
    def passphrase(self):
        """Gets the passphrase of this RemoteFilestoreBackupFile.  # noqa: E501

        Passphrase used to encrypt backup file  # noqa: E501

        :return: The passphrase of this RemoteFilestoreBackupFile.  # noqa: E501
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this RemoteFilestoreBackupFile.

        Passphrase used to encrypt backup file  # noqa: E501

        :param passphrase: The passphrase of this RemoteFilestoreBackupFile.  # noqa: E501
        :type: str
        """
        if passphrase is None:
            raise ValueError("Invalid value for `passphrase`, must not be `None`")  # noqa: E501

        self._passphrase = passphrase

    @property
    def file_store(self):
        """Gets the file_store of this RemoteFilestoreBackupFile.  # noqa: E501

        File location  # noqa: E501

        :return: The file_store of this RemoteFilestoreBackupFile.  # noqa: E501
        :rtype: str
        """
        return self._file_store

    @file_store.setter
    def file_store(self, file_store):
        """Sets the file_store of this RemoteFilestoreBackupFile.

        File location  # noqa: E501

        :param file_store: The file_store of this RemoteFilestoreBackupFile.  # noqa: E501
        :type: str
        """
        if file_store is None:
            raise ValueError("Invalid value for `file_store`, must not be `None`")  # noqa: E501
        allowed_values = ["remote"]  # noqa: E501
        if file_store not in allowed_values:
            raise ValueError(
                "Invalid value for `file_store` ({0}), must be one of {1}"  # noqa: E501
                .format(file_store, allowed_values)
            )

        self._file_store = file_store

    @property
    def port(self):
        """Gets the port of this RemoteFilestoreBackupFile.  # noqa: E501

        Server port  # noqa: E501

        :return: The port of this RemoteFilestoreBackupFile.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this RemoteFilestoreBackupFile.

        Server port  # noqa: E501

        :param port: The port of this RemoteFilestoreBackupFile.  # noqa: E501
        :type: int
        """
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 1:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

    @property
    def uri(self):
        """Gets the uri of this RemoteFilestoreBackupFile.  # noqa: E501

        URI of file to copy  # noqa: E501

        :return: The uri of this RemoteFilestoreBackupFile.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RemoteFilestoreBackupFile.

        URI of file to copy  # noqa: E501

        :param uri: The uri of this RemoteFilestoreBackupFile.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def server(self):
        """Gets the server of this RemoteFilestoreBackupFile.  # noqa: E501

        Remote server hostname or IP address  # noqa: E501

        :return: The server of this RemoteFilestoreBackupFile.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this RemoteFilestoreBackupFile.

        Remote server hostname or IP address  # noqa: E501

        :param server: The server of this RemoteFilestoreBackupFile.  # noqa: E501
        :type: str
        """
        if server is None:
            raise ValueError("Invalid value for `server`, must not be `None`")  # noqa: E501

        self._server = server

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
        if not isinstance(other, RemoteFilestoreBackupFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other