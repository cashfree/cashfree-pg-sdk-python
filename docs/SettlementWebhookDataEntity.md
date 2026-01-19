# SettlementWebhookDataEntity

data entity in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement** | [**SettlementEntity**](SettlementEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.settlement_webhook_data_entity import SettlementWebhookDataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementWebhookDataEntity from a JSON string
settlement_webhook_data_entity_instance = SettlementWebhookDataEntity.from_json(json)
# print the JSON string representation of the object
print SettlementWebhookDataEntity.to_json()

# convert the object into a dict
settlement_webhook_data_entity_dict = settlement_webhook_data_entity_instance.to_dict()
# create an instance of SettlementWebhookDataEntity from a dict
settlement_webhook_data_entity_form_dict = settlement_webhook_data_entity.from_dict(settlement_webhook_data_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


