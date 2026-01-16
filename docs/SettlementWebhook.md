# SettlementWebhook

Settlement webhook object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SettlementWebhookDataEntity**](SettlementWebhookDataEntity.md) |  | [optional] 
**event_time** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.settlement_webhook import SettlementWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementWebhook from a JSON string
settlement_webhook_instance = SettlementWebhook.from_json(json)
# print the JSON string representation of the object
print SettlementWebhook.to_json()

# convert the object into a dict
settlement_webhook_dict = settlement_webhook_instance.to_dict()
# create an instance of SettlementWebhook from a dict
settlement_webhook_form_dict = settlement_webhook.from_dict(settlement_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


