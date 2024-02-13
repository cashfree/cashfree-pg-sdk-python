# Eligibility

Method | HTTP request | Description
------------- | ------------- | -------------
[**PGEligibilityFetchCardlessEMI**](Eligibility.md#PGEligibilityFetchCardlessEMI) | **Post** /eligibility/cardlessemi | Get Eligible Cardless EMI
[**PGEligibilityFetchOffers**](Eligibility.md#PGEligibilityFetchOffers) | **Post** /eligibility/offers | Get Eligible Offers
[**PGEligibilityFetchPaylater**](Eligibility.md#PGEligibilityFetchPaylater) | **Post** /eligibility/paylater | Get Eligible Paylater
[**PGEligibilityFetchPaymentMethods**](Eligibility.md#PGEligibilityFetchPaymentMethods) | **Post** /eligibility/payment_methods | Get Eligible Payment Methods



## PGEligibilityFetchCardlessEMI

> PGEligibilityFetchCardlessEmi(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, eligibility_fetch_cardless_emi_request : Annotated[EligibilityFetchCardlessEMIRequest, Field(..., description="Request Body to get eligible cardless emi options for a customer and order")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Eligible Cardless EMI ([Docs](https://docs.cashfree.com/reference/pgeligibilityfetchcardlessemi))

### Example

```python
eligibility_fetch_cardless_emi_request = EligibilityFetchCardlessEMIRequest(
    queries=CardlessEMIQueries(
        amount=1000.00, 
        customer_details=CustomerDetailsCardlessEMI(customer_phone="8908908901")
    )
)
try:
    api_response = Cashfree().PGEligibilityFetchCardlessEmi(x_api_version="2022-09-01", eligibility_fetch_cardless_emi_request=eligibility_fetch_cardless_emi_request)
    print(api_response.data)
except Exception as e:
    print(e)
```

###  Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**eligibilityFetchCardlessEMIRequest** | [**EligibilityFetchCardlessEMIRequest***](Eligibility.md#EligibilityFetchCardlessEMIRequest) | Request Body to get eligible cardless emi options for a customer and order | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree |

### Response

```json
[
  {
    "eligibility": true,
    "entity_type": "cardlessemi",
    "entity_value": "idfc",
    "entity_details": {
      "payment_method": "idfc",
      "emi_plans": [
        {
          "tenure": 1,
          "interest_rate": 10,
          "currency": "INR",
          "emi": 400,
          "total_interest": 10,
          "total_amount": 40
        }
      ]
    }
  }
]
```

## PGEligibilityFetchOffers

> PGEligibilityFetchOffers(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, eligibility_fetch_offers_request : Annotated[EligibilityFetchOffersRequest, Field(..., description="Request Body to get eligible offers for a customer and order")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Eligible Offers ([Docs](https://docs.cashfree.com/reference/pgeligibilityfetchoffers))

### Example

```python
eligibility_fetch_offers_request = EligibilityFetchOffersRequest(
    queries=OfferQueries(amount=1000.00)
)
try:
    api_response = Cashfree().PGEligibilityFetchOffers(x_api_version="2022-09-01", eligibility_fetch_offers_request=eligibility_fetch_offers_request)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**eligibilityFetchOffersRequest** | [**EligibilityFetchOffersRequest***](EligibilityFetchOffersRequest.md) | Request Body to get eligible offers for a customer and order | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 

### Response

```json
[
  {
    "offer_id": "d2b430fb-1afe-455a-af31-66d00377b29a",
    "offer_status": "active",
    "offer_meta": {
      "offer_title": "some title",
      "offer_description": "some offer description",
      "offer_code": "CFTESTOFFER",
      "offer_start_time": "2023-03-21T08:09:51Z",
      "offer_end_time": "2023-03-29T08:09:51Z"
    },
    "offer_tnc": {
      "offer_tnc_type": "text",
      "offer_tnc_value": "TnC for the Offer."
    },
    "offer_details": {
      "offer_type": "DISCOUNT_AND_CASHBACK",
      "discount_details": {
        "discount_type": "flat",
        "discount_value": "10",
        "max_discount_amount": "10"
      },
      "cashback_details": {
        "cashback_type": "percentage",
        "cashback_value": "20",
        "max_cashback_amount": "150"
      }
    },
    "offer_validations": {
      "min_amount": 10,
      "payment_method": {
        "wallet": {
          "issuer": "paytm"
        }
      },
      "max_allowed": 2
    }
  }
]
```


## PGEligibilityFetchPaylater

> PGEligibilityFetchPaylater(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, eligibility_fetch_paylater_request : Annotated[EligibilityFetchPaylaterRequest, Field(..., description="Request Body to get eligible paylater options for a customer and order")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Eligible Paylater ([Docs](https://docs.cashfree.com/reference/pgeligibilityfetchpaylater))



### Example

```python
eligibility_fetch_paylater_request = EligibilityFetchPaylaterRequest(
    queries=CardlessEMIQueries(
        amount=1000.00, 
        customer_details=CustomerDetailsCardlessEMI(customer_phone="8908908901")
    )
)
try:
    api_response = Cashfree().PGEligibilityFetchPaylater(x_api_version="2022-09-01", eligibility_fetch_paylater_request=eligibility_fetch_paylater_request)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**eligibilityFetchPaylaterRequest** | [**EligibilityFetchPaylaterRequest***](EligibilityFetchPaylaterRequest.md) | Request Body to get eligible paylater options for a customer and order | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 

### Response

```json
[
  {
    "eligibility": true,
    "entity_type": "paylater",
    "entity_value": "olapostpaid",
    "entity_details": {
      "payment_method": "olapostpaid"
    }
  }
]
```


## PGEligibilityFetchPaymentMethods

> PGEligibilityFetchPaymentMethods(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, eligibility_fetch_payment_methods_request : Annotated[EligibilityFetchPaymentMethodsRequest, Field(..., description="Request Body to get eligible payment methods for an account and order")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Eligible Payment Methods ([Docs](https://docs.cashfree.com/reference/pgeligibilityfetchpaymentmethods))



### Example

```python
eligibility_fetch_payment_methods_request = EligibilityFetchPaymentMethodsRequest(
    queries=PaymentMethodsQueries(amount=1000.00)
)
try:
    api_response = Cashfree().PGEligibilityFetchPaymentMethods(x_api_version="2022-09-01", eligibility_fetch_payment_methods_request=eligibility_fetch_payment_methods_request)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**eligibilityFetchPaymentMethodsRequest** | [**EligibilityFetchPaymentMethodsRequest***](EligibilityFetchPaymentMethodsRequest.md) | Request Body to get eligible payment methods for an account and order | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 

### Response
```json
[
  {
    "eligibility": true,
    "entity_type": "payment_methods",
    "entity_value": "netbanking",
    "entity_details": {
      "payment_method_details": [
        {
          "nick": "motak_kahindra_bank",
          "display": "Motak Kahindra Bank",
          "eligibility": true,
          "code": 3032
        },
        {
          "nick": "bank_of_india",
          "display": "Bank Of India",
          "eligibility": true,
          "code": 3031
        }
      ]
    }
  }
]
```
