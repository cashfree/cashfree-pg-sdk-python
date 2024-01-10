# Cashfree PG Python SDK
![GitHub](https://img.shields.io/github/license/cashfree/cashfree-pg-sdk-python) ![Discord](https://img.shields.io/discord/931125665669972018?label=discord) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/cashfree/cashfree-pg-sdk-python/master) ![GitHub release (with filter)](https://img.shields.io/github/v/release/cashfree/cashfree-pg-sdk-python?label=latest) ![GitHub forks](https://img.shields.io/github/forks/cashfree/cashfree-pg-sdk-python)

The Cashfree PG Python SDK offers a convenient solution to access [Cashfree PG APIs](https://docs.cashfree.com/reference/pg-new-apis-endpoint) from a server-side Go  applications. 



## Documentation

Cashfree's PG API Documentation - https://docs.cashfree.com/reference/pg-new-apis-endpoint

Learn and understand payment gateway workflows at Cashfree Payments [here](https://docs.cashfree.com/docs/payment-gateway)

Try out our interactive guides at [Cashfree Dev Studio](https://www.cashfree.com/devstudio) !

## Getting Started

### Installation
```bash
pip install cashfree_pg
```
### Configuration

```python
from cashfree_pg.models.create_order_request import CreateOrderRequest
from cashfree_pg.api_client import Cashfree
from cashfree_pg.models.customer_details import CustomerDetails

Cashfree.XClientId = "<x-client-id>"
Cashfree.XClientSecret = "<x-client-secret>"
Cashfree.XEnvironment = Cashfree.SANDBOX
x_api_version = "2022-09-01"
```

Generate your API keys (x-client-id , x-client-secret) from [Cashfree Merchant Dashboard](https://merchant.cashfree.com/merchants/login)

### Basic Usage
Create Order
```python
customerDetails = CustomerDetails(customer_id="walterwNrcMi", customer_phone="9999999999")
orderMeta = CreateOrderRequestOrderMeta(return_url="https://www.cashfree.com/devstudio/preview/pg/web/checkout?order_id={order_id}")
createOrderRequest = CreateOrderRequest(order_amount=1, order_currency="INR", customer_details=customerDetails, order_meta=orderMeta)
try:
    api_response = Cashfree().PGCreateOrder(x_api_version, createOrderRequest, None, None)
    print(api_response.data)
except Exception as e:
    print(e)
```

Get Order
```python
try:
    api_response = Cashfree().PGFetchOrder(x_api_version, "order_3242X4jQ5f0S9KYxZO9mtDL1Kx2Y7u", None)
    print(api_response.data)
except Exception as e:
    print(e)
```

## Licence

Apache Licensed. See [LICENSE.md](LICENSE.md) for more details
