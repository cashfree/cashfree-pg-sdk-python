# RefundWebhook

refund webhook object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RefundWebhookDataEntity**](RefundWebhookDataEntity.md) |  | [optional] 
**event_time** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.refund_webhook import RefundWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of RefundWebhook from a JSON string
refund_webhook_instance = RefundWebhook.from_json(json)
# print the JSON string representation of the object
print RefundWebhook.to_json()

# convert the object into a dict
refund_webhook_dict = refund_webhook_instance.to_dict()
# create an instance of RefundWebhook from a dict
refund_webhook_form_dict = refund_webhook.from_dict(refund_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


