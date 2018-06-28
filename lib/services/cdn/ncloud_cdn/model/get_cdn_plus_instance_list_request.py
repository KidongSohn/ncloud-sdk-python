# coding: utf-8

"""
    cdn

    OpenAPI spec version: 2018-06-21T02:27:10Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCdnPlusInstanceListRequest(object):
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
        'cdn_instance_no': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'cdn_instance_no': 'cdnInstanceNo',
        'page_no': 'pageNo',
        'page_size': 'pageSize'
    }

    def __init__(self, cdn_instance_no=None, page_no=None, page_size=None):  # noqa: E501
        """GetCdnPlusInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._cdn_instance_no = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if cdn_instance_no is not None:
            self.cdn_instance_no = cdn_instance_no
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def cdn_instance_no(self):
        """Gets the cdn_instance_no of this GetCdnPlusInstanceListRequest.  # noqa: E501

        CDN 인스턴스 번호  # noqa: E501

        :return: The cdn_instance_no of this GetCdnPlusInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._cdn_instance_no

    @cdn_instance_no.setter
    def cdn_instance_no(self, cdn_instance_no):
        """Sets the cdn_instance_no of this GetCdnPlusInstanceListRequest.

        CDN 인스턴스 번호  # noqa: E501

        :param cdn_instance_no: The cdn_instance_no of this GetCdnPlusInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._cdn_instance_no = cdn_instance_no

    @property
    def page_no(self):
        """Gets the page_no of this GetCdnPlusInstanceListRequest.  # noqa: E501

        페이지 번호  # noqa: E501

        :return: The page_no of this GetCdnPlusInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetCdnPlusInstanceListRequest.

        페이지 번호  # noqa: E501

        :param page_no: The page_no of this GetCdnPlusInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetCdnPlusInstanceListRequest.  # noqa: E501

        페이지 사이즈  # noqa: E501

        :return: The page_size of this GetCdnPlusInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetCdnPlusInstanceListRequest.

        페이지 사이즈  # noqa: E501

        :param page_size: The page_size of this GetCdnPlusInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if not isinstance(other, GetCdnPlusInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other