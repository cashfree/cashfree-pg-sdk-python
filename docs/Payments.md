# Payments

Method | HTTP request | Description
------------- | ------------- | -------------
[**PGOrderFetchPayment**](Payments.md#PGOrderFetchPayment) | **Get** /orders/{order_id}/payments/{cf_payment_id} | Get Payment by ID
[**PGOrderFetchPayments**](Payments.md#PGOrderFetchPayments) | **Get** /orders/{order_id}/payments | Get Payments for an Order
[**PGPayOrder**](Payments.md#PGPayOrder) | **Post** /orders/sessions | Order Pay
[**PGAuthorizeOrder**](Payments.md#PGAuthorizeOrder) | **Post** /orders/{order_id}/authorization | Preauthorization
[**PGOrderAuthenticatePayment**](Payments.md#PGOrderAuthenticatePayment) | **Post** /orders/pay/authenticate/{cf_payment_id} | Submit or Resend OTP


## PGOrderFetchPayment

> PGOrderFetchPayment(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, order_id : Annotated[StrictStr, Field(..., description="The id which uniquely identifies your order")] = None, cf_payment_id : Annotated[StrictStr, Field(..., description="The Cashfree payment or transaction ID.")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Payment by ID ([Docs](https://docs.cashfree.com/reference/pgorderfetchpayment))



### Example

```python
try:
    api_response = Cashfree().PGOrderFetchPayment(x_api_version="2022-09-01", order_id="order_342bAHtHiGpa2XePHbvRdu22S7p8U", cf_payment_id="14910259396")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**orderId** | **string*** | The id which uniquely identifies your order | 
**cfPaymentId** | **string*** | The Cashfree payment or transaction ID. | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response
```json
{
  "cf_payment_id": 12376123,
  "order_id": "order_8123",
  "entity": "payment",
  "payment_currency": "INR",
  "error_details": null,
  "order_amount": 10.01,
  "is_captured": true,
  "payment_group": "upi",
  "authorization": {
    "action": "CAPTURE",
    "status": "PENDING",
    "captured_amount": 100,
    "start_time": "2022-02-09T18:04:34+05:30",
    "end_time": "2022-02-19T18:04:34+05:30",
    "approve_by": "2022-02-09T18:04:34+05:30",
    "action_reference": "6595231908096894505959",
    "action_time": "2022-08-03T16:09:51"
  },
  "payment_method": {
    "upi": {
      "channel": "collect",
      "upi_id": "rohit@xcxcx"
    }
  },
  "payment_amount": 10.01,
  "payment_time": "2021-07-23T12:15:06+05:30",
  "payment_completion_time": "2021-07-23T12:18:59+05:30",
  "payment_status": "SUCCESS",
  "payment_message": "Transaction successful",
  "bank_reference": "P78112898712",
  "auth_id": "A898101"
}
```



## PGOrderFetchPayments

> PGOrderFetchPayments(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, order_id : Annotated[StrictStr, Field(..., description="The id which uniquely identifies your order")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Get Payments for an Order ([Docs](https://docs.cashfree.com/reference/pgorderfetchpayments))



### Example

```python
try:
    api_response = Cashfree().PGOrderFetchPayments(x_api_version="2022-09-01", order_id="order_342bAHtHiGpa2XePHbvRdu22S7p8U")
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**xApiVersion** | **string*** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**orderId** | **string*** | The id which uniquely identifies your order | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response
```json
[
  {
    "cf_payment_id": 12376123,
    "order_id": "order_8123",
    "entity": "payment",
    "payment_currency": "INR",
    "error_details": null,
    "order_amount": 10.01,
    "is_captured": true,
    "payment_group": "upi",
    "authorization": {
      "action": "CAPTURE",
      "status": "PENDING",
      "captured_amount": 100,
      "start_time": "2022-02-09T18:04:34+05:30",
      "end_time": "2022-02-19T18:04:34+05:30",
      "approve_by": "2022-02-09T18:04:34+05:30",
      "action_reference": "6595231908096894505959",
      "action_time": "2022-08-03T16:09:51"
    },
    "payment_method": {
      "upi": {
        "channel": "collect",
        "upi_id": "rohit@xcxcx"
      }
    },
    "payment_amount": 10.01,
    "payment_time": "2021-07-23T12:15:06+05:30",
    "payment_completion_time": "2021-07-23T12:18:59+05:30",
    "payment_status": "SUCCESS",
    "payment_message": "Transaction successful",
    "bank_reference": "P78112898712",
    "auth_id": "A898101"
  },
  {
    "cf_payment_id": 12376124,
    "order_id": "order_8123",
    "entity": "payment",
    "payment_currency": "INR",
    "error_details": {
      "error_code": "TRANSACTION_DECLINED",
      "error_description": "issuer bank or payment service provider declined the transaction",
      "error_reason": "auth_declined",
      "error_source": "customer"
    },
    "order_amount": 10.01,
    "is_captured": true,
    "payment_group": "credit_card",
    "authorization": null,
    "payment_method": {
      "card": {
        "channel": "link",
        "card_number": "xxxxxx1111"
      }
    },
    "payment_amount": 10.01,
    "payment_time": "2021-07-23T12:15:06+05:30",
    "payment_completion_time": "2021-07-23T12:18:59+05:30",
    "payment_status": "FAILED",
    "payment_message": "Transaction failed",
    "bank_reference": "P78112898712",
    "auth_id": "A898101"
  }
]
```

## PGPayOrder

> PGPayOrder(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, pay_order_request : Annotated[PayOrderRequest, Field(..., description="Request body to create a transaction at cashfree using `payment_session_id`")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Order Pay ([Docs](https://docs.cashfree.com/reference/pgpayorder))

## Example
#### Card
```python
cardPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        CardPaymentMethod(
            card=Card(
                channel="link",
                card_number="4111111111111111",
                card_expiry_mm="12",
                card_holder_name="Test",
                card_cvv="123",
                card_expiry_yy="25"
            )
        )
    )
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=cardPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payOrderRequest** | **PayOrderRequest*** | Request body to create a transaction at cashfree using &#x60;payment_session_id&#x60; | 
 **xApiVersion** | **string** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
 **xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 
 

#### Netbanking
```python
netbankingRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        NetBankingPaymentMethod(
            netbanking=Netbanking(
                channel="link",
                netbanking_bank_code=3010
            )
        )
    )
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=netbankingRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### UPI
```python
upiPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        UPIPaymentMethod(
            upi=Upi(
                channel="collect",
                upi_id="testsuccess@gocash"
            )
        )
    )
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=upiPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### UPI
```python
upiPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        UPIPaymentMethod(
            upi=Upi(
                channel="link"
            )
        )
    )
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=upiPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### QR
```python
upiPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        UPIPaymentMethod(
            upi=Upi(
                channel="qrcode",
                upi_id="testsuccess@gocash"
            )
        )
    )
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=upiPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### Wallet
```python
walletPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        AppPaymentMethod(
            app=App(
                channel="link",
                provider="phonepe",
                phone="9898989898"
            )
        )
    )
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=walletPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### Card (with saving it)
```python
cardPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        CardPaymentMethod(
            card=Card(
                channel="link",
                card_number="4111111111111111",
                card_expiry_mm="12",
                card_holder_name="Test",
                card_cvv="123",
                card_expiry_yy="25"
            )
        )
    ),
    save_instrument=True
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=cardPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### Card with saved instrument
```python
cardPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        CardPaymentMethod(
            card=Card(
                channel="link",
                card_cvv="123",
                instrument_id="54deabb4-ba45-4a60-9e6a-9c016fe7ab10"
            )
        )
    ),
    save_instrument=True
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=cardPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### Card (with native otp)
```python
cardPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        CardPaymentMethod(
            card=Card(
                channel="post",
                card_number="4111111111111111",
                card_expiry_mm="12",
                card_holder_name="Test",
                card_cvv="123",
                card_expiry_yy="25"
            )
        )
    ),
    save_instrument=True
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=cardPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

#### EMI
```python
emiPayRequest = PayOrderRequest(
    payment_session_id="session_LnO-vcZ9znG_swyugIFmZRtvP3ZC7euzAq4Gq8IfNjt68OFCJ31mbJsN8SWZ169G8y0awciDTv5wSGSgG-EDdG0eQTX1Ra43hdhWE4EtEEIJ",
    payment_method=PayOrderRequestPaymentMethod(
        CardEMIPaymentMethod(
            emi=CardEMI(
                channel="post",
                card_number="4111111111111111",
                card_expiry_mm="12",
                card_holder_name="Test",
                card_cvv="123",
                card_expiry_yy="25",
                emi_tenure=3,
                card_bank_name="hdfc"
            )
        )
    ),
    save_instrument=True
)
try:
    api_response = Cashfree().PGPayOrder(x_api_version="2022-09-01", pay_order_request=emiPayRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Response
```json
{
  "payment_method": "card",
  "channel": "link",
  "action": "link",
  "cf_payment_id": 91235,
  "payment_amount": 22.42,
  "data": {
    "url": "https://sandbox.cashfree.com/pg/view/gateway/FHsuvhayLM5mmhINoqri7ba296e2ebca8b98e6119f6223021a13",
    "payload": {
      "name": "card"
    },
    "content_type": "application/x-www-form-urlencoded",
    "method": "post"
  }
}
```

## PGAuthorizeOrder

> PGAuthorizeOrder(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, order_id : Annotated[StrictStr, Field(..., description="The id which uniquely identifies your order")] = None, authorize_order_request : Annotated[AuthorizeOrderRequest, Field(..., description="Request to Capture or Void Transactions")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Preauthorization ([Docs](https://docs.cashfree.com/reference/pgauthorizeorder))

### Example

```python
authorizeOrderRequest = AuthorizeOrderRequest(
    action="CAPTURE",
    amount=1.0
)
try:
    api_response = Cashfree().PGAuthorizeOrder(x_api_version="2022-09-01", order_id="order_342bAHtHiGpa2XePHbvRdu22S7p8U", authorize_order_request=authorizeOrderRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderId** | **string*** | The id which uniquely identifies your order | 
 **authorizeOrderRequest** | **AuthorizeOrderRequest*** | Request to Capture or Void Transactions |
 **xApiVersion** | **string** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
 **xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 
 

### Response
```json
{
  "cf_payment_id": 12376123,
  "order_id": "order_8123",
  "entity": "payment",
  "payment_currency": "INR",
  "error_details": null,
  "order_amount": 10.01,
  "is_captured": true,
  "payment_group": "upi",
  "authorization": {
    "action": "CAPTURE",
    "status": "PENDING",
    "captured_amount": 100,
    "start_time": "2022-02-09T18:04:34+05:30",
    "end_time": "2022-02-19T18:04:34+05:30",
    "approve_by": "2022-02-09T18:04:34+05:30",
    "action_reference": "6595231908096894505959",
    "action_time": "2022-08-03T16:09:51"
  },
  "payment_method": {
    "upi": {
      "channel": "collect",
      "upi_id": "rohit@xcxcx"
    }
  },
  "payment_amount": 10.01,
  "payment_time": "2021-07-23T12:15:06+05:30",
  "payment_completion_time": "2021-07-23T12:18:59+05:30",
  "payment_status": "SUCCESS",
  "payment_message": "Transaction successful",
  "bank_reference": "P78112898712",
  "auth_id": "A898101"
}
```


## PGOrderAuthenticatePayment

> PGOrderAuthenticatePayment(self, x_api_version : Annotated[StrictStr, Field(..., description="API version to be used. Format is in YYYY-MM-DD")] = None, cf_payment_id : Annotated[StrictStr, Field(..., description="The Cashfree payment or transaction ID.")] = None, order_authenticate_payment_request : Annotated[OrderAuthenticatePaymentRequest, Field(..., description="Request body to submit/resend headless OTP. To use this API make sure you have headless OTP enabled for your account")] = None, x_request_id : Annotated[Optional[StrictStr], Field(description="Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree")] = None, x_idempotency_key : Annotated[Optional[StrictStr], Field(description="An idempotency key is a unique identifier you include with your API call. If the request fails or times out, you can safely retry it using the same key to avoid duplicate actions.  ")] = None, **kwargs) -> ApiResponse:

Submit or Resend OTP ([Docs](https://docs.cashfree.com/reference/pgorderauthenticatepayment))

### Example

```python
authenticatePaymentRequest = OrderAuthenticatePaymentRequest(
    action="SUBMIT_OTP",
    otp="111000"
)
try:
    api_response = Cashfree().PGOrderAuthenticatePayment(x_api_version="2022-09-01", cf_payment_id="12376124", order_authenticate_payment_request=authenticatePaymentRequest)
    print(api_response.data)
except Exception as e:
    print(e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**cfPaymentId** | **string*** | The Cashfree payment or transaction ID. | 
**xApiVersion** | **string** | API version to be used. Format is in YYYY-MM-DD | [default to &quot;2022-09-01&quot;]
**orderAuthenticatePaymentRequest** | **OrderAuthenticatePaymentRequest*** | Request body to submit/resend headless OTP. To use this API make sure you have headless OTP enabled for your account | 
**xRequestId** | **string** | Request id for the API call. Can be used to resolve tech issues. Communicate this in your tech related queries to cashfree | 


### Response
```json
{
  "cf_payment_id": 975654863,
  "authenticate_status": "FAILED",
  "action": "SUBMIT_OTP",
  "payment_message": "otp is invalid"
}
```
