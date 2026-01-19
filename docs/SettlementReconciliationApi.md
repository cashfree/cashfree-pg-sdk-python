# cashfree_pg.SettlementReconciliationApi

All URIs are relative to *https://sandbox.cashfree.com/pg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_g_fetch_settlements**](SettlementReconciliationApi.md#p_g_fetch_settlements) | **POST** /settlements | Get All Settlements
[**p_g_settlement_fetch_recon**](SettlementReconciliationApi.md#p_g_settlement_fetch_recon) | **POST** /settlement/recon | Settlement Reconciliation


# **p_g_fetch_settlements**
> SettlementEntity p_g_fetch_settlements(x_api_version, fetch_settlements_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)

Get All Settlements

Use this API to get all settlement details by specifying the settlement ID, settlement UTR or date range.

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
from cashfree_pg.models.fetch_settlements_request import FetchSettlementsRequest
from cashfree_pg.models.settlement_entity import SettlementEntity
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
    api_instance = cashfree_pg.SettlementReconciliationApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    fetch_settlements_request = cashfree_pg.FetchSettlementsRequest() # FetchSettlementsRequest | Request Body to get the settlements
    content_type = 'application/json' # str | application/json (optional)
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    accept = 'application/json' # str | application/json (optional)

    try:
        # Get All Settlements
        api_response = api_instance.p_g_fetch_settlements(x_api_version, fetch_settlements_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)
        print("The response of SettlementReconciliationApi->p_g_fetch_settlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementReconciliationApi->p_g_fetch_settlements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **fetch_settlements_request** | [**FetchSettlementsRequest**](FetchSettlementsRequest.md)| Request Body to get the settlements | 
 **content_type** | **str**| application/json | [optional] 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **accept** | **str**| application/json | [optional] 

### Return type

[**SettlementEntity**](SettlementEntity.md)

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

# **p_g_settlement_fetch_recon**
> SettlementReconEntity p_g_settlement_fetch_recon(x_api_version, settlement_fetch_recon_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)

Settlement Reconciliation

- Use this API to get settlement reconciliation details using Settlement ID, settlement UTR or date range. - This API will return events for the settlement IDs you want 

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
from cashfree_pg.models.settlement_fetch_recon_request import SettlementFetchReconRequest
from cashfree_pg.models.settlement_recon_entity import SettlementReconEntity
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
    api_instance = cashfree_pg.SettlementReconciliationApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    settlement_fetch_recon_request = cashfree_pg.SettlementFetchReconRequest() # SettlementFetchReconRequest | Request Body for the settlement reconciliation
    content_type = 'application/json' # str | application/json (optional)
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = '47bf8872-46fe-11ee-be56-0242ac120002' # str | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    accept = 'application/json' # str | application/json (optional)

    try:
        # Settlement Reconciliation
        api_response = api_instance.p_g_settlement_fetch_recon(x_api_version, settlement_fetch_recon_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)
        print("The response of SettlementReconciliationApi->p_g_settlement_fetch_recon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementReconciliationApi->p_g_settlement_fetch_recon: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **settlement_fetch_recon_request** | [**SettlementFetchReconRequest**](SettlementFetchReconRequest.md)| Request Body for the settlement reconciliation | 
 **content_type** | **str**| application/json | [optional] 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **accept** | **str**| application/json | [optional] 

### Return type

[**SettlementReconEntity**](SettlementReconEntity.md)

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

