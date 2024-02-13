# Settlements

Method | HTTP request | Description
------------- | ------------- | -------------
[**PGOrderFetchSettlement**](Settlements.md#PGOrderFetchSettlement) | **Get** /orders/{order_id}/settlements | Get Settlements by Order ID



## PGOrderFetchSettlement

> PGOrderFetchSettlement(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, order_id : Annotated[StrictStr, Field(..., description="The id which uniquely identifies your order")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Settlements by Order ID ([Docs](https://docs.cashfree.com/reference/pgorderfetchsettlement)

### Example

```python
try:
    api_response = Cashfree().PGOrderFetchSettlement(x_api_version="2022-09-01", order_id="order_342bAHtHiGpa2XePHbvRdu22S7p8U")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**orderId** | **string** | The id which uniquely identifies your order | 
**xApiVersion** | **string** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response

```json
{
  "cf_payment_id": 553338,
  "order_id": "order-12-127",
  "entity": "settlement",
  "order_amount": 100,
  "payment_time": "2021-07-13T13:13:59+05:30",
  "service_charge": 10,
  "service_tax": 1.8,
  "settlement_amount": 88.2,
  "cf_settlement_id": 6121238,
  "transfer_id": 238,
  "transfer_time": "2021-07-25T12:57:52+05:30",
  "transfer_utr": "N87912312",
  "order_currency": "INR",
  "settlement_currency": "INR"
}
```
