# RefundWebhookDataEntity

data entity in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund** | [**RefundEntity**](RefundEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.refund_webhook_data_entity import RefundWebhookDataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RefundWebhookDataEntity from a JSON string
refund_webhook_data_entity_instance = RefundWebhookDataEntity.from_json(json)
# print the JSON string representation of the object
print RefundWebhookDataEntity.to_json()

# convert the object into a dict
refund_webhook_data_entity_dict = refund_webhook_data_entity_instance.to_dict()
# create an instance of RefundWebhookDataEntity from a dict
refund_webhook_data_entity_form_dict = refund_webhook_data_entity.from_dict(refund_webhook_data_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


