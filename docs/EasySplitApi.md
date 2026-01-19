# cashfree_pg.EasySplitApi

All URIs are relative to *https://sandbox.cashfree.com/pg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_g_order_split_after_payment**](EasySplitApi.md#p_g_order_split_after_payment) | **POST** /easy-split/orders/{order_id}/split | Split After Payment
[**p_g_order_static_split**](EasySplitApi.md#p_g_order_static_split) | **POST** /easy-split/static-split | Create Static Split Configuration
[**p_g_split_order_recon**](EasySplitApi.md#p_g_split_order_recon) | **GET** /easy-split/orders/{order_id} | Get Split and Settlement Details by OrderID
[**p_ges_create_adjustment**](EasySplitApi.md#p_ges_create_adjustment) | **POST** /easy-split/vendors/{vendor_id}/adjustment | Create Adjustment
[**p_ges_create_on_demand_transfer**](EasySplitApi.md#p_ges_create_on_demand_transfer) | **POST** /easy-split/vendors/{vendor_id}/transfer | Create On Demand Transfer
[**p_ges_create_vendors**](EasySplitApi.md#p_ges_create_vendors) | **POST** /easy-split/vendors | Create vendor
[**p_ges_download_vendors_docs**](EasySplitApi.md#p_ges_download_vendors_docs) | **GET** /easy-split/vendor-docs/{vendor_id}/download/{doc_type} | Download Vendor Documents
[**p_ges_fetch_vendors**](EasySplitApi.md#p_ges_fetch_vendors) | **GET** /easy-split/vendors/{vendor_id} | Get Vendor All Details
[**p_ges_get_vendor_balance**](EasySplitApi.md#p_ges_get_vendor_balance) | **GET** /easy-split/vendors/{vendor_id}/balances | Get On Demand Balance
[**p_ges_get_vendor_balance_transfer_charges**](EasySplitApi.md#p_ges_get_vendor_balance_transfer_charges) | **GET** /easy-split/amount/{amount}/charges | Get Vendor Balance Transfer Charges
[**p_ges_get_vendors_docs**](EasySplitApi.md#p_ges_get_vendors_docs) | **GET** /easy-split/vendor-docs/{vendor_id} | Get Vendor All Documents Status
[**p_ges_order_recon**](EasySplitApi.md#p_ges_order_recon) | **POST** /split/order/vendor/recon | Get Split and Settlement Details by OrderID v2.0
[**p_ges_update_vendors**](EasySplitApi.md#p_ges_update_vendors) | **PATCH** /easy-split/vendors/{vendor_id} | Update vendor Details
[**p_ges_upload_vendors_docs**](EasySplitApi.md#p_ges_upload_vendors_docs) | **POST** /easy-split/vendor-docs/{vendor_id} | Upload Vendor Docs


# **p_g_order_split_after_payment**
> SplitAfterPaymentResponse p_g_order_split_after_payment(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, split_after_payment_request=split_after_payment_request)

Split After Payment

Split After Payment API splits the payments to vendors after successful payment from the customers.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.split_after_payment_request import SplitAfterPaymentRequest
from cashfree_pg.models.split_after_payment_response import SplitAfterPaymentResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    order_id = 'your-order-id' # str | The id which uniquely identifies your order
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    split_after_payment_request = {"split":[{"vendor_id":"test03","percentage":10,"tags":{"product":"Dri-Fit trouser","size":"L","AWB":"NIKE12334"}}],"disable_split":true} # SplitAfterPaymentRequest | Request Body to Create Split for an order. (optional)

    try:
        # Split After Payment
        api_response = api_instance.p_g_order_split_after_payment(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, split_after_payment_request=split_after_payment_request)
        print("The response of EasySplitApi->p_g_order_split_after_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_g_order_split_after_payment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **order_id** | **str**| The id which uniquely identifies your order | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **split_after_payment_request** | [**SplitAfterPaymentRequest**](SplitAfterPaymentRequest.md)| Request Body to Create Split for an order. | [optional] 

### Return type

[**SplitAfterPaymentResponse**](SplitAfterPaymentResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Split After Payment Success Response. |  -  |
**400** | Split After Payment Failure Response. |  -  |
**404** | Split After Payment Failure Response. |  -  |
**409** | Split After Payment Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_g_order_static_split**
> StaticSplitResponse p_g_order_static_split(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, static_split_request=static_split_request)

Create Static Split Configuration

This API will create a static split scheme wherein you can define the split type and the vendor-wise split percentage.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.static_split_request import StaticSplitRequest
from cashfree_pg.models.static_split_response import StaticSplitResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    static_split_request = {"active":true,"terminal_id":0,"product_type":"PG","scheme":[{"merchant_vendor_id":"EsTest1Success","percentage":10}]} # StaticSplitRequest | Static Split (optional)

    try:
        # Create Static Split Configuration
        api_response = api_instance.p_g_order_static_split(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, static_split_request=static_split_request)
        print("The response of EasySplitApi->p_g_order_static_split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_g_order_static_split: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **static_split_request** | [**StaticSplitRequest**](StaticSplitRequest.md)| Static Split | [optional] 

### Return type

[**StaticSplitResponse**](StaticSplitResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Static Split Success Response. |  -  |
**400** | Static Split Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_g_split_order_recon**
> SplitOrderReconSuccessResponse p_g_split_order_recon(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Split and Settlement Details by OrderID

Use this API to get all the split details, settled and unsettled transactions details of each vendor who were part of a particular order by providing order Id or start date and end date.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.split_order_recon_success_response import SplitOrderReconSuccessResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    order_id = 'your-order-id' # str | The id which uniquely identifies your order
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get Split and Settlement Details by OrderID
        api_response = api_instance.p_g_split_order_recon(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of EasySplitApi->p_g_split_order_recon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_g_split_order_recon: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **order_id** | **str**| The id which uniquely identifies your order | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**SplitOrderReconSuccessResponse**](SplitOrderReconSuccessResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Split and Settlement Details by OrderID |  -  |
**404** | Split Order Recon Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_create_adjustment**
> VendorAdjustmentSuccessResponse p_ges_create_adjustment(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, vendor_adjustment_request=vendor_adjustment_request)

Create Adjustment

The Create Adjustment API will create a adjustment request either from vendor to the merchant or from merchant to the vendor.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.vendor_adjustment_request import VendorAdjustmentRequest
from cashfree_pg.models.vendor_adjustment_success_response import VendorAdjustmentSuccessResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    vendor_adjustment_request = {"vendor_id":"test_123","adjustment_id":1234567,"amount":10,"type":"CREDIT","remarks":"Testing"} # VendorAdjustmentRequest | Vendor Adjustment Request Body. (optional)

    try:
        # Create Adjustment
        api_response = api_instance.p_ges_create_adjustment(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, vendor_adjustment_request=vendor_adjustment_request)
        print("The response of EasySplitApi->p_ges_create_adjustment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_create_adjustment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **vendor_adjustment_request** | [**VendorAdjustmentRequest**](VendorAdjustmentRequest.md)| Vendor Adjustment Request Body. | [optional] 

### Return type

[**VendorAdjustmentSuccessResponse**](VendorAdjustmentSuccessResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor Adjustment Success Response. |  -  |
**400** | Adjust Vendor Balance Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_create_on_demand_transfer**
> AdjustVendorBalanceResponse p_ges_create_on_demand_transfer(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, adjust_vendor_balance_request=adjust_vendor_balance_request)

Create On Demand Transfer

The Create On Demand Transfer API will create a new on-demand request either from to the merchant or from to the vendor.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.adjust_vendor_balance_request import AdjustVendorBalanceRequest
from cashfree_pg.models.adjust_vendor_balance_response import AdjustVendorBalanceResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    adjust_vendor_balance_request = {"transfer_from":"VENDOR","transfer_type":"ADJUSTMENT","transfer_amount":10,"remark":"Testing","tags":{"size":1,"product":"SHRT"}} # AdjustVendorBalanceRequest | Adjust Vendor Balance Request Body. (optional)

    try:
        # Create On Demand Transfer
        api_response = api_instance.p_ges_create_on_demand_transfer(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, adjust_vendor_balance_request=adjust_vendor_balance_request)
        print("The response of EasySplitApi->p_ges_create_on_demand_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_create_on_demand_transfer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **adjust_vendor_balance_request** | [**AdjustVendorBalanceRequest**](AdjustVendorBalanceRequest.md)| Adjust Vendor Balance Request Body. | [optional] 

### Return type

[**AdjustVendorBalanceResponse**](AdjustVendorBalanceResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adjust Vendor Balance Success Response. |  -  |
**400** | Adjust Vendor Balance Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_create_vendors**
> CreateVendorResponse p_ges_create_vendors(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, create_vendor_request=create_vendor_request)

Create vendor

Use this API to create a new vendor to your EasySplit account along with the KYC details. Provide KYC details such as account_type, business_type, gst, cin, pan, passport number and so on.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.create_vendor_request import CreateVendorRequest
from cashfree_pg.models.create_vendor_response import CreateVendorResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    create_vendor_request = {"vendor_id":"vendortest123","status":"ACTIVE","name":"customer","email":"johndoe@cashfree.com","phone":9876543210,"verify_account":true,"dashboard_access":true,"schedule_option":1,"bank":{"account_number":12345678890,"account_holder":"John Doe","ifsc":"HDFC019345"},"kyc_details":{"account_type":"BUSINESS","business_type":"NBFC","uidai":753624181019,"gst":"11AAAAA1111A1Z0","cin":"L00000Aa0000AaA000000","pan":"BIAPA2934N","passport_number":"L6892603"}} # CreateVendorRequest | Create Vendor Request Body. (optional)

    try:
        # Create vendor
        api_response = api_instance.p_ges_create_vendors(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, create_vendor_request=create_vendor_request)
        print("The response of EasySplitApi->p_ges_create_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_create_vendors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **create_vendor_request** | [**CreateVendorRequest**](CreateVendorRequest.md)| Create Vendor Request Body. | [optional] 

### Return type

[**CreateVendorResponse**](CreateVendorResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create Vendor Success Response. |  -  |
**400** | Create Vendor Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_download_vendors_docs**
> VendorDocumentDownloadResponse p_ges_download_vendors_docs(x_api_version, doc_type, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Download Vendor Documents

Use this API to download the uploaded KYC documents of that particular vendor. Provide the document type. Click the link from the sample request to download the KYC document.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.vendor_document_download_response import VendorDocumentDownloadResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    doc_type = 'doc_type_example' # str | Mention the document type that has to be downloaded. Only an uploaded document can be downloaded.
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Download Vendor Documents
        api_response = api_instance.p_ges_download_vendors_docs(x_api_version, doc_type, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of EasySplitApi->p_ges_download_vendors_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_download_vendors_docs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **doc_type** | **str**| Mention the document type that has to be downloaded. Only an uploaded document can be downloaded. | 
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**VendorDocumentDownloadResponse**](VendorDocumentDownloadResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Download Vendor Docs Success Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_fetch_vendors**
> VendorEntity p_ges_fetch_vendors(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Vendor All Details

Use this API to get the details of a specific vendor associated with your Easy Split account.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.vendor_entity import VendorEntity
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get Vendor All Details
        api_response = api_instance.p_ges_fetch_vendors(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of EasySplitApi->p_ges_fetch_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_fetch_vendors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**VendorEntity**](VendorEntity.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Vendor Success Response. |  -  |
**400** | Get Vendor Docs Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_get_vendor_balance**
> VendorBalance p_ges_get_vendor_balance(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get On Demand Balance

This API fetches the available amount with the merchant, vendor, and the unsettled amount for the merchant as well as the vendor.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.vendor_balance import VendorBalance
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get On Demand Balance
        api_response = api_instance.p_ges_get_vendor_balance(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of EasySplitApi->p_ges_get_vendor_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_get_vendor_balance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**VendorBalance**](VendorBalance.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Vendor Balance Success Response. |  -  |
**400** | Get Vendor Docs Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_get_vendor_balance_transfer_charges**
> VendorBalanceTransferCharges p_ges_get_vendor_balance_transfer_charges(x_api_version, amount, rate_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Vendor Balance Transfer Charges

This API returns the applicable service charge and service tax for a vendor balance transfer, based on the provided amount and rate type.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.vendor_balance_transfer_charges import VendorBalanceTransferCharges
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    amount = 1000 # float | Specify the amount for which you want to view the service charges and service taxes in the response.
    rate_type = 'VENDOR_ON_DEMAND' # str | Mention the type of rate for which you want to check the charges. Possible value: VENDOR_ON_DEMAND
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get Vendor Balance Transfer Charges
        api_response = api_instance.p_ges_get_vendor_balance_transfer_charges(x_api_version, amount, rate_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of EasySplitApi->p_ges_get_vendor_balance_transfer_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_get_vendor_balance_transfer_charges: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **amount** | **float**| Specify the amount for which you want to view the service charges and service taxes in the response. | 
 **rate_type** | **str**| Mention the type of rate for which you want to check the charges. Possible value: VENDOR_ON_DEMAND | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**VendorBalanceTransferCharges**](VendorBalanceTransferCharges.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Vendor Balance Transfer Charges Response. |  -  |
**400** | Get Vendor Balance Transfer Charges Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_get_vendors_docs**
> VendorDocumentsResponse p_ges_get_vendors_docs(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Vendor All Documents Status

Use this API to fetch the details of all the KYC details of a particular vendor.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.vendor_documents_response import VendorDocumentsResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get Vendor All Documents Status
        api_response = api_instance.p_ges_get_vendors_docs(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of EasySplitApi->p_ges_get_vendors_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_get_vendors_docs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**VendorDocumentsResponse**](VendorDocumentsResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Vendor Docs Success Response. |  -  |
**400** | Get Vendor Docs Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_order_recon**
> ESOrderReconResponse p_ges_order_recon(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, es_order_recon_request=es_order_recon_request)

Get Split and Settlement Details by OrderID v2.0

Use this API to get all the split details, settled and unsettled transactions details of each vendor who were part of a particular order by providing order Id or start date and end date.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.es_order_recon_request import ESOrderReconRequest
from cashfree_pg.models.es_order_recon_response import ESOrderReconResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    es_order_recon_request = {"filters":{"start_date":null,"end_date":null,"order_ids":["order_1527072afd7Hlp4lpVLiz7dj0P0i84r1X"]}} # ESOrderReconRequest | Get Split and Settlement Details by OrderID v2.0 (optional)

    try:
        # Get Split and Settlement Details by OrderID v2.0
        api_response = api_instance.p_ges_order_recon(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, es_order_recon_request=es_order_recon_request)
        print("The response of EasySplitApi->p_ges_order_recon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_order_recon: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **es_order_recon_request** | [**ESOrderReconRequest**](ESOrderReconRequest.md)| Get Split and Settlement Details by OrderID v2.0 | [optional] 

### Return type

[**ESOrderReconResponse**](ESOrderReconResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ES Order Recon Success Response. |  -  |
**400** | ES Order Recon Failure Response. |  -  |
**404** | ES Order Recon Failure Response. |  -  |
**409** | ES Order Recon Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_update_vendors**
> UpdateVendorResponse p_ges_update_vendors(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, update_vendor_request=update_vendor_request)

Update vendor Details

Use this API to edit the existing vendor details added to your EasySplit account. You can edit vendor details such as name, email, phone number, upi details, and any of the KYC details.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.update_vendor_request import UpdateVendorRequest
from cashfree_pg.models.update_vendor_response import UpdateVendorResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    update_vendor_request = {"status":"ACTIVE","name":"customer","email":"johndoe@cashfree.com","phone":9876543210,"verify_account":true,"dashboard_access":true,"schedule_option":1,"bank":{"account_number":12345678890,"account_holder":"John Doe","ifsc":"HDFC019345"},"kyc_details":{"account_type":"BUSINESS","business_type":"NBFC","uidai":753624181019,"gst":"11AAAAA1111A1Z0","cin":"L00000Aa0000AaA000000","pan":"BIAPA2934N","passport_number":"L6892603"}} # UpdateVendorRequest | Create Vendor Request Body. (optional)

    try:
        # Update vendor Details
        api_response = api_instance.p_ges_update_vendors(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, update_vendor_request=update_vendor_request)
        print("The response of EasySplitApi->p_ges_update_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_update_vendors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **update_vendor_request** | [**UpdateVendorRequest**](UpdateVendorRequest.md)| Create Vendor Request Body. | [optional] 

### Return type

[**UpdateVendorResponse**](UpdateVendorResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Vendor Success Response. |  -  |
**400** | Update Vendor Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ges_upload_vendors_docs**
> UploadVendorDocumentsResponse p_ges_upload_vendors_docs(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, doc_type=doc_type, doc_value=doc_value, file=file)

Upload Vendor Docs

Use this API to upload KYC documents of a specific vendor.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):
```python
import time
import os
import cashfree_pg
from cashfree_pg.models.upload_vendor_documents_response import UploadVendorDocumentsResponse
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XPartnerAPIKey
configuration.api_key['XPartnerAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerAPIKey'] = 'Bearer'

# Configure API key authorization: XClientSecret
configuration.api_key['XClientSecret'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSecret'] = 'Bearer'

# Configure API key authorization: XPartnerMerchantID
configuration.api_key['XPartnerMerchantID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XPartnerMerchantID'] = 'Bearer'

# Configure API key authorization: XClientID
configuration.api_key['XClientID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientID'] = 'Bearer'

# Configure API key authorization: XClientSignatureHeader
configuration.api_key['XClientSignatureHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XClientSignatureHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.EasySplitApi(api_client)
    x_api_version = '2025-01-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2025-01-01')
    vendor_id = 'your-vendor-id' # str | The id which uniquely identifies your vendor.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    doc_type = 'doc_type_example' # str | Mention the type of the document you are uploading. Possible values: UIDAI_FRONT, UIDAI_BACK, UIDAI_NUMBER, DL, DL_NUMBER, PASSPORT_FRONT, PASSPORT_BACK, PASSPORT_NUMBER, VOTER_ID, VOTER_ID_NUMBER, PAN, PAN_NUMBER, GST, GSTIN_NUMBER, CIN, CIN_NUMBER, NBFC_CERTIFICATE. If the doc type ends with a number you should add the doc value else upload the doc file. (optional)
    doc_value = 'doc_value_example' # str | Enter the display name of the uploaded file. (optional)
    file = None # bytearray | Select the document that should be uploaded or provide the path of that file. You cannot upload a file that is more than 2MB in size. (optional)

    try:
        # Upload Vendor Docs
        api_response = api_instance.p_ges_upload_vendors_docs(x_api_version, vendor_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, doc_type=doc_type, doc_value=doc_value, file=file)
        print("The response of EasySplitApi->p_ges_upload_vendors_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EasySplitApi->p_ges_upload_vendors_docs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2025-01-01&#39;]
 **vendor_id** | **str**| The id which uniquely identifies your vendor. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **doc_type** | **str**| Mention the type of the document you are uploading. Possible values: UIDAI_FRONT, UIDAI_BACK, UIDAI_NUMBER, DL, DL_NUMBER, PASSPORT_FRONT, PASSPORT_BACK, PASSPORT_NUMBER, VOTER_ID, VOTER_ID_NUMBER, PAN, PAN_NUMBER, GST, GSTIN_NUMBER, CIN, CIN_NUMBER, NBFC_CERTIFICATE. If the doc type ends with a number you should add the doc value else upload the doc file. | [optional] 
 **doc_value** | **str**| Enter the display name of the uploaded file. | [optional] 
 **file** | **bytearray**| Select the document that should be uploaded or provide the path of that file. You cannot upload a file that is more than 2MB in size. | [optional] 

### Return type

[**UploadVendorDocumentsResponse**](UploadVendorDocumentsResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload Vendor Docs Success Response. |  -  |
**400** | Upload Vendor Docs Failure Response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

