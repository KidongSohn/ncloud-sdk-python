# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-06-21T02:22:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SetServerInstanceHealthRequest(object):
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
        'health_status_code': 'str',
        'server_instance_no': 'str',
        'should_respect_grace_period': 'bool'
    }

    attribute_map = {
        'health_status_code': 'healthStatusCode',
        'server_instance_no': 'serverInstanceNo',
        'should_respect_grace_period': 'shouldRespectGracePeriod'
    }

    def __init__(self, health_status_code=None, server_instance_no=None, should_respect_grace_period=None):  # noqa: E501
        """SetServerInstanceHealthRequest - a model defined in Swagger"""  # noqa: E501

        self._health_status_code = None
        self._server_instance_no = None
        self._should_respect_grace_period = None
        self.discriminator = None

        self.health_status_code = health_status_code
        self.server_instance_no = server_instance_no
        if should_respect_grace_period is not None:
            self.should_respect_grace_period = should_respect_grace_period

    @property
    def health_status_code(self):
        """Gets the health_status_code of this SetServerInstanceHealthRequest.  # noqa: E501

        헬스상태코드  # noqa: E501

        :return: The health_status_code of this SetServerInstanceHealthRequest.  # noqa: E501
        :rtype: str
        """
        return self._health_status_code

    @health_status_code.setter
    def health_status_code(self, health_status_code):
        """Sets the health_status_code of this SetServerInstanceHealthRequest.

        헬스상태코드  # noqa: E501

        :param health_status_code: The health_status_code of this SetServerInstanceHealthRequest.  # noqa: E501
        :type: str
        """
        if health_status_code is None:
            raise ValueError("Invalid value for `health_status_code`, must not be `None`")  # noqa: E501

        self._health_status_code = health_status_code

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this SetServerInstanceHealthRequest.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this SetServerInstanceHealthRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this SetServerInstanceHealthRequest.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this SetServerInstanceHealthRequest.  # noqa: E501
        :type: str
        """
        if server_instance_no is None:
            raise ValueError("Invalid value for `server_instance_no`, must not be `None`")  # noqa: E501

        self._server_instance_no = server_instance_no

    @property
    def should_respect_grace_period(self):
        """Gets the should_respect_grace_period of this SetServerInstanceHealthRequest.  # noqa: E501

        health-check grace-period 존중여부  # noqa: E501

        :return: The should_respect_grace_period of this SetServerInstanceHealthRequest.  # noqa: E501
        :rtype: bool
        """
        return self._should_respect_grace_period

    @should_respect_grace_period.setter
    def should_respect_grace_period(self, should_respect_grace_period):
        """Sets the should_respect_grace_period of this SetServerInstanceHealthRequest.

        health-check grace-period 존중여부  # noqa: E501

        :param should_respect_grace_period: The should_respect_grace_period of this SetServerInstanceHealthRequest.  # noqa: E501
        :type: bool
        """

        self._should_respect_grace_period = should_respect_grace_period

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
        if not isinstance(other, SetServerInstanceHealthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
