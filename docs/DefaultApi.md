# cashfree_pg.DefaultApi

All URIs are relative to *https://sandbox.cashfree.com/pg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_create_qr_codes**](DefaultApi.md#terminal_create_qr_codes) | **POST** /partners/merchant/qrcodes | Create Pre-Activated Vpas for partner
[**terminal_get_qr_codes**](DefaultApi.md#terminal_get_qr_codes) | **GET** /partners/merchant/qrcodes | Get Pre-Activated Vpas for partner


# **terminal_create_qr_codes**
> List[StaticQrResponseEntity] terminal_create_qr_codes(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, create_partner_vpa_request=create_partner_vpa_request)

Create Pre-Activated Vpas for partner

Use this API to create a pre-activated vpa for partner.

### Example


```python
import cashfree_pg
from cashfree_pg.models.create_partner_vpa_request import CreatePartnerVpaRequest
from cashfree_pg.models.static_qr_response_entity import StaticQrResponseEntity
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)


# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.DefaultApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = 47bf8872-46fe-11ee-be56-0242ac120002 # UUID | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)
    create_partner_vpa_request = cashfree_pg.CreatePartnerVpaRequest() # CreatePartnerVpaRequest |  (optional)

    try:
        # Create Pre-Activated Vpas for partner
        api_response = api_instance.terminal_create_qr_codes(x_api_version, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key, create_partner_vpa_request=create_partner_vpa_request)
        print("The response of DefaultApi->terminal_create_qr_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->terminal_create_qr_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **UUID**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 
 **create_partner_vpa_request** | [**CreatePartnerVpaRequest**](CreatePartnerVpaRequest.md)|  | [optional] 

### Return type

[**List[StaticQrResponseEntity]**](StaticQrResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Invalid Partner API Key |  -  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**409** | Resource already present |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**422** | Idempotency error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_get_qr_codes**
> List[StaticQrResponseEntity] terminal_get_qr_codes(x_api_version, status, cf_terminal_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)

Get Pre-Activated Vpas for partner

Use this API to get a pre-activated vpa for partner.

### Example


```python
import cashfree_pg
from cashfree_pg.models.static_qr_response_entity import StaticQrResponseEntity
from cashfree_pg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = cashfree_pg.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)


# Enter a context with an instance of the API client
with cashfree_pg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cashfree_pg.DefaultApi(api_client)
    x_api_version = '2023-08-01' # str | API version to be used. Format is in YYYY-MM-DD (default to '2023-08-01')
    status = 'MAPPED' # str | Status of pre-created Qr.
    cf_terminal_id = '123344' # str | Cashfree terminal id for which you want to get pre-generated staticQRs.
    x_request_id = '4dfb9780-46fe-11ee-be56-0242ac120002' # str | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree (optional)
    x_idempotency_key = 47bf8872-46fe-11ee-be56-0242ac120002 # UUID | An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   (optional)

    try:
        # Get Pre-Activated Vpas for partner
        api_response = api_instance.terminal_get_qr_codes(x_api_version, status, cf_terminal_id, x_request_id=x_request_id, x_idempotency_key=x_idempotency_key)
        print("The response of DefaultApi->terminal_get_qr_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->terminal_get_qr_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| API version to be used. Format is in YYYY-MM-DD | [default to &#39;2023-08-01&#39;]
 **status** | **str**| Status of pre-created Qr. | 
 **cf_terminal_id** | **str**| Cashfree terminal id for which you want to get pre-generated staticQRs. | 
 **x_request_id** | **str**| Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | [optional] 
 **x_idempotency_key** | **UUID**| An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.   | [optional] 

### Return type

[**List[StaticQrResponseEntity]**](StaticQrResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Invalid Partner API Key |  -  |
**400** | Bad request error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**404** | Resource Not found |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**409** | Resource already present |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**422** | Idempotency error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**429** | Rate Limit Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |
**500** | API related Error |  * x-api-version -  <br>  * x-ratelimit-limit -  <br>  * x-ratelimit-remaining -  <br>  * x-ratelimit-retry -  <br>  * x-ratelimit-type -  <br>  * x-request-id -  <br>  * x-idempotency-key -  <br>  * x-idempotency-replayed -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

