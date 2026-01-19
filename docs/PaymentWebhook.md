# PaymentWebhook

payment webhook object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentWebhookDataEntity**](PaymentWebhookDataEntity.md) |  | [optional] 
**event_time** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_webhook import PaymentWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWebhook from a JSON string
payment_webhook_instance = PaymentWebhook.from_json(json)
# print the JSON string representation of the object
print PaymentWebhook.to_json()

# convert the object into a dict
payment_webhook_dict = payment_webhook_instance.to_dict()
# create an instance of PaymentWebhook from a dict
payment_webhook_form_dict = payment_webhook.from_dict(payment_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


