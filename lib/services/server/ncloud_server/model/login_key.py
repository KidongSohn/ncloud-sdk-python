# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-06-22T02:34:44Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoginKey(object):
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
        'fingerprint': 'str',
        'key_name': 'str',
        'create_date': 'str'
    }

    attribute_map = {
        'fingerprint': 'fingerprint',
        'key_name': 'keyName',
        'create_date': 'createDate'
    }

    def __init__(self, fingerprint=None, key_name=None, create_date=None):  # noqa: E501
        """LoginKey - a model defined in Swagger"""  # noqa: E501

        self._fingerprint = None
        self._key_name = None
        self._create_date = None
        self.discriminator = None

        if fingerprint is not None:
            self.fingerprint = fingerprint
        if key_name is not None:
            self.key_name = key_name
        if create_date is not None:
            self.create_date = create_date

    @property
    def fingerprint(self):
        """Gets the fingerprint of this LoginKey.  # noqa: E501

        핑거프린트  # noqa: E501

        :return: The fingerprint of this LoginKey.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this LoginKey.

        핑거프린트  # noqa: E501

        :param fingerprint: The fingerprint of this LoginKey.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def key_name(self):
        """Gets the key_name of this LoginKey.  # noqa: E501

        키명  # noqa: E501

        :return: The key_name of this LoginKey.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this LoginKey.

        키명  # noqa: E501

        :param key_name: The key_name of this LoginKey.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def create_date(self):
        """Gets the create_date of this LoginKey.  # noqa: E501

        생성일자  # noqa: E501

        :return: The create_date of this LoginKey.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this LoginKey.

        생성일자  # noqa: E501

        :param create_date: The create_date of this LoginKey.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

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
        if not isinstance(other, LoginKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other