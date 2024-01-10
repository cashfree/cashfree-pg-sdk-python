# PaymentWebhookErrorEntity

error details present in the webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 
**error_reason** | **str** |  | [optional] 
**error_source** | **str** |  | [optional] 
**error_code_raw** | **str** |  | [optional] 
**error_description_raw** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_webhook_error_entity import PaymentWebhookErrorEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWebhookErrorEntity from a JSON string
payment_webhook_error_entity_instance = PaymentWebhookErrorEntity.from_json(json)
# print the JSON string representation of the object
print PaymentWebhookErrorEntity.to_json()

# convert the object into a dict
payment_webhook_error_entity_dict = payment_webhook_error_entity_instance.to_dict()
# create an instance of PaymentWebhookErrorEntity from a dict
payment_webhook_error_entity_form_dict = payment_webhook_error_entity.from_dict(payment_webhook_error_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


