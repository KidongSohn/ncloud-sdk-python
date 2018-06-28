# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-06-21T02:22:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetLaunchConfigurationListRequest(object):
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
        'launch_configuration_name_list': 'list[str]',
        'page_no': 'int',
        'page_size': 'int',
        'sorted_by': 'str',
        'sorting_order': 'str'
    }

    attribute_map = {
        'launch_configuration_name_list': 'launchConfigurationNameList',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder'
    }

    def __init__(self, launch_configuration_name_list=None, page_no=None, page_size=None, sorted_by=None, sorting_order=None):  # noqa: E501
        """GetLaunchConfigurationListRequest - a model defined in Swagger"""  # noqa: E501

        self._launch_configuration_name_list = None
        self._page_no = None
        self._page_size = None
        self._sorted_by = None
        self._sorting_order = None
        self.discriminator = None

        if launch_configuration_name_list is not None:
            self.launch_configuration_name_list = launch_configuration_name_list
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order

    @property
    def launch_configuration_name_list(self):
        """Gets the launch_configuration_name_list of this GetLaunchConfigurationListRequest.  # noqa: E501

        론치설정명리스트  # noqa: E501

        :return: The launch_configuration_name_list of this GetLaunchConfigurationListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._launch_configuration_name_list

    @launch_configuration_name_list.setter
    def launch_configuration_name_list(self, launch_configuration_name_list):
        """Sets the launch_configuration_name_list of this GetLaunchConfigurationListRequest.

        론치설정명리스트  # noqa: E501

        :param launch_configuration_name_list: The launch_configuration_name_list of this GetLaunchConfigurationListRequest.  # noqa: E501
        :type: list[str]
        """

        self._launch_configuration_name_list = launch_configuration_name_list

    @property
    def page_no(self):
        """Gets the page_no of this GetLaunchConfigurationListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetLaunchConfigurationListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetLaunchConfigurationListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetLaunchConfigurationListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetLaunchConfigurationListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetLaunchConfigurationListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetLaunchConfigurationListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetLaunchConfigurationListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetLaunchConfigurationListRequest.  # noqa: E501

        소팅대상  # noqa: E501

        :return: The sorted_by of this GetLaunchConfigurationListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetLaunchConfigurationListRequest.

        소팅대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetLaunchConfigurationListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetLaunchConfigurationListRequest.  # noqa: E501

        소팅순서  # noqa: E501

        :return: The sorting_order of this GetLaunchConfigurationListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetLaunchConfigurationListRequest.

        소팅순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetLaunchConfigurationListRequest.  # noqa: E501
        :type: str
        """

        self._sorting_order = sorting_order

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
        if not isinstance(other, GetLaunchConfigurationListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other