# Webhook


## PGVerifyWebhookSignature

> PGVerifyWebhookSignature(self, signature, rawBody, timestamp):

Verify Webhook Signatures ([Docs](https://docs.cashfree.com/reference/pg-webhook))

### Example
```python
# the below example uses flask framework
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    signature = request.headers.get('x-webhook-signature')
    timestamp = request.headers.get('x-webhook-timestamp')
    
    raw_body = request.data.decode('utf-8')
    webhook_event, err = Cashfree().PGVerifyWebhookSignature(signature, raw_body, timestamp)
    
    if err is not None:
        print(err)
    else:
        print(webhook_event['object'])
    
    return '', 200
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**signature** | **string** | The "x-webhook-signature" present in the headers received | 
**rawBody** | **string** | The request body received in the request in string format |
**timestamp** | **string** | The "x-webhook-timestamp" present in the headers received | 


### Response

```json
{
    "type": "PAYMENT_SUCCESS_WEBHOOK",
    "rawBody":"{\"type\":\"PAYMENT_SUCCESS_WEBHOOK\",\"data\":{}}",
    "object": {
        "type": "PAYMENT_SUCCESS_WEBHOOK",
        "data": {
            
        }
    }
}
```

`Note:` The `object` in the response is returned as a JSON object. But it can be of any of the following types:
- [Payment Webhook](https://docs.cashfree.com/docs/payment-webhooks)
- [Refund Webhook](https://docs.cashfree.com/docs/refunds-webhook)
- [Settlement Webhook](https://docs.cashfree.com/docs/settlements-webhook)
- [Instrument Webhook](https://docs.cashfree.com/docs/instrument-webhook)
