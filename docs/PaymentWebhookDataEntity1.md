# PaymentWebhookDataEntity1

data entity in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund** | [**RefundEntity**](RefundEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_webhook_data_entity1 import PaymentWebhookDataEntity1

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWebhookDataEntity1 from a JSON string
payment_webhook_data_entity1_instance = PaymentWebhookDataEntity1.from_json(json)
# print the JSON string representation of the object
print PaymentWebhookDataEntity1.to_json()

# convert the object into a dict
payment_webhook_data_entity1_dict = payment_webhook_data_entity1_instance.to_dict()
# create an instance of PaymentWebhookDataEntity1 from a dict
payment_webhook_data_entity1_form_dict = payment_webhook_data_entity1.from_dict(payment_webhook_data_entity1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


