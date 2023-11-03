# cashfree_pg.SettlementReconciliationApi

All URIs are relative to *https://sandbox.cashfree.com/pg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PGFetchSettlements**](SettlementReconciliationApi.md#PGFetchSettlements) | **POST** /settlements | Get All Settlements
[**PGSettlementFetchRecon**](SettlementReconciliationApi.md#PGSettlementFetchRecon) | **POST** /settlement/recon | Settlement Reconciliation


# **PGFetchSettlements**
> SettlementEntity PGFetchSettlements(x_api_version, fetch_settlements_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)

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


    Cashfree.XClientId = "<x-client-id>"
    Cashfree.XClientSecret = "<x-client-secret>"
    Cashfree.XEnvironment = Cashfree.Sandbox
    x_api_version = "2022-09-01"

    try:
        # Get All Settlements
        api_response = Cashfree().PGFetchSettlements(x_api_version, fetch_settlements_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)
        print("The response of SettlementReconciliationApi->PGFetchSettlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementReconciliationApi->PGFetchSettlements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2022-09-01&#39;]
 **fetch_settlements_request** | [**FetchSettlementsRequest**](FetchSettlementsRequest.md)| Request Body to get the settlements | 
 **content_type** | **str**| application/json | [optional] 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| Idempotency works by saving the resulting status code and body of the first request made for any given idempotency key, regardless of whether it succeeded or failed. Subsequent requests with the same key return the same result, including 500 errors.  Currently supported on all POST calls that uses x-client-id &amp; x-client-secret. To use enable, pass x-idempotency-key in the request header. The value of this header must be unique to each operation you are trying to do. One example can be to use the same order_id that you pass while creating orders   | [optional] 
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

# **PGSettlementFetchRecon**
> SettlementReconEntity PGSettlementFetchRecon(x_api_version, settlement_fetch_recon_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)

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


    Cashfree.XClientId = "<x-client-id>"
    Cashfree.XClientSecret = "<x-client-secret>"
    Cashfree.XEnvironment = Cashfree.Sandbox
    x_api_version = "2022-09-01"

    try:
        # Settlement Reconciliation
        api_response = Cashfree().PGSettlementFetchRecon(x_api_version, settlement_fetch_recon_request, content_type=content_type, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, accept=accept)
        print("The response of SettlementReconciliationApi->PGSettlementFetchRecon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementReconciliationApi->PGSettlementFetchRecon: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2022-09-01&#39;]
 **settlement_fetch_recon_request** | [**SettlementFetchReconRequest**](SettlementFetchReconRequest.md)| Request Body for the settlement reconciliation | 
 **content_type** | **str**| application/json | [optional] 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| Idempotency works by saving the resulting status code and body of the first request made for any given idempotency key, regardless of whether it succeeded or failed. Subsequent requests with the same key return the same result, including 500 errors.  Currently supported on all POST calls that uses x-client-id &amp; x-client-secret. To use enable, pass x-idempotency-key in the request header. The value of this header must be unique to each operation you are trying to do. One example can be to use the same order_id that you pass while creating orders   | [optional] 
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

