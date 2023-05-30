# cashfree-pg-sdk-python

- API version: 2022-09-01
- Package version: 2.0.1

---

## Requirements.

Python 2.7 and 3.4+

## Discord Server Support

Official Discord server is helpful to get support regarding any cashfree SDK , share any issues , raise tickets , give suggestions and request features for the SDK. Join the community of like-minded developers using the link provided below.
Link :- https://discord.gg/HrCz9tW2sh 

## Installation & Usage

### pip install

Yyou can install directly using:

```sh
pip3 install git+https://github.com/cashfree/cashfree-pg-sdk-python.git
```

(you may need to run `pip3` with root permission: `sudo pip3 install git+https://github.com/cashfree/cashfree-pg-sdk-python.git`)

Then import the package:

```python
import cashfree_pg_sdk_python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python3 setup.py install --user
```

(or `sudo python3 setup.py install` to install the package for all users)

Then import the package:

```python
import cashfree_pg_sdk_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:
The following part is the basic and common setup required to make any request to Casfhfree using the sdk.

```python
# Note : Please visit https://docs.cashfree.com/ for the complete documentation of the various terminologies used below, 
# if not familiar with.


from __future__ import print_function

import time
import cashfree_pg_sdk_python
from cashfree_pg_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.cashfree.com/pg
# See configuration.py for a list of all supported configuration parameters.
configuration = CFPython_sdk.Configuration(
    host = "https://sandbox.cashfree.com/pg"
)
# Enter a context with an instance of the API client
with CFPython_sdk.ApiClient(configuration) as api_client:
# Create an instance of the API class
api_instance = CFPython_sdk.OrdersApi(api_client)
x_client_id = 'x_client_id_example' # str |
x_client_secret = 'x_client_secret_example' # str |
x_api_version = '2022-09-01' # str |  (optional) (default to '2022-09-01')
x_idempotency_replayed = False # bool |  (optional) (default to False)
x_idempotency_key = 'x_idempotency_key_example' # str |  (optional)
x_request_id = 'x_request_id_example' # str |  (optional)
cf_order_request = CFPython_sdk.CFOrderRequest() # CFOrderRequest |  (optional)
```

### Making the config and headers for the subsequent CreateOrder / pay_order etc. requests
The variables declared and assigned in the previous (GETTING STARTED) step will be used here.
```python
    cf_config_test = CFConfig(x_client_id,
                            x_client_secret, x_api_version, CFenv.SANDBOX)
    # cfHeaders consists of two things mainly, 1) x-idempotecy-key and 2) x-request-id ; x-request-id can help the consumer of the # sdk to maintain meaningful logs on their side. This can be a unique/non-unique identifier that the consumer can use. It is
    # advisable that x-request-id be unique for each request so that the logging of the events of one request do not clash 
    # with the other. Here, request is a CreateOrder/OrderPay etc. requests that the consumer makes to cashfree.
    cf_headers_test = CFHeaders(
        x_idempotency_key, x_request_id)
```

### Creating an Order 
The following snippet provides an example on how to create an order with Cashfree
```python
    # Making the create order request. For more extensive 
    cf_order_request_test = cf_order_request.CFOrderRequest(
        order_amount=10.16,
        order_currency="INR",
        customer_details=cf_customer_details.CFCustomerDetails(
            customer_id="testpythonSDKUSER",
            customer_email="email@cf.com",
            customer_phone="9999999999"
        ), order_note="YOUR_NOTE",
        order_tags={
            "key": "key_example",
        },
        order_meta=CFOrderMeta(
            payment_methods="nb,upi",
            notify_url="https://webhook.merchantsite.com/691ffcf3-80db-4c10-b0d6-fbdc0be7b146" # This is the webhook url.
        ),
    )
     # Create Order Snippet
    try:
        createOrderResult = CreateOrder(cf_config_test, cf_headers_test,
                             cf_order_request_test)
        print("Creat order successful with the following details")
        print(createOrderResult)
    except ApiException as e:
        print("Exception when calling create order: %s\n" % e)
```
Note: createOrderResult[0].order_id can be used to get the order id from the response.

### Getting Order Details
You may wonder why is this function important -> Although you get the order details of the created order in the response of the CreateOrder as a part of the result above , but if you have to get the order details again after some time against the orderid then this function can be utilised.
The following snippet is an example on how to use the function.

```python
# Get Order Snippet
try:
    GetOrderResult = GetOrder(cfconfigtest, cfheaderstest,
                      result[0].order_id)
    print("Get Order successful wiith the following details")
    print(createOrderResult)
except ApiException as e:
    print("Exception when calling create order: %s\n" % e)
```
### Other funtions
Pay Order call , getting transaction details and creating refund are all supported by this SDK, the same payload as in the normal API can be created and passed to the funtions and the SDK takes care of the network call thereafter.
gatewayiinterface.py contains all the methods that can be used.

For any queries/help join the Official discord group mentioned in the beginning of this README doc.

## Documentation For Models

- [CFApp](docs/CFApp.md)
- [CFAppPayment](docs/CFAppPayment.md)
- [CFAuthorizationInPaymentsEntity](docs/CFAuthorizationInPaymentsEntity.md)
- [CFAuthorizationRequest](docs/CFAuthorizationRequest.md)
- [CFCard](docs/CFCard.md)
- [CFCardEMI](docs/CFCardEMI.md)
- [CFCardPayment](docs/CFCardPayment.md)
- [CFCardlessEMI](docs/CFCardlessEMI.md)
- [CFCardlessEMIPayment](docs/CFCardlessEMIPayment.md)
- [CFCryptogram](docs/CFCryptogram.md)
- [CFCustomerDetails](docs/CFCustomerDetails.md)
- [CFEMIPayment](docs/CFEMIPayment.md)
- [CFError](docs/CFError.md)
- [CFFetchAllSavedInstruments](docs/CFFetchAllSavedInstruments.md)
- [CFLink](docs/CFLink.md)
- [CFLinkCancelledResponse](docs/CFLinkCancelledResponse.md)
- [CFLinkCustomerDetailsEntity](docs/CFLinkCustomerDetailsEntity.md)
- [CFLinkMetaEntity](docs/CFLinkMetaEntity.md)
- [CFLinkNotifyEntity](docs/CFLinkNotifyEntity.md)
- [CFLinkOrders](docs/CFLinkOrders.md)
- [CFLinkRequest](docs/CFLinkRequest.md)
- [CFNetbanking](docs/CFNetbanking.md)
- [CFNetbankingPayment](docs/CFNetbankingPayment.md)
- [CFOrder](docs/CFOrder.md)
- [CFOrderMeta](docs/CFOrderMeta.md)
- [CFOrderPayData](docs/CFOrderPayData.md)
- [CFOrderPayRequest](docs/CFOrderPayRequest.md)
- [CFOrderPayResponse](docs/CFOrderPayResponse.md)
- [CFOrderRequest](docs/CFOrderRequest.md)
- [CFPaylater](docs/CFPaylater.md)
- [CFPaylaterPayment](docs/CFPaylaterPayment.md)
- [CFPaymentMethod](docs/CFPaymentMethod.md)
- [CFPaymentURLObject](docs/CFPaymentURLObject.md)
- [CFPaymentsEntity](docs/CFPaymentsEntity.md)
- [CFPaymentsEntityApp](docs/CFPaymentsEntityApp.md)
- [CFPaymentsEntityAppPayment](docs/CFPaymentsEntityAppPayment.md)
- [CFPaymentsEntityCard](docs/CFPaymentsEntityCard.md)
- [CFPaymentsEntityCardPayment](docs/CFPaymentsEntityCardPayment.md)
- [CFPaymentsEntityCardlessEMI](docs/CFPaymentsEntityCardlessEMI.md)
- [CFPaymentsEntityCardlessEMIPayment](docs/CFPaymentsEntityCardlessEMIPayment.md)
- [CFPaymentsEntityMethod](docs/CFPaymentsEntityMethod.md)
- [CFPaymentsEntityNetbankingPayment](docs/CFPaymentsEntityNetbankingPayment.md)
- [CFPaymentsEntityPaylater](docs/CFPaymentsEntityPaylater.md)
- [CFPaymentsEntityPaylaterPayment](docs/CFPaymentsEntityPaylaterPayment.md)
- [CFPaymentsEntityUPI](docs/CFPaymentsEntityUPI.md)
- [CFPaymentsEntityUPIPayment](docs/CFPaymentsEntityUPIPayment.md)
- [CFRefund](docs/CFRefund.md)
- [CFRefundRequest](docs/CFRefundRequest.md)
- [CFRefundURLObject](docs/CFRefundURLObject.md)
- [CFSavedInstrumentMeta](docs/CFSavedInstrumentMeta.md)
- [CFSettlementURLObject](docs/CFSettlementURLObject.md)
- [CFSettlementsEntity](docs/CFSettlementsEntity.md)
- [CFUPI](docs/CFUPI.md)
- [CFUPIAuthorizeDetails](docs/CFUPIAuthorizeDetails.md)
- [CFUPIPayment](docs/CFUPIPayment.md)
- [CFVendorSplit](docs/CFVendorSplit.md)
- [LinkCancelledError](docs/LinkCancelledError.md)
- [RefundSpeed](docs/RefundSpeed.md)

## Documentation For Authorization

All endpoints do not require authorization.

## Author

developers@cashfree.com
