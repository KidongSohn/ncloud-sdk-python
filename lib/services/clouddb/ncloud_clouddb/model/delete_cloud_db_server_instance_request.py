# coding: utf-8

"""
    clouddb

    OpenAPI spec version: 2018-06-21T02:28:05Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeleteCloudDBServerInstanceRequest(object):
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
        'cloud_db_server_instance_no': 'str'
    }

    attribute_map = {
        'cloud_db_server_instance_no': 'cloudDBServerInstanceNo'
    }

    def __init__(self, cloud_db_server_instance_no=None):  # noqa: E501
        """DeleteCloudDBServerInstanceRequest - a model defined in Swagger"""  # noqa: E501

        self._cloud_db_server_instance_no = None
        self.discriminator = None

        self.cloud_db_server_instance_no = cloud_db_server_instance_no

    @property
    def cloud_db_server_instance_no(self):
        """Gets the cloud_db_server_instance_no of this DeleteCloudDBServerInstanceRequest.  # noqa: E501

        CloudDB서버인스턴스번호  # noqa: E501

        :return: The cloud_db_server_instance_no of this DeleteCloudDBServerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cloud_db_server_instance_no

    @cloud_db_server_instance_no.setter
    def cloud_db_server_instance_no(self, cloud_db_server_instance_no):
        """Sets the cloud_db_server_instance_no of this DeleteCloudDBServerInstanceRequest.

        CloudDB서버인스턴스번호  # noqa: E501

        :param cloud_db_server_instance_no: The cloud_db_server_instance_no of this DeleteCloudDBServerInstanceRequest.  # noqa: E501
        :type: str
        """
        if cloud_db_server_instance_no is None:
            raise ValueError("Invalid value for `cloud_db_server_instance_no`, must not be `None`")  # noqa: E501

        self._cloud_db_server_instance_no = cloud_db_server_instance_no

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
        if not isinstance(other, DeleteCloudDBServerInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
