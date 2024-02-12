# TokenVault

Method | HTTP request | Description
------------- | ------------- | -------------
[**PGCustomerDeleteInstrument**](TokenVault.md#PGCustomerDeleteInstrument) | **Delete** /customers/{customer_id}/instruments/{instrument_id} | Delete Saved Card Instrument
[**PGCustomerFetchInstrument**](TokenVault.md#PGCustomerFetchInstrument) | **Get** /customers/{customer_id}/instruments/{instrument_id} | Fetch Specific Saved Card Instrument
[**PGCustomerFetchInstruments**](TokenVault.md#PGCustomerFetchInstruments) | **Get** /customers/{customer_id}/instruments | Fetch All Saved Card Instrument
[**PGCustomerInstrumentsFetchCryptogram**](TokenVault.md#PGCustomerInstrumentsFetchCryptogram) | **Get** /customers/{customer_id}/instruments/{instrument_id}/cryptogram | Fetch cryptogram for a saved card instrument



## PGCustomerDeleteInstrument

> PGCustomerDeleteInstrument(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, customer_id : Annotated[StrictStr, Field(..., description="Your Customer ID that you had sent during create order API `POST/orders`")] = None, instrument_id : Annotated[StrictStr, Field(..., description="The instrument_id which needs to be deleted")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Delete Saved Card Instrument ([Docs](https://docs.cashfree.com/reference/pgcustomerdeleteinstrument))

### Example

```python
try:
    api_response = Cashfree().PGCustomerDeleteInstrument(x_api_version="2022-09-01", customer_id="siddhesh_desai", instrument_id="54deabb4-ba45-4a60-9e6a-9c016fe7ab10")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**customerId** | **string*** | Your Customer ID that you had sent during create order API &#x60;POST/orders&#x60; | 
**instrumentId** | **string*** | The instrument_id which needs to be deleted | 
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response

```json
{
  "customer_id": "siddhesh_desai",
  "afa_reference": "740324562",
  "instrument_id": "54deabb4-ba45-4a60-9e6a-9c016fe7ab10",
  "instrument_type": "card",
  "instrument_uid": "0d8f70838cc5af8b1cd2bc0fe71278551fd3f1101e40020d89ad22ceba4f933c",
  "instrument_display": "xxxxxxxxxxxx4375",
  "instrument_status": "ACTIVE",
  "created_at": "2021-11-11 16:57:57",
  "instrument_meta": {
    "card_network": "VISA",
    "card_bank_name": "HDFC Bank Limited",
    "card_country": "IN",
    "card_type": "DEBIT_CARD",
    "card_token_details": {
      "par": "somepar",
      "expiry_month": "12",
      "expiry_year": "23"
    }
  }
}
```

## PGCustomerFetchInstrument

> PGCustomerFetchInstrument(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, customer_id : Annotated[StrictStr, Field(..., description="Your Customer ID that you had sent during create order API `POST/orders`")] = None, instrument_id : Annotated[StrictStr, Field(..., description="The instrument_id of the saved instrument which needs to be queried")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Fetch Specific Saved Card Instrument ([Docs](https://docs.cashfree.com/reference/pgcustomerfetchinstrument))



### Example

```python
try:
    api_response = Cashfree().PGCustomerFetchInstrument(x_api_version="2022-09-01", customer_id="siddhesh_desai", instrument_id="54deabb4-ba45-4a60-9e6a-9c016fe7ab10")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**customerId** | **string** | Your Customer ID that you had sent during create order API &#x60;POST/orders&#x60; | 
**instrumentId** | **string** | The instrument_id of the saved instrument which needs to be queried | 
**xApiVersion** | **string** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response
```json
{
  "customer_id": "siddhesh_desai",
  "afa_reference": "740324562",
  "instrument_id": "54deabb4-ba45-4a60-9e6a-9c016fe7ab10",
  "instrument_type": "card",
  "instrument_uid": "0d8f70838cc5af8b1cd2bc0fe71278551fd3f1101e40020d89ad22ceba4f933c",
  "instrument_display": "xxxxxxxxxxxx4375",
  "instrument_status": "ACTIVE",
  "created_at": "2021-11-11 16:57:57",
  "instrument_meta": {
    "card_network": "VISA",
    "card_bank_name": "HDFC Bank Limited",
    "card_country": "IN",
    "card_type": "DEBIT_CARD",
    "card_token_details": {
      "par": "somepar",
      "expiry_month": "12",
      "expiry_year": "23"
    }
  }
}
```

## PGCustomerFetchInstruments

> PGCustomerFetchInstruments(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, customer_id : Annotated[StrictStr, Field(..., description="Your Customer ID that you had sent during create order API `POST/orders`")] = None, instrument_type : Annotated[StrictStr, Field(..., description="Payment mode or type of saved instrument ")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Fetch All Saved Card Instrument ([Docs](https://docs.cashfree.com/reference/pgcustomerfetchinstruments))

### Example

```python
try:
    api_response = Cashfree().PGCustomerFetchInstruments(x_api_version="2022-09-01", customer_id="siddhesh_desai", instrument_type="card")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**customerId** | **string*** | Your Customer ID that you had sent during create order API &#x60;POST/orders&#x60; | 
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**instrumentType** | **string*** | Payment mode or type of saved instrument  | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response
```json
[
  {
  "customer_id": "siddhesh_desai",
  "afa_reference": "740324562",
  "instrument_id": "54deabb4-ba45-4a60-9e6a-9c016fe7ab10",
  "instrument_type": "card",
  "instrument_uid": "0d8f70838cc5af8b1cd2bc0fe71278551fd3f1101e40020d89ad22ceba4f933c",
  "instrument_display": "xxxxxxxxxxxx4375",
  "instrument_status": "ACTIVE",
  "created_at": "2021-11-11 16:57:57",
  "instrument_meta": {
    "card_network": "VISA",
    "card_bank_name": "HDFC Bank Limited",
    "card_country": "IN",
    "card_type": "DEBIT_CARD",
    "card_token_details": {
      "par": "somepar",
      "expiry_month": "12",
      "expiry_year": "23"
    }
  }
}
]
```


## PGCustomerInstrumentsFetchCryptogram

> PGCustomerInstrumentsFetchCryptogram(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, customer_id : Annotated[StrictStr, Field(..., description="Your Customer ID that you had sent during create order API `POST/orders`")] = None, instrument_id : Annotated[StrictStr, Field(..., description="The instrument_id of the saved card instrument which needs to be queried")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Fetch cryptogram for a saved card instrument ([Docs](https://docs.cashfree.com/reference/pgcustomerinstrumentsfetchcryptogram))



### Example

```python
try:
    api_response = Cashfree().PGCustomerInstrumentsFetchCryptogram(x_api_version="2022-09-01", customer_id="siddhesh_desai", instrument_id="54deabb4-ba45-4a60-9e6a-9c016fe7ab10")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**customerId** | **string*** | Your Customer ID that you had sent during create order API &#x60;POST/orders&#x60; | 
**instrumentId** | **string*** | The instrument_id of the saved card instrument which needs to be queried | 
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response

```json
{
  "instrument_id": "54deabb4-ba45-4a60-9e6a-9c016fe7ab10",
  "token_requestor_id": "22457512314",
  "card_number": "4491365621601472",
  "card_expiry_mm": "06",
  "card_expiry_yy": "2025",
  "cryptogram": "AQBBBBBBZatIlaIAmWKSghwBBBB=",
  "card_display": "1234"
}
```
