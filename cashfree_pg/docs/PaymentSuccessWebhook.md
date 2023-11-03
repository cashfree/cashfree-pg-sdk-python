# PaymentSuccessWebhook

object for payment success webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WHdata**](WHdata.md) |  | [optional] 
**event_time** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_success_webhook import PaymentSuccessWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessWebhook from a JSON string
payment_success_webhook_instance = PaymentSuccessWebhook.from_json(json)
# print the JSON string representation of the object
print PaymentSuccessWebhook.to_json()

# convert the object into a dict
payment_success_webhook_dict = payment_success_webhook_instance.to_dict()
# create an instance of PaymentSuccessWebhook from a dict
payment_success_webhook_form_dict = payment_success_webhook.from_dict(payment_success_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


