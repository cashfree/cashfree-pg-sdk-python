# cashfree_pg.OrdersApi

All URIs are relative to *https://sandbox.cashfree.com/pg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_g_create_order**](OrdersApi.md#p_g_create_order) | **POST** /orders | Create Order
[**p_g_fetch_order**](OrdersApi.md#p_g_fetch_order) | **GET** /orders/{order_id} | Get Order
[**p_g_fetch_order_extended_data**](OrdersApi.md#p_g_fetch_order_extended_data) | **GET** /orders/{order_id}/extended | Get Order Extended
[**p_g_terminate_order**](OrdersApi.md#p_g_terminate_order) | **PATCH** /orders/{order_id} | Terminate Order
[**p_g_update_order_extended_data**](OrdersApi.md#p_g_update_order_extended_data) | **PUT** /orders/{order_id}/extended | Update Order Extended


# **p_g_create_order**
> OrderEntity p_g_create_order(x_api_version, create_order_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Create Order

### Order An order is an entity which has a amount and currency associated with it. It is something for which you want to collect payment for. Use this API to create orders with Cashfree from your backend to get a `payment_sessions_id`.  You can use the `payment_sessions_id` to create a transaction for the order. 

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
from cashfree_pg.models.create_order_request import CreateOrderRequest
from cashfree_pg.models.order_entity import OrderEntity
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
    api_instance = cashfree_pg.OrdersApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    create_order_request = cashfree_pg.CreateOrderRequest() # CreateOrderRequest | Request body to create an order at cashfree
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Create Order
        api_response = api_instance.p_g_create_order(x_api_version, create_order_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of OrdersApi->p_g_create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->p_g_create_order: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **create_order_request** | [**CreateOrderRequest**](CreateOrderRequest.md)| Request body to create an order at cashfree | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**OrderEntity**](OrderEntity.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**401** | Authentication Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**409** | Resource already present |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**422** | Idempotency error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_g_fetch_order**
> OrderEntity p_g_fetch_order(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Order

Use this API to fetch the order that was created at Cashfree's using the `order_id`.  ## When to use this API - To check the status of your order - Once the order is PAID - Once your customer returns to `return_url` 

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
from cashfree_pg.models.order_entity import OrderEntity
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
    api_instance = cashfree_pg.OrdersApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    order_id = 'your-order-id' # str | The id which uniquely identifies your order
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get Order
        api_response = api_instance.p_g_fetch_order(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of OrdersApi->p_g_fetch_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->p_g_fetch_order: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **order_id** | **str**| The id which uniquely identifies your order | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**OrderEntity**](OrderEntity.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**401** | Authentication Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**409** | Resource already present |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**422** | Idempotency error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_g_fetch_order_extended_data**
> OrderExtendedDataEntity p_g_fetch_order_extended_data(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Order Extended

Use this API to fetch the order related data like address,cart,offers,customer details etc using the Cashfree's `order_id`. ## When to use this API - To get the extended data associated with order. - Once the order is PAID - Once your customer returns to `return_url` 

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
from cashfree_pg.models.order_extended_data_entity import OrderExtendedDataEntity
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
    api_instance = cashfree_pg.OrdersApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    order_id = 'your-order-id' # str | The id which uniquely identifies your order
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get Order Extended
        api_response = api_instance.p_g_fetch_order_extended_data(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of OrdersApi->p_g_fetch_order_extended_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->p_g_fetch_order_extended_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **order_id** | **str**| The id which uniquely identifies your order | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**OrderExtendedDataEntity**](OrderExtendedDataEntity.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**401** | Authentication Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**409** | Resource already present |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**422** | Idempotency error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_g_terminate_order**
> OrderEntity p_g_terminate_order(x_api_version, order_id, terminate_order_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Terminate Order

Use this API to terminate the order that was created at Cashfree's using the `order_id`.

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
from cashfree_pg.models.order_entity import OrderEntity
from cashfree_pg.models.terminate_order_request import TerminateOrderRequest
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
    api_instance = cashfree_pg.OrdersApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    order_id = 'your-order-id' # str | The id which uniquely identifies your order
    terminate_order_request = cashfree_pg.TerminateOrderRequest() # TerminateOrderRequest | Request body to terminate an order at cashfree
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Terminate Order
        api_response = api_instance.p_g_terminate_order(x_api_version, order_id, terminate_order_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of OrdersApi->p_g_terminate_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->p_g_terminate_order: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **order_id** | **str**| The id which uniquely identifies your order | 
 **terminate_order_request** | [**TerminateOrderRequest**](TerminateOrderRequest.md)| Request body to terminate an order at cashfree | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**OrderEntity**](OrderEntity.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**401** | Authentication Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**409** | Resource already present |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**422** | Idempotency error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_g_update_order_extended_data**
> UpdateOrderExtendedDataEntity p_g_update_order_extended_data(x_api_version, order_id, update_order_extended_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Update Order Extended

Use this api to update the order related data like shipment details,order delivery status etc. ## When to use this API - To provide/update the shipment details or order delivery status. - Once the order is PAID. 

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
from cashfree_pg.models.update_order_extended_data_entity import UpdateOrderExtendedDataEntity
from cashfree_pg.models.update_order_extended_request import UpdateOrderExtendedRequest
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
    api_instance = cashfree_pg.OrdersApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    order_id = 'your-order-id' # str | The id which uniquely identifies your order
    update_order_extended_request = cashfree_pg.UpdateOrderExtendedRequest() # UpdateOrderExtendedRequest | Request Body to Update extended data related to order
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Update Order Extended
        api_response = api_instance.p_g_update_order_extended_data(x_api_version, order_id, update_order_extended_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of OrdersApi->p_g_update_order_extended_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->p_g_update_order_extended_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **order_id** | **str**| The id which uniquely identifies your order | 
 **update_order_extended_request** | [**UpdateOrderExtendedRequest**](UpdateOrderExtendedRequest.md)| Request Body to Update extended data related to order | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**UpdateOrderExtendedDataEntity**](UpdateOrderExtendedDataEntity.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**401** | Authentication Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**409** | Resource already present |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**422** | Idempotency error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

