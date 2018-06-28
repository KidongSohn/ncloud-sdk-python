# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-06-22T02:34:44Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetAccessControlRuleListRequest(object):
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
        'access_control_group_configuration_no': 'str'
    }

    attribute_map = {
        'access_control_group_configuration_no': 'accessControlGroupConfigurationNo'
    }

    def __init__(self, access_control_group_configuration_no=None):  # noqa: E501
        """GetAccessControlRuleListRequest - a model defined in Swagger"""  # noqa: E501

        self._access_control_group_configuration_no = None
        self.discriminator = None

        self.access_control_group_configuration_no = access_control_group_configuration_no

    @property
    def access_control_group_configuration_no(self):
        """Gets the access_control_group_configuration_no of this GetAccessControlRuleListRequest.  # noqa: E501

        접근제어그룹설정번호  # noqa: E501

        :return: The access_control_group_configuration_no of this GetAccessControlRuleListRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_configuration_no

    @access_control_group_configuration_no.setter
    def access_control_group_configuration_no(self, access_control_group_configuration_no):
        """Sets the access_control_group_configuration_no of this GetAccessControlRuleListRequest.

        접근제어그룹설정번호  # noqa: E501

        :param access_control_group_configuration_no: The access_control_group_configuration_no of this GetAccessControlRuleListRequest.  # noqa: E501
        :type: str
        """
        if access_control_group_configuration_no is None:
            raise ValueError("Invalid value for `access_control_group_configuration_no`, must not be `None`")  # noqa: E501

        self._access_control_group_configuration_no = access_control_group_configuration_no

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
        if not isinstance(other, GetAccessControlRuleListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
