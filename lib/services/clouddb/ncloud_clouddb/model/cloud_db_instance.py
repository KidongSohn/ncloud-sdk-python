# coding: utf-8

"""
    clouddb

    OpenAPI spec version: 2018-06-21T02:28:05Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_clouddb.model.access_control_group import AccessControlGroup  # noqa: F401,E501
from ncloud_clouddb.model.cloud_db_config import CloudDBConfig  # noqa: F401,E501
from ncloud_clouddb.model.cloud_db_config_group import CloudDBConfigGroup  # noqa: F401,E501
from ncloud_clouddb.model.cloud_db_server_instance import CloudDBServerInstance  # noqa: F401,E501
from ncloud_clouddb.model.common_code import CommonCode  # noqa: F401,E501
from ncloud_clouddb.model.region import Region  # noqa: F401,E501
from ncloud_clouddb.model.zone import Zone  # noqa: F401,E501


class CloudDBInstance(object):
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
        'cloud_db_instance_no': 'str',
        'cloud_db_service_name': 'str',
        'db_kind_code': 'str',
        'engine_version': 'str',
        'cpu_count': 'int',
        'memory_size': 'int',
        'data_storage_type': 'CommonCode',
        'license_code': 'str',
        'cloud_db_port': 'int',
        'is_ha': 'bool',
        'backup_time': 'str',
        'backup_file_retention_period': 'int',
        'cloud_db_instance_status_name': 'str',
        'collation': 'str',
        'reboot_schedule_time': 'str',
        'create_date': 'str',
        'cloud_db_image_product_code': 'str',
        'cloud_db_product_code': 'str',
        'is_cloud_db_config_need_reboot': 'bool',
        'is_cloud_db_need_reboot': 'bool',
        'zone': 'Zone',
        'region': 'Region',
        'cloud_db_config_list': 'list[CloudDBConfig]',
        'cloud_db_config_group_list': 'list[CloudDBConfigGroup]',
        'access_control_group_list': 'list[AccessControlGroup]',
        'cloud_db_server_instance_list': 'list[CloudDBServerInstance]'
    }

    attribute_map = {
        'cloud_db_instance_no': 'cloudDBInstanceNo',
        'cloud_db_service_name': 'cloudDBServiceName',
        'db_kind_code': 'dbKindCode',
        'engine_version': 'engineVersion',
        'cpu_count': 'cpuCount',
        'memory_size': 'memorySize',
        'data_storage_type': 'dataStorageType',
        'license_code': 'licenseCode',
        'cloud_db_port': 'cloudDBPort',
        'is_ha': 'isHa',
        'backup_time': 'backupTime',
        'backup_file_retention_period': 'backupFileRetentionPeriod',
        'cloud_db_instance_status_name': 'cloudDBInstanceStatusName',
        'collation': 'collation',
        'reboot_schedule_time': 'rebootScheduleTime',
        'create_date': 'createDate',
        'cloud_db_image_product_code': 'cloudDBImageProductCode',
        'cloud_db_product_code': 'cloudDBProductCode',
        'is_cloud_db_config_need_reboot': 'isCloudDBConfigNeedReboot',
        'is_cloud_db_need_reboot': 'isCloudDBNeedReboot',
        'zone': 'zone',
        'region': 'region',
        'cloud_db_config_list': 'cloudDBConfigList',
        'cloud_db_config_group_list': 'cloudDBConfigGroupList',
        'access_control_group_list': 'accessControlGroupList',
        'cloud_db_server_instance_list': 'cloudDBServerInstanceList'
    }

    def __init__(self, cloud_db_instance_no=None, cloud_db_service_name=None, db_kind_code=None, engine_version=None, cpu_count=None, memory_size=None, data_storage_type=None, license_code=None, cloud_db_port=None, is_ha=None, backup_time=None, backup_file_retention_period=None, cloud_db_instance_status_name=None, collation=None, reboot_schedule_time=None, create_date=None, cloud_db_image_product_code=None, cloud_db_product_code=None, is_cloud_db_config_need_reboot=None, is_cloud_db_need_reboot=None, zone=None, region=None, cloud_db_config_list=None, cloud_db_config_group_list=None, access_control_group_list=None, cloud_db_server_instance_list=None):  # noqa: E501
        """CloudDBInstance - a model defined in Swagger"""  # noqa: E501

        self._cloud_db_instance_no = None
        self._cloud_db_service_name = None
        self._db_kind_code = None
        self._engine_version = None
        self._cpu_count = None
        self._memory_size = None
        self._data_storage_type = None
        self._license_code = None
        self._cloud_db_port = None
        self._is_ha = None
        self._backup_time = None
        self._backup_file_retention_period = None
        self._cloud_db_instance_status_name = None
        self._collation = None
        self._reboot_schedule_time = None
        self._create_date = None
        self._cloud_db_image_product_code = None
        self._cloud_db_product_code = None
        self._is_cloud_db_config_need_reboot = None
        self._is_cloud_db_need_reboot = None
        self._zone = None
        self._region = None
        self._cloud_db_config_list = None
        self._cloud_db_config_group_list = None
        self._access_control_group_list = None
        self._cloud_db_server_instance_list = None
        self.discriminator = None

        if cloud_db_instance_no is not None:
            self.cloud_db_instance_no = cloud_db_instance_no
        if cloud_db_service_name is not None:
            self.cloud_db_service_name = cloud_db_service_name
        if db_kind_code is not None:
            self.db_kind_code = db_kind_code
        if engine_version is not None:
            self.engine_version = engine_version
        if cpu_count is not None:
            self.cpu_count = cpu_count
        if memory_size is not None:
            self.memory_size = memory_size
        if data_storage_type is not None:
            self.data_storage_type = data_storage_type
        if license_code is not None:
            self.license_code = license_code
        if cloud_db_port is not None:
            self.cloud_db_port = cloud_db_port
        if is_ha is not None:
            self.is_ha = is_ha
        if backup_time is not None:
            self.backup_time = backup_time
        if backup_file_retention_period is not None:
            self.backup_file_retention_period = backup_file_retention_period
        if cloud_db_instance_status_name is not None:
            self.cloud_db_instance_status_name = cloud_db_instance_status_name
        if collation is not None:
            self.collation = collation
        if reboot_schedule_time is not None:
            self.reboot_schedule_time = reboot_schedule_time
        if create_date is not None:
            self.create_date = create_date
        if cloud_db_image_product_code is not None:
            self.cloud_db_image_product_code = cloud_db_image_product_code
        if cloud_db_product_code is not None:
            self.cloud_db_product_code = cloud_db_product_code
        if is_cloud_db_config_need_reboot is not None:
            self.is_cloud_db_config_need_reboot = is_cloud_db_config_need_reboot
        if is_cloud_db_need_reboot is not None:
            self.is_cloud_db_need_reboot = is_cloud_db_need_reboot
        if zone is not None:
            self.zone = zone
        if region is not None:
            self.region = region
        if cloud_db_config_list is not None:
            self.cloud_db_config_list = cloud_db_config_list
        if cloud_db_config_group_list is not None:
            self.cloud_db_config_group_list = cloud_db_config_group_list
        if access_control_group_list is not None:
            self.access_control_group_list = access_control_group_list
        if cloud_db_server_instance_list is not None:
            self.cloud_db_server_instance_list = cloud_db_server_instance_list

    @property
    def cloud_db_instance_no(self):
        """Gets the cloud_db_instance_no of this CloudDBInstance.  # noqa: E501

        CloudDB인스턴스번호  # noqa: E501

        :return: The cloud_db_instance_no of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._cloud_db_instance_no

    @cloud_db_instance_no.setter
    def cloud_db_instance_no(self, cloud_db_instance_no):
        """Sets the cloud_db_instance_no of this CloudDBInstance.

        CloudDB인스턴스번호  # noqa: E501

        :param cloud_db_instance_no: The cloud_db_instance_no of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._cloud_db_instance_no = cloud_db_instance_no

    @property
    def cloud_db_service_name(self):
        """Gets the cloud_db_service_name of this CloudDBInstance.  # noqa: E501

        CloudDB서비스이름  # noqa: E501

        :return: The cloud_db_service_name of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._cloud_db_service_name

    @cloud_db_service_name.setter
    def cloud_db_service_name(self, cloud_db_service_name):
        """Sets the cloud_db_service_name of this CloudDBInstance.

        CloudDB서비스이름  # noqa: E501

        :param cloud_db_service_name: The cloud_db_service_name of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._cloud_db_service_name = cloud_db_service_name

    @property
    def db_kind_code(self):
        """Gets the db_kind_code of this CloudDBInstance.  # noqa: E501

        DB유형코드  # noqa: E501

        :return: The db_kind_code of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._db_kind_code

    @db_kind_code.setter
    def db_kind_code(self, db_kind_code):
        """Sets the db_kind_code of this CloudDBInstance.

        DB유형코드  # noqa: E501

        :param db_kind_code: The db_kind_code of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._db_kind_code = db_kind_code

    @property
    def engine_version(self):
        """Gets the engine_version of this CloudDBInstance.  # noqa: E501

        엔진버전  # noqa: E501

        :return: The engine_version of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this CloudDBInstance.

        엔진버전  # noqa: E501

        :param engine_version: The engine_version of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._engine_version = engine_version

    @property
    def cpu_count(self):
        """Gets the cpu_count of this CloudDBInstance.  # noqa: E501

        CPU개수  # noqa: E501

        :return: The cpu_count of this CloudDBInstance.  # noqa: E501
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """Sets the cpu_count of this CloudDBInstance.

        CPU개수  # noqa: E501

        :param cpu_count: The cpu_count of this CloudDBInstance.  # noqa: E501
        :type: int
        """

        self._cpu_count = cpu_count

    @property
    def memory_size(self):
        """Gets the memory_size of this CloudDBInstance.  # noqa: E501

        메모리사이즈  # noqa: E501

        :return: The memory_size of this CloudDBInstance.  # noqa: E501
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this CloudDBInstance.

        메모리사이즈  # noqa: E501

        :param memory_size: The memory_size of this CloudDBInstance.  # noqa: E501
        :type: int
        """

        self._memory_size = memory_size

    @property
    def data_storage_type(self):
        """Gets the data_storage_type of this CloudDBInstance.  # noqa: E501

        데이터스토리지타입  # noqa: E501

        :return: The data_storage_type of this CloudDBInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._data_storage_type

    @data_storage_type.setter
    def data_storage_type(self, data_storage_type):
        """Sets the data_storage_type of this CloudDBInstance.

        데이터스토리지타입  # noqa: E501

        :param data_storage_type: The data_storage_type of this CloudDBInstance.  # noqa: E501
        :type: CommonCode
        """

        self._data_storage_type = data_storage_type

    @property
    def license_code(self):
        """Gets the license_code of this CloudDBInstance.  # noqa: E501

        라이센스코드  # noqa: E501

        :return: The license_code of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._license_code

    @license_code.setter
    def license_code(self, license_code):
        """Sets the license_code of this CloudDBInstance.

        라이센스코드  # noqa: E501

        :param license_code: The license_code of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._license_code = license_code

    @property
    def cloud_db_port(self):
        """Gets the cloud_db_port of this CloudDBInstance.  # noqa: E501

        CloudDB포트  # noqa: E501

        :return: The cloud_db_port of this CloudDBInstance.  # noqa: E501
        :rtype: int
        """
        return self._cloud_db_port

    @cloud_db_port.setter
    def cloud_db_port(self, cloud_db_port):
        """Sets the cloud_db_port of this CloudDBInstance.

        CloudDB포트  # noqa: E501

        :param cloud_db_port: The cloud_db_port of this CloudDBInstance.  # noqa: E501
        :type: int
        """

        self._cloud_db_port = cloud_db_port

    @property
    def is_ha(self):
        """Gets the is_ha of this CloudDBInstance.  # noqa: E501

        HA여부  # noqa: E501

        :return: The is_ha of this CloudDBInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_ha

    @is_ha.setter
    def is_ha(self, is_ha):
        """Sets the is_ha of this CloudDBInstance.

        HA여부  # noqa: E501

        :param is_ha: The is_ha of this CloudDBInstance.  # noqa: E501
        :type: bool
        """

        self._is_ha = is_ha

    @property
    def backup_time(self):
        """Gets the backup_time of this CloudDBInstance.  # noqa: E501

        백업시간  # noqa: E501

        :return: The backup_time of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._backup_time

    @backup_time.setter
    def backup_time(self, backup_time):
        """Sets the backup_time of this CloudDBInstance.

        백업시간  # noqa: E501

        :param backup_time: The backup_time of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._backup_time = backup_time

    @property
    def backup_file_retention_period(self):
        """Gets the backup_file_retention_period of this CloudDBInstance.  # noqa: E501

        백업파일유지기간  # noqa: E501

        :return: The backup_file_retention_period of this CloudDBInstance.  # noqa: E501
        :rtype: int
        """
        return self._backup_file_retention_period

    @backup_file_retention_period.setter
    def backup_file_retention_period(self, backup_file_retention_period):
        """Sets the backup_file_retention_period of this CloudDBInstance.

        백업파일유지기간  # noqa: E501

        :param backup_file_retention_period: The backup_file_retention_period of this CloudDBInstance.  # noqa: E501
        :type: int
        """

        self._backup_file_retention_period = backup_file_retention_period

    @property
    def cloud_db_instance_status_name(self):
        """Gets the cloud_db_instance_status_name of this CloudDBInstance.  # noqa: E501

        CloudDB인스턴스상태이름  # noqa: E501

        :return: The cloud_db_instance_status_name of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._cloud_db_instance_status_name

    @cloud_db_instance_status_name.setter
    def cloud_db_instance_status_name(self, cloud_db_instance_status_name):
        """Sets the cloud_db_instance_status_name of this CloudDBInstance.

        CloudDB인스턴스상태이름  # noqa: E501

        :param cloud_db_instance_status_name: The cloud_db_instance_status_name of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._cloud_db_instance_status_name = cloud_db_instance_status_name

    @property
    def collation(self):
        """Gets the collation of this CloudDBInstance.  # noqa: E501

        Collation  # noqa: E501

        :return: The collation of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._collation

    @collation.setter
    def collation(self, collation):
        """Sets the collation of this CloudDBInstance.

        Collation  # noqa: E501

        :param collation: The collation of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._collation = collation

    @property
    def reboot_schedule_time(self):
        """Gets the reboot_schedule_time of this CloudDBInstance.  # noqa: E501

        재부팅예약시간  # noqa: E501

        :return: The reboot_schedule_time of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._reboot_schedule_time

    @reboot_schedule_time.setter
    def reboot_schedule_time(self, reboot_schedule_time):
        """Sets the reboot_schedule_time of this CloudDBInstance.

        재부팅예약시간  # noqa: E501

        :param reboot_schedule_time: The reboot_schedule_time of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._reboot_schedule_time = reboot_schedule_time

    @property
    def create_date(self):
        """Gets the create_date of this CloudDBInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this CloudDBInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def cloud_db_image_product_code(self):
        """Gets the cloud_db_image_product_code of this CloudDBInstance.  # noqa: E501

        CloudDB이미지상품코드  # noqa: E501

        :return: The cloud_db_image_product_code of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._cloud_db_image_product_code

    @cloud_db_image_product_code.setter
    def cloud_db_image_product_code(self, cloud_db_image_product_code):
        """Sets the cloud_db_image_product_code of this CloudDBInstance.

        CloudDB이미지상품코드  # noqa: E501

        :param cloud_db_image_product_code: The cloud_db_image_product_code of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._cloud_db_image_product_code = cloud_db_image_product_code

    @property
    def cloud_db_product_code(self):
        """Gets the cloud_db_product_code of this CloudDBInstance.  # noqa: E501

        CloudDB상품코드  # noqa: E501

        :return: The cloud_db_product_code of this CloudDBInstance.  # noqa: E501
        :rtype: str
        """
        return self._cloud_db_product_code

    @cloud_db_product_code.setter
    def cloud_db_product_code(self, cloud_db_product_code):
        """Sets the cloud_db_product_code of this CloudDBInstance.

        CloudDB상품코드  # noqa: E501

        :param cloud_db_product_code: The cloud_db_product_code of this CloudDBInstance.  # noqa: E501
        :type: str
        """

        self._cloud_db_product_code = cloud_db_product_code

    @property
    def is_cloud_db_config_need_reboot(self):
        """Gets the is_cloud_db_config_need_reboot of this CloudDBInstance.  # noqa: E501

        CloudDB설정재부팅필요여부  # noqa: E501

        :return: The is_cloud_db_config_need_reboot of this CloudDBInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_cloud_db_config_need_reboot

    @is_cloud_db_config_need_reboot.setter
    def is_cloud_db_config_need_reboot(self, is_cloud_db_config_need_reboot):
        """Sets the is_cloud_db_config_need_reboot of this CloudDBInstance.

        CloudDB설정재부팅필요여부  # noqa: E501

        :param is_cloud_db_config_need_reboot: The is_cloud_db_config_need_reboot of this CloudDBInstance.  # noqa: E501
        :type: bool
        """

        self._is_cloud_db_config_need_reboot = is_cloud_db_config_need_reboot

    @property
    def is_cloud_db_need_reboot(self):
        """Gets the is_cloud_db_need_reboot of this CloudDBInstance.  # noqa: E501

        CloudDB재부팅필요여부  # noqa: E501

        :return: The is_cloud_db_need_reboot of this CloudDBInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_cloud_db_need_reboot

    @is_cloud_db_need_reboot.setter
    def is_cloud_db_need_reboot(self, is_cloud_db_need_reboot):
        """Sets the is_cloud_db_need_reboot of this CloudDBInstance.

        CloudDB재부팅필요여부  # noqa: E501

        :param is_cloud_db_need_reboot: The is_cloud_db_need_reboot of this CloudDBInstance.  # noqa: E501
        :type: bool
        """

        self._is_cloud_db_need_reboot = is_cloud_db_need_reboot

    @property
    def zone(self):
        """Gets the zone of this CloudDBInstance.  # noqa: E501

        Zone  # noqa: E501

        :return: The zone of this CloudDBInstance.  # noqa: E501
        :rtype: Zone
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this CloudDBInstance.

        Zone  # noqa: E501

        :param zone: The zone of this CloudDBInstance.  # noqa: E501
        :type: Zone
        """

        self._zone = zone

    @property
    def region(self):
        """Gets the region of this CloudDBInstance.  # noqa: E501

        리전  # noqa: E501

        :return: The region of this CloudDBInstance.  # noqa: E501
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudDBInstance.

        리전  # noqa: E501

        :param region: The region of this CloudDBInstance.  # noqa: E501
        :type: Region
        """

        self._region = region

    @property
    def cloud_db_config_list(self):
        """Gets the cloud_db_config_list of this CloudDBInstance.  # noqa: E501


        :return: The cloud_db_config_list of this CloudDBInstance.  # noqa: E501
        :rtype: list[CloudDBConfig]
        """
        return self._cloud_db_config_list

    @cloud_db_config_list.setter
    def cloud_db_config_list(self, cloud_db_config_list):
        """Sets the cloud_db_config_list of this CloudDBInstance.


        :param cloud_db_config_list: The cloud_db_config_list of this CloudDBInstance.  # noqa: E501
        :type: list[CloudDBConfig]
        """

        self._cloud_db_config_list = cloud_db_config_list

    @property
    def cloud_db_config_group_list(self):
        """Gets the cloud_db_config_group_list of this CloudDBInstance.  # noqa: E501


        :return: The cloud_db_config_group_list of this CloudDBInstance.  # noqa: E501
        :rtype: list[CloudDBConfigGroup]
        """
        return self._cloud_db_config_group_list

    @cloud_db_config_group_list.setter
    def cloud_db_config_group_list(self, cloud_db_config_group_list):
        """Sets the cloud_db_config_group_list of this CloudDBInstance.


        :param cloud_db_config_group_list: The cloud_db_config_group_list of this CloudDBInstance.  # noqa: E501
        :type: list[CloudDBConfigGroup]
        """

        self._cloud_db_config_group_list = cloud_db_config_group_list

    @property
    def access_control_group_list(self):
        """Gets the access_control_group_list of this CloudDBInstance.  # noqa: E501


        :return: The access_control_group_list of this CloudDBInstance.  # noqa: E501
        :rtype: list[AccessControlGroup]
        """
        return self._access_control_group_list

    @access_control_group_list.setter
    def access_control_group_list(self, access_control_group_list):
        """Sets the access_control_group_list of this CloudDBInstance.


        :param access_control_group_list: The access_control_group_list of this CloudDBInstance.  # noqa: E501
        :type: list[AccessControlGroup]
        """

        self._access_control_group_list = access_control_group_list

    @property
    def cloud_db_server_instance_list(self):
        """Gets the cloud_db_server_instance_list of this CloudDBInstance.  # noqa: E501


        :return: The cloud_db_server_instance_list of this CloudDBInstance.  # noqa: E501
        :rtype: list[CloudDBServerInstance]
        """
        return self._cloud_db_server_instance_list

    @cloud_db_server_instance_list.setter
    def cloud_db_server_instance_list(self, cloud_db_server_instance_list):
        """Sets the cloud_db_server_instance_list of this CloudDBInstance.


        :param cloud_db_server_instance_list: The cloud_db_server_instance_list of this CloudDBInstance.  # noqa: E501
        :type: list[CloudDBServerInstance]
        """

        self._cloud_db_server_instance_list = cloud_db_server_instance_list

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
        if not isinstance(other, CloudDBInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other