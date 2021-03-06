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
from ncloud_server.model.region import Region  # noqa: F401,E501
from ncloud_server.model.zone import Zone  # noqa: F401,E501


class MemberServerImage(object):
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
        'member_server_image_no': 'str',
        'member_server_image_name': 'str',
        'member_server_image_description': 'str',
        'original_server_instance_no': 'str',
        'original_server_product_code': 'str',
        'original_server_name': 'str',
        'original_base_block_storage_disk_type': 'CommonCode',
        'original_server_image_product_code': 'str',
        'original_os_information': 'str',
        'original_server_image_name': 'str',
        'member_server_image_status_name': 'str',
        'member_server_image_status': 'CommonCode',
        'member_server_image_operation': 'CommonCode',
        'member_server_image_platform_type': 'CommonCode',
        'region': 'Region',
        'zone': 'Zone',
        'create_date': 'str',
        'member_server_image_block_storage_total_rows': 'int',
        'member_server_image_block_storage_total_size': 'int'
    }

    attribute_map = {
        'member_server_image_no': 'memberServerImageNo',
        'member_server_image_name': 'memberServerImageName',
        'member_server_image_description': 'memberServerImageDescription',
        'original_server_instance_no': 'originalServerInstanceNo',
        'original_server_product_code': 'originalServerProductCode',
        'original_server_name': 'originalServerName',
        'original_base_block_storage_disk_type': 'originalBaseBlockStorageDiskType',
        'original_server_image_product_code': 'originalServerImageProductCode',
        'original_os_information': 'originalOsInformation',
        'original_server_image_name': 'originalServerImageName',
        'member_server_image_status_name': 'memberServerImageStatusName',
        'member_server_image_status': 'memberServerImageStatus',
        'member_server_image_operation': 'memberServerImageOperation',
        'member_server_image_platform_type': 'memberServerImagePlatformType',
        'region': 'region',
        'zone': 'zone',
        'create_date': 'createDate',
        'member_server_image_block_storage_total_rows': 'memberServerImageBlockStorageTotalRows',
        'member_server_image_block_storage_total_size': 'memberServerImageBlockStorageTotalSize'
    }

    def __init__(self, member_server_image_no=None, member_server_image_name=None, member_server_image_description=None, original_server_instance_no=None, original_server_product_code=None, original_server_name=None, original_base_block_storage_disk_type=None, original_server_image_product_code=None, original_os_information=None, original_server_image_name=None, member_server_image_status_name=None, member_server_image_status=None, member_server_image_operation=None, member_server_image_platform_type=None, region=None, zone=None, create_date=None, member_server_image_block_storage_total_rows=None, member_server_image_block_storage_total_size=None):  # noqa: E501
        """MemberServerImage - a model defined in Swagger"""  # noqa: E501

        self._member_server_image_no = None
        self._member_server_image_name = None
        self._member_server_image_description = None
        self._original_server_instance_no = None
        self._original_server_product_code = None
        self._original_server_name = None
        self._original_base_block_storage_disk_type = None
        self._original_server_image_product_code = None
        self._original_os_information = None
        self._original_server_image_name = None
        self._member_server_image_status_name = None
        self._member_server_image_status = None
        self._member_server_image_operation = None
        self._member_server_image_platform_type = None
        self._region = None
        self._zone = None
        self._create_date = None
        self._member_server_image_block_storage_total_rows = None
        self._member_server_image_block_storage_total_size = None
        self.discriminator = None

        if member_server_image_no is not None:
            self.member_server_image_no = member_server_image_no
        if member_server_image_name is not None:
            self.member_server_image_name = member_server_image_name
        if member_server_image_description is not None:
            self.member_server_image_description = member_server_image_description
        if original_server_instance_no is not None:
            self.original_server_instance_no = original_server_instance_no
        if original_server_product_code is not None:
            self.original_server_product_code = original_server_product_code
        if original_server_name is not None:
            self.original_server_name = original_server_name
        if original_base_block_storage_disk_type is not None:
            self.original_base_block_storage_disk_type = original_base_block_storage_disk_type
        if original_server_image_product_code is not None:
            self.original_server_image_product_code = original_server_image_product_code
        if original_os_information is not None:
            self.original_os_information = original_os_information
        if original_server_image_name is not None:
            self.original_server_image_name = original_server_image_name
        if member_server_image_status_name is not None:
            self.member_server_image_status_name = member_server_image_status_name
        if member_server_image_status is not None:
            self.member_server_image_status = member_server_image_status
        if member_server_image_operation is not None:
            self.member_server_image_operation = member_server_image_operation
        if member_server_image_platform_type is not None:
            self.member_server_image_platform_type = member_server_image_platform_type
        if region is not None:
            self.region = region
        if zone is not None:
            self.zone = zone
        if create_date is not None:
            self.create_date = create_date
        if member_server_image_block_storage_total_rows is not None:
            self.member_server_image_block_storage_total_rows = member_server_image_block_storage_total_rows
        if member_server_image_block_storage_total_size is not None:
            self.member_server_image_block_storage_total_size = member_server_image_block_storage_total_size

    @property
    def member_server_image_no(self):
        """Gets the member_server_image_no of this MemberServerImage.  # noqa: E501

        회원서버이미지번호  # noqa: E501

        :return: The member_server_image_no of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_no

    @member_server_image_no.setter
    def member_server_image_no(self, member_server_image_no):
        """Sets the member_server_image_no of this MemberServerImage.

        회원서버이미지번호  # noqa: E501

        :param member_server_image_no: The member_server_image_no of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._member_server_image_no = member_server_image_no

    @property
    def member_server_image_name(self):
        """Gets the member_server_image_name of this MemberServerImage.  # noqa: E501

        회원서버이미지명  # noqa: E501

        :return: The member_server_image_name of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_name

    @member_server_image_name.setter
    def member_server_image_name(self, member_server_image_name):
        """Sets the member_server_image_name of this MemberServerImage.

        회원서버이미지명  # noqa: E501

        :param member_server_image_name: The member_server_image_name of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._member_server_image_name = member_server_image_name

    @property
    def member_server_image_description(self):
        """Gets the member_server_image_description of this MemberServerImage.  # noqa: E501

        회원서버이미지설명  # noqa: E501

        :return: The member_server_image_description of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_description

    @member_server_image_description.setter
    def member_server_image_description(self, member_server_image_description):
        """Sets the member_server_image_description of this MemberServerImage.

        회원서버이미지설명  # noqa: E501

        :param member_server_image_description: The member_server_image_description of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._member_server_image_description = member_server_image_description

    @property
    def original_server_instance_no(self):
        """Gets the original_server_instance_no of this MemberServerImage.  # noqa: E501

        원본서버인스턴스번호  # noqa: E501

        :return: The original_server_instance_no of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._original_server_instance_no

    @original_server_instance_no.setter
    def original_server_instance_no(self, original_server_instance_no):
        """Sets the original_server_instance_no of this MemberServerImage.

        원본서버인스턴스번호  # noqa: E501

        :param original_server_instance_no: The original_server_instance_no of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._original_server_instance_no = original_server_instance_no

    @property
    def original_server_product_code(self):
        """Gets the original_server_product_code of this MemberServerImage.  # noqa: E501

        원본서버상품코드  # noqa: E501

        :return: The original_server_product_code of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._original_server_product_code

    @original_server_product_code.setter
    def original_server_product_code(self, original_server_product_code):
        """Sets the original_server_product_code of this MemberServerImage.

        원본서버상품코드  # noqa: E501

        :param original_server_product_code: The original_server_product_code of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._original_server_product_code = original_server_product_code

    @property
    def original_server_name(self):
        """Gets the original_server_name of this MemberServerImage.  # noqa: E501

        원본서버명  # noqa: E501

        :return: The original_server_name of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._original_server_name

    @original_server_name.setter
    def original_server_name(self, original_server_name):
        """Sets the original_server_name of this MemberServerImage.

        원본서버명  # noqa: E501

        :param original_server_name: The original_server_name of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._original_server_name = original_server_name

    @property
    def original_base_block_storage_disk_type(self):
        """Gets the original_base_block_storage_disk_type of this MemberServerImage.  # noqa: E501

        원본서버기본블록스토리지디스크유형  # noqa: E501

        :return: The original_base_block_storage_disk_type of this MemberServerImage.  # noqa: E501
        :rtype: CommonCode
        """
        return self._original_base_block_storage_disk_type

    @original_base_block_storage_disk_type.setter
    def original_base_block_storage_disk_type(self, original_base_block_storage_disk_type):
        """Sets the original_base_block_storage_disk_type of this MemberServerImage.

        원본서버기본블록스토리지디스크유형  # noqa: E501

        :param original_base_block_storage_disk_type: The original_base_block_storage_disk_type of this MemberServerImage.  # noqa: E501
        :type: CommonCode
        """

        self._original_base_block_storage_disk_type = original_base_block_storage_disk_type

    @property
    def original_server_image_product_code(self):
        """Gets the original_server_image_product_code of this MemberServerImage.  # noqa: E501

        원본서버이미지상품코드  # noqa: E501

        :return: The original_server_image_product_code of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._original_server_image_product_code

    @original_server_image_product_code.setter
    def original_server_image_product_code(self, original_server_image_product_code):
        """Sets the original_server_image_product_code of this MemberServerImage.

        원본서버이미지상품코드  # noqa: E501

        :param original_server_image_product_code: The original_server_image_product_code of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._original_server_image_product_code = original_server_image_product_code

    @property
    def original_os_information(self):
        """Gets the original_os_information of this MemberServerImage.  # noqa: E501

        원본OS정보  # noqa: E501

        :return: The original_os_information of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._original_os_information

    @original_os_information.setter
    def original_os_information(self, original_os_information):
        """Sets the original_os_information of this MemberServerImage.

        원본OS정보  # noqa: E501

        :param original_os_information: The original_os_information of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._original_os_information = original_os_information

    @property
    def original_server_image_name(self):
        """Gets the original_server_image_name of this MemberServerImage.  # noqa: E501

        원본서버이미지명  # noqa: E501

        :return: The original_server_image_name of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._original_server_image_name

    @original_server_image_name.setter
    def original_server_image_name(self, original_server_image_name):
        """Sets the original_server_image_name of this MemberServerImage.

        원본서버이미지명  # noqa: E501

        :param original_server_image_name: The original_server_image_name of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._original_server_image_name = original_server_image_name

    @property
    def member_server_image_status_name(self):
        """Gets the member_server_image_status_name of this MemberServerImage.  # noqa: E501

        원본서버이미지상태명  # noqa: E501

        :return: The member_server_image_status_name of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_status_name

    @member_server_image_status_name.setter
    def member_server_image_status_name(self, member_server_image_status_name):
        """Sets the member_server_image_status_name of this MemberServerImage.

        원본서버이미지상태명  # noqa: E501

        :param member_server_image_status_name: The member_server_image_status_name of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._member_server_image_status_name = member_server_image_status_name

    @property
    def member_server_image_status(self):
        """Gets the member_server_image_status of this MemberServerImage.  # noqa: E501

        원본서버이미지상태  # noqa: E501

        :return: The member_server_image_status of this MemberServerImage.  # noqa: E501
        :rtype: CommonCode
        """
        return self._member_server_image_status

    @member_server_image_status.setter
    def member_server_image_status(self, member_server_image_status):
        """Sets the member_server_image_status of this MemberServerImage.

        원본서버이미지상태  # noqa: E501

        :param member_server_image_status: The member_server_image_status of this MemberServerImage.  # noqa: E501
        :type: CommonCode
        """

        self._member_server_image_status = member_server_image_status

    @property
    def member_server_image_operation(self):
        """Gets the member_server_image_operation of this MemberServerImage.  # noqa: E501

        원본서버이미지OP  # noqa: E501

        :return: The member_server_image_operation of this MemberServerImage.  # noqa: E501
        :rtype: CommonCode
        """
        return self._member_server_image_operation

    @member_server_image_operation.setter
    def member_server_image_operation(self, member_server_image_operation):
        """Sets the member_server_image_operation of this MemberServerImage.

        원본서버이미지OP  # noqa: E501

        :param member_server_image_operation: The member_server_image_operation of this MemberServerImage.  # noqa: E501
        :type: CommonCode
        """

        self._member_server_image_operation = member_server_image_operation

    @property
    def member_server_image_platform_type(self):
        """Gets the member_server_image_platform_type of this MemberServerImage.  # noqa: E501

        회원서버이미지플랫폼구분  # noqa: E501

        :return: The member_server_image_platform_type of this MemberServerImage.  # noqa: E501
        :rtype: CommonCode
        """
        return self._member_server_image_platform_type

    @member_server_image_platform_type.setter
    def member_server_image_platform_type(self, member_server_image_platform_type):
        """Sets the member_server_image_platform_type of this MemberServerImage.

        회원서버이미지플랫폼구분  # noqa: E501

        :param member_server_image_platform_type: The member_server_image_platform_type of this MemberServerImage.  # noqa: E501
        :type: CommonCode
        """

        self._member_server_image_platform_type = member_server_image_platform_type

    @property
    def region(self):
        """Gets the region of this MemberServerImage.  # noqa: E501

        리전  # noqa: E501

        :return: The region of this MemberServerImage.  # noqa: E501
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MemberServerImage.

        리전  # noqa: E501

        :param region: The region of this MemberServerImage.  # noqa: E501
        :type: Region
        """

        self._region = region

    @property
    def zone(self):
        """Gets the zone of this MemberServerImage.  # noqa: E501

        ZONE  # noqa: E501

        :return: The zone of this MemberServerImage.  # noqa: E501
        :rtype: Zone
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this MemberServerImage.

        ZONE  # noqa: E501

        :param zone: The zone of this MemberServerImage.  # noqa: E501
        :type: Zone
        """

        self._zone = zone

    @property
    def create_date(self):
        """Gets the create_date of this MemberServerImage.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this MemberServerImage.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this MemberServerImage.

        생성일시  # noqa: E501

        :param create_date: The create_date of this MemberServerImage.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def member_server_image_block_storage_total_rows(self):
        """Gets the member_server_image_block_storage_total_rows of this MemberServerImage.  # noqa: E501

        회원서버이미지블록스토리지인스턴스총 개수  # noqa: E501

        :return: The member_server_image_block_storage_total_rows of this MemberServerImage.  # noqa: E501
        :rtype: int
        """
        return self._member_server_image_block_storage_total_rows

    @member_server_image_block_storage_total_rows.setter
    def member_server_image_block_storage_total_rows(self, member_server_image_block_storage_total_rows):
        """Sets the member_server_image_block_storage_total_rows of this MemberServerImage.

        회원서버이미지블록스토리지인스턴스총 개수  # noqa: E501

        :param member_server_image_block_storage_total_rows: The member_server_image_block_storage_total_rows of this MemberServerImage.  # noqa: E501
        :type: int
        """

        self._member_server_image_block_storage_total_rows = member_server_image_block_storage_total_rows

    @property
    def member_server_image_block_storage_total_size(self):
        """Gets the member_server_image_block_storage_total_size of this MemberServerImage.  # noqa: E501

        회원서버이미지총사이즈  # noqa: E501

        :return: The member_server_image_block_storage_total_size of this MemberServerImage.  # noqa: E501
        :rtype: int
        """
        return self._member_server_image_block_storage_total_size

    @member_server_image_block_storage_total_size.setter
    def member_server_image_block_storage_total_size(self, member_server_image_block_storage_total_size):
        """Sets the member_server_image_block_storage_total_size of this MemberServerImage.

        회원서버이미지총사이즈  # noqa: E501

        :param member_server_image_block_storage_total_size: The member_server_image_block_storage_total_size of this MemberServerImage.  # noqa: E501
        :type: int
        """

        self._member_server_image_block_storage_total_size = member_server_image_block_storage_total_size

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
        if not isinstance(other, MemberServerImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
