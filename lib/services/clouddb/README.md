# ncloud-clouddb

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2018-06-21T02:28:05Z
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.NcpPythonForNcloudClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import ncloud_clouddb 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ncloud_clouddb
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
create_cloud_db_instance_request = ncloud_clouddb.CreateCloudDBInstanceRequest() # CreateCloudDBInstanceRequest | createCloudDBInstanceRequest

try:
    api_response = api_instance.create_cloud_db_instance(create_cloud_db_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_cloud_db_instance: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://ncloud.apigw.ntruss.com/clouddb/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*V2Api* | [**create_cloud_db_instance**](docs/V2Api.md#create_cloud_db_instance) | **POST** /createCloudDBInstance | 
*V2Api* | [**delete_cloud_db_server_instance**](docs/V2Api.md#delete_cloud_db_server_instance) | **POST** /deleteCloudDBServerInstance | 
*V2Api* | [**get_cloud_db_config_group_list**](docs/V2Api.md#get_cloud_db_config_group_list) | **POST** /getCloudDBConfigGroupList | 
*V2Api* | [**get_cloud_db_image_product_list**](docs/V2Api.md#get_cloud_db_image_product_list) | **POST** /getCloudDBImageProductList | 
*V2Api* | [**get_cloud_db_instance_list**](docs/V2Api.md#get_cloud_db_instance_list) | **POST** /getCloudDBInstanceList | 
*V2Api* | [**get_cloud_db_product_list**](docs/V2Api.md#get_cloud_db_product_list) | **POST** /getCloudDBProductList | 
*V2Api* | [**reboot_cloud_db_server_instance**](docs/V2Api.md#reboot_cloud_db_server_instance) | **POST** /rebootCloudDBServerInstance | 


## Documentation For Models

 - [AccessControlGroup](docs/AccessControlGroup.md)
 - [CloudDBConfig](docs/CloudDBConfig.md)
 - [CloudDBConfigGroup](docs/CloudDBConfigGroup.md)
 - [CloudDBInstance](docs/CloudDBInstance.md)
 - [CloudDBServerInstance](docs/CloudDBServerInstance.md)
 - [CommonCode](docs/CommonCode.md)
 - [CreateCloudDBInstanceRequest](docs/CreateCloudDBInstanceRequest.md)
 - [CreateCloudDBInstanceResponse](docs/CreateCloudDBInstanceResponse.md)
 - [DeleteCloudDBServerInstanceRequest](docs/DeleteCloudDBServerInstanceRequest.md)
 - [DeleteCloudDBServerInstanceResponse](docs/DeleteCloudDBServerInstanceResponse.md)
 - [GetCloudDBConfigGroupListRequest](docs/GetCloudDBConfigGroupListRequest.md)
 - [GetCloudDBConfigGroupListResponse](docs/GetCloudDBConfigGroupListResponse.md)
 - [GetCloudDBImageProductListRequest](docs/GetCloudDBImageProductListRequest.md)
 - [GetCloudDBImageProductListResponse](docs/GetCloudDBImageProductListResponse.md)
 - [GetCloudDBInstanceListRequest](docs/GetCloudDBInstanceListRequest.md)
 - [GetCloudDBInstanceListResponse](docs/GetCloudDBInstanceListResponse.md)
 - [GetCloudDBProductListRequest](docs/GetCloudDBProductListRequest.md)
 - [GetCloudDBProductListResponse](docs/GetCloudDBProductListResponse.md)
 - [Product](docs/Product.md)
 - [RebootCloudDBServerInstanceRequest](docs/RebootCloudDBServerInstanceRequest.md)
 - [RebootCloudDBServerInstanceResponse](docs/RebootCloudDBServerInstanceResponse.md)
 - [Region](docs/Region.md)
 - [Zone](docs/Zone.md)

