# PaymentLinks

Method | HTTP request | Description
------------- | ------------- | -------------
[**PGCancelLink**](PaymentLink.md#PGCancelLink) | **Post** /links/{link_id}/cancel | Cancel Payment Link
[**PGCreateLink**](PaymentLink.md#PGCreateLink) | **Post** /links | Create Payment Link
[**PGFetchLink**](PaymentLink.md#PGFetchLink) | **Get** /links/{link_id} | Fetch Payment Link Details
[**PGLinkFetchOrders**](PaymentLink.md#PGLinkFetchOrders) | **Get** /links/{link_id}/orders | Get Orders for a Payment Link



## PGCancelLink

> PGCancelLink(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, link_id : Annotated[StrictStr, Field(..., description="The payment link ID for which you want to view the details.")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Cancel Payment Link ([Docs](https://docs.cashfree.com/reference/pgcancellink))

### Example

```python
try:
    api_response = Cashfree().PGCancelLink(x_api_version="2022-09-01", link_id="go_sdk_link_01")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**linkId** | **string** | The payment link ID for which you want to view the details. | 
**xApiVersion** | **string** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response

```json
{
    "cf_link_id": 30111525,
    "link_id": "my_links_id_test",
    "link_status": "ACTIVE",
    "link_currency": "INR",
    "link_amount": 100,
    "link_amount_paid": 0,
    "link_partial_payments": true,
    "link_minimum_partial_amount": 20,
    "link_purpose": "Payment for PlayStation 11",
    "link_created_at": "2024-01-18T19:14:24+05:30",
    "customer_details": {
        "customer_name": "John Doe",
        "country_code": "+91",
        "customer_phone": "9999999999",
        "customer_email": "john@cashfree.com"
    },
    "link_meta": {
        "notify_url": "https://ee08e626ecd88c61c85f5c69c0418cb5.m.pipedream.net",
        "payment_methods": "",
        "return_url": "https://b8af79f41056.eu.ngrok.io",
        "upi_intent": "false"
    },
    "link_url": "https://payments.cashfree.com/links/z64lc99v754g",
    "link_expiry_time": "2024-10-14T15:04:05+05:30",
    "link_notes": {
        "key_1": "value_1",
        "key_2": "value_2"
    },
    "link_auto_reminders": false,
    "link_notify": {
        "send_email": true,
        "send_sms": false
    },
    "thank_you_msg": "",
    "terms_and_conditions": "",
    "enable_invoice": false
}
```


## PGCreateLink

> PGCreateLink(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, create_link_request : Annotated[CreateLinkRequest, Field(..., description="Request Body to Create Payment Links")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Create Payment Link ([Docs](https://docs.cashfree.com/reference/pgcreatelink))

### Example

```python
create_link_request = CreateLinkRequest(
    link_id="my_link_id",
    link_amount=30,
    link_currency="INR",
    link_purpose="A new product to sell",
    customer_details=LinkCustomerDetailsEntity(customer_phone="8908908901"),
    link_notify=LinkNotifyEntity(send_sms=True)
)
try:
    api_response = Cashfree().PGCreateLink(x_api_version="2022-09-01", create_link_request=create_link_request)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**createLinkRequest** | **CreateLinkRequest*** | Request Body to Create Payment Links | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response

```json
{
    "cf_link_id": 30111525,
    "link_id": "my_links_id_test",
    "link_status": "ACTIVE",
    "link_currency": "INR",
    "link_amount": 100,
    "link_amount_paid": 0,
    "link_partial_payments": true,
    "link_minimum_partial_amount": 20,
    "link_purpose": "Payment for PlayStation 11",
    "link_created_at": "2024-01-18T19:14:24+05:30",
    "customer_details": {
        "customer_name": "John Doe",
        "country_code": "+91",
        "customer_phone": "9999999999",
        "customer_email": "john@cashfree.com"
    },
    "link_meta": {
        "notify_url": "https://ee08e626ecd88c61c85f5c69c0418cb5.m.pipedream.net",
        "payment_methods": "",
        "return_url": "https://b8af79f41056.eu.ngrok.io",
        "upi_intent": "false"
    },
    "link_url": "https://payments.cashfree.com/links/z64lc99v754g",
    "link_expiry_time": "2024-10-14T15:04:05+05:30",
    "link_notes": {
        "key_1": "value_1",
        "key_2": "value_2"
    },
    "link_auto_reminders": false,
    "link_notify": {
        "send_email": true,
        "send_sms": false
    },
    "thank_you_msg": "",
    "terms_and_conditions": "",
    "enable_invoice": false
}
```


## PGFetchLink

> PGFetchLink(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, link_id : Annotated[StrictStr, Field(..., description="The payment link ID for which you want to view the details.")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Fetch Payment Link Details ([Docs](https://docs.cashfree.com/reference/pgfetchlink))

### Example

```python
try:
    api_response = Cashfree().PGFetchLink(x_api_version="2022-09-01", link_id="go_sdk_link_01")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**linkId** | **string*** | The payment link ID for which you want to view the details. | 
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response
```json
{
    "cf_link_id": 30111525,
    "link_id": "my_links_id_test",
    "link_status": "ACTIVE",
    "link_currency": "INR",
    "link_amount": 100,
    "link_amount_paid": 0,
    "link_partial_payments": true,
    "link_minimum_partial_amount": 20,
    "link_purpose": "Payment for PlayStation 11",
    "link_created_at": "2024-01-18T19:14:24+05:30",
    "customer_details": {
        "customer_name": "John Doe",
        "country_code": "+91",
        "customer_phone": "9999999999",
        "customer_email": "john@cashfree.com"
    },
    "link_meta": {
        "notify_url": "https://ee08e626ecd88c61c85f5c69c0418cb5.m.pipedream.net",
        "payment_methods": "",
        "return_url": "https://b8af79f41056.eu.ngrok.io",
        "upi_intent": "false"
    },
    "link_url": "https://payments.cashfree.com/links/z64lc99v754g",
    "link_expiry_time": "2024-10-14T15:04:05+05:30",
    "link_notes": {
        "key_1": "value_1",
        "key_2": "value_2"
    },
    "link_auto_reminders": false,
    "link_notify": {
        "send_email": true,
        "send_sms": false
    },
    "thank_you_msg": "",
    "terms_and_conditions": "",
    "enable_invoice": false
}
```


## PGLinkFetchOrders

> PGLinkFetchOrders(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, link_id : Annotated[StrictStr, Field(..., description="The payment link ID for which you want to view the details.")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Orders for a Payment Link ([Docs](https://docs.cashfree.com/reference/pglinkfetchorders))



### Example

```python
try:
    api_response = Cashfree().PGLinkFetchOrders(x_api_version="2022-09-01", link_id="go_sdk_link_01")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**linkId** | **string*** | The payment link ID for which you want to view the details. | 
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response
```json
[
  {
    "cf_order_id": 2149460581,
    "created_at": "2023-08-11T18:02:46+05:30",
    "customer_details": {
      "customer_id": "409128494",
      "customer_name": "Johmn Doe",
      "customer_email": "pmlpayme@ntsas.com",
      "customer_phone": "9876543210"
    },
    "entity": "order",
    "order_amount": 22,
    "order_currency": "INR",
    "order_expiry_time": "2023-09-09T18:02:46+05:30",
    "order_id": "order_3242Tq4Edj9CC5RDcMeobmJOWOBJij",
    "order_meta": {
      "return_url": "https://example.com/return/{order_id}",
      "notify_url": "https://example.com/notify",
      "payment_methods": "cc"
    },
    "order_note": "some order note LIST",
    "order_splits": [],
    "order_status": "ACTIVE",
    "order_tags": {
      "name": "John",
      "age": "19"
    },
    "payment_session_id": "session_a1VXIPJo8kh7IBigVXX8LgTMupQW_cu25FS8KwLwQLOmiHqbBxq5UhEilrhbDSKKHA6UAuOj9506aaHNlFAHEqYrHSEl9AVtYQN9LIIc4vkH",
    "payments": {
      "url": "https://sandbox.cashfree.com/pg/orders/order_3242Tq4Edj9CC5RDcMeobmJOWOBJij/payments"
    },
    "refunds": {
      "url": "https://sandbox.cashfree.com/pg/orders/order_3242Tq4Edj9CC5RDcMeobmJOWOBJij/refunds"
    },
    "settlements": {
      "url": "https://sandbox.cashfree.com/pg/orders/order_3242Tq4Edj9CC5RDcMeobmJOWOBJij/settlements"
    },
    "terminal_data": null
  }
]
```
