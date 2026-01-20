# cashfree_pg.SimulationApi

All URIs are relative to *https://sandbox.cashfree.com/pg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_g_fetch_simulation**](SimulationApi.md#p_g_fetch_simulation) | **GET** /simulate/{simulation_id} | Fetch Simulation
[**p_g_simulate_payment**](SimulationApi.md#p_g_simulate_payment) | **POST** /simulate | Simulate Payment


# **p_g_fetch_simulation**
> SimulationResponse p_g_fetch_simulation(x_api_version, simulation_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Fetch Simulation

Use this API to fetch simulated payment details.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):

```python
import cashfree_pg
from cashfree_pg.models.simulation_response import SimulationResponse
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
    api_instance = cashfree_pg.SimulationApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    simulation_id = 'sim_2900842gV18Lhh7owswLj5XF0uHHUn1CX' # str | Provide the SimulationId for which the details have to be fetched.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = 47bf8872-46fe-11ee-be56-0242ac120002 # UUID | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Fetch Simulation
        api_response = api_instance.p_g_fetch_simulation(x_api_version, simulation_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of SimulationApi->p_g_fetch_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationApi->p_g_fetch_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **simulation_id** | **str**| Provide the SimulationId for which the details have to be fetched. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **UUID**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**SimulationResponse**](SimulationResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched Simulated Response |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**401** | Authentication Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_g_simulate_payment**
> SimulationResponse p_g_simulate_payment(x_api_version, simulate_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Simulate Payment

Use this API to simulate payment. To use this API you should first create an order using the Create Order API. Also, you need to create a payment with the same order.

### Example

* Api Key Authentication (XPartnerAPIKey):
* Api Key Authentication (XClientSecret):
* Api Key Authentication (XPartnerMerchantID):
* Api Key Authentication (XClientID):
* Api Key Authentication (XClientSignatureHeader):

```python
import cashfree_pg
from cashfree_pg.models.simulate_request import SimulateRequest
from cashfree_pg.models.simulation_response import SimulationResponse
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
    api_instance = cashfree_pg.SimulationApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    simulate_request = {"entity":"PAYMENTS","entity_id":"14934289844","entity_simulation":{"payment_status":"FAILED","payment_error_code":"ISSUER_NOT_AVAILABLE"}} # SimulateRequest | Request Body to Make Simulation
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = 47bf8872-46fe-11ee-be56-0242ac120002 # UUID | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Simulate Payment
        api_response = api_instance.p_g_simulate_payment(x_api_version, simulate_request, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of SimulationApi->p_g_simulate_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationApi->p_g_simulate_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **simulate_request** | [**SimulateRequest**](SimulateRequest.md)| Request Body to Make Simulation | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **UUID**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**SimulationResponse**](SimulationResponse.md)

### Authorization

[XPartnerAPIKey](../README.md#XPartnerAPIKey), [XClientSecret](../README.md#XClientSecret), [XPartnerMerchantID](../README.md#XPartnerMerchantID), [XClientID](../README.md#XClientID), [XClientSignatureHeader](../README.md#XClientSignatureHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment Simulated Response |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**401** | Authentication Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

