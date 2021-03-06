# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-06-22T02:34:44Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_server.model.common_code import CommonCode  # noqa: F401,E501
from ncloud_server.model.port_forwarding_rule import PortForwardingRule  # noqa: F401,E501
from ncloud_server.model.zone import Zone  # noqa: F401,E501


class GetPortForwardingRuleListResponse(object):
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
        'port_forwarding_configuration_no': 'str',
        'port_forwarding_public_ip': 'str',
        'zone': 'Zone',
        'internet_line_type': 'CommonCode',
        'total_rows': 'int',
        'port_forwarding_rule_list': 'list[PortForwardingRule]'
    }

    attribute_map = {
        'port_forwarding_configuration_no': 'portForwardingConfigurationNo',
        'port_forwarding_public_ip': 'portForwardingPublicIp',
        'zone': 'zone',
        'internet_line_type': 'internetLineType',
        'total_rows': 'totalRows',
        'port_forwarding_rule_list': 'portForwardingRuleList'
    }

    def __init__(self, port_forwarding_configuration_no=None, port_forwarding_public_ip=None, zone=None, internet_line_type=None, total_rows=None, port_forwarding_rule_list=None):  # noqa: E501
        """GetPortForwardingRuleListResponse - a model defined in Swagger"""  # noqa: E501

        self._port_forwarding_configuration_no = None
        self._port_forwarding_public_ip = None
        self._zone = None
        self._internet_line_type = None
        self._total_rows = None
        self._port_forwarding_rule_list = None
        self.discriminator = None

        if port_forwarding_configuration_no is not None:
            self.port_forwarding_configuration_no = port_forwarding_configuration_no
        if port_forwarding_public_ip is not None:
            self.port_forwarding_public_ip = port_forwarding_public_ip
        if zone is not None:
            self.zone = zone
        if internet_line_type is not None:
            self.internet_line_type = internet_line_type
        if total_rows is not None:
            self.total_rows = total_rows
        if port_forwarding_rule_list is not None:
            self.port_forwarding_rule_list = port_forwarding_rule_list

    @property
    def port_forwarding_configuration_no(self):
        """Gets the port_forwarding_configuration_no of this GetPortForwardingRuleListResponse.  # noqa: E501

        포트포워딩설정번호  # noqa: E501

        :return: The port_forwarding_configuration_no of this GetPortForwardingRuleListResponse.  # noqa: E501
        :rtype: str
        """
        return self._port_forwarding_configuration_no

    @port_forwarding_configuration_no.setter
    def port_forwarding_configuration_no(self, port_forwarding_configuration_no):
        """Sets the port_forwarding_configuration_no of this GetPortForwardingRuleListResponse.

        포트포워딩설정번호  # noqa: E501

        :param port_forwarding_configuration_no: The port_forwarding_configuration_no of this GetPortForwardingRuleListResponse.  # noqa: E501
        :type: str
        """

        self._port_forwarding_configuration_no = port_forwarding_configuration_no

    @property
    def port_forwarding_public_ip(self):
        """Gets the port_forwarding_public_ip of this GetPortForwardingRuleListResponse.  # noqa: E501

        포트포워딩공인IP  # noqa: E501

        :return: The port_forwarding_public_ip of this GetPortForwardingRuleListResponse.  # noqa: E501
        :rtype: str
        """
        return self._port_forwarding_public_ip

    @port_forwarding_public_ip.setter
    def port_forwarding_public_ip(self, port_forwarding_public_ip):
        """Sets the port_forwarding_public_ip of this GetPortForwardingRuleListResponse.

        포트포워딩공인IP  # noqa: E501

        :param port_forwarding_public_ip: The port_forwarding_public_ip of this GetPortForwardingRuleListResponse.  # noqa: E501
        :type: str
        """

        self._port_forwarding_public_ip = port_forwarding_public_ip

    @property
    def zone(self):
        """Gets the zone of this GetPortForwardingRuleListResponse.  # noqa: E501

        ZONE객체  # noqa: E501

        :return: The zone of this GetPortForwardingRuleListResponse.  # noqa: E501
        :rtype: Zone
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this GetPortForwardingRuleListResponse.

        ZONE객체  # noqa: E501

        :param zone: The zone of this GetPortForwardingRuleListResponse.  # noqa: E501
        :type: Zone
        """

        self._zone = zone

    @property
    def internet_line_type(self):
        """Gets the internet_line_type of this GetPortForwardingRuleListResponse.  # noqa: E501

        인터넷라인구분  # noqa: E501

        :return: The internet_line_type of this GetPortForwardingRuleListResponse.  # noqa: E501
        :rtype: CommonCode
        """
        return self._internet_line_type

    @internet_line_type.setter
    def internet_line_type(self, internet_line_type):
        """Sets the internet_line_type of this GetPortForwardingRuleListResponse.

        인터넷라인구분  # noqa: E501

        :param internet_line_type: The internet_line_type of this GetPortForwardingRuleListResponse.  # noqa: E501
        :type: CommonCode
        """

        self._internet_line_type = internet_line_type

    @property
    def total_rows(self):
        """Gets the total_rows of this GetPortForwardingRuleListResponse.  # noqa: E501


        :return: The total_rows of this GetPortForwardingRuleListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this GetPortForwardingRuleListResponse.


        :param total_rows: The total_rows of this GetPortForwardingRuleListResponse.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def port_forwarding_rule_list(self):
        """Gets the port_forwarding_rule_list of this GetPortForwardingRuleListResponse.  # noqa: E501


        :return: The port_forwarding_rule_list of this GetPortForwardingRuleListResponse.  # noqa: E501
        :rtype: list[PortForwardingRule]
        """
        return self._port_forwarding_rule_list

    @port_forwarding_rule_list.setter
    def port_forwarding_rule_list(self, port_forwarding_rule_list):
        """Sets the port_forwarding_rule_list of this GetPortForwardingRuleListResponse.


        :param port_forwarding_rule_list: The port_forwarding_rule_list of this GetPortForwardingRuleListResponse.  # noqa: E501
        :type: list[PortForwardingRule]
        """

        self._port_forwarding_rule_list = port_forwarding_rule_list

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
        if not isinstance(other, GetPortForwardingRuleListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
