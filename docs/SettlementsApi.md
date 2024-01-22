# cashfree_pg.SettlementsApi

All URIs are relative to *https://sandbox.cashfree.com/pg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PGOrderFetchSettlement**](SettlementsApi.md#PGOrderFetchSettlement) | **GET** /orders/{order_id}/settlements | Get Settlements by Order ID


# **PGOrderFetchSettlement**
> SettlementEntity PGOrderFetchSettlement(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Settlements by Order ID

Use this API to view all the settlements of a particular order.

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
from cashfree_pg.models.settlement_entity import SettlementEntity
from cashfree_pg.rest import ApiException
from pprint import pprint


    Cashfree.XClientId = "<x-client-id>"
    Cashfree.XClientSecret = "<x-client-secret>"
    Cashfree.XEnvironment = Cashfree.Sandbox
    x_api_version = "2022-09-01"

    try:
        # Get Settlements by Order ID
        api_response = Cashfree().PGOrderFetchSettlement(x_api_version, order_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of SettlementsApi->PGOrderFetchSettlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementsApi->PGOrderFetchSettlement: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **order_id** | **str**| The id which uniquely identifies your order | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **str**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**SettlementEntity**](SettlementEntity.md)

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
**502** | Bank related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

