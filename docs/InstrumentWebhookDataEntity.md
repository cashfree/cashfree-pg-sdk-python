# InstrumentWebhookDataEntity

data entity in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | [**InstrumentEntity**](InstrumentEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.instrument_webhook_data_entity import InstrumentWebhookDataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentWebhookDataEntity from a JSON string
instrument_webhook_data_entity_instance = InstrumentWebhookDataEntity.from_json(json)
# print the JSON string representation of the object
print InstrumentWebhookDataEntity.to_json()

# convert the object into a dict
instrument_webhook_data_entity_dict = instrument_webhook_data_entity_instance.to_dict()
# create an instance of InstrumentWebhookDataEntity from a dict
instrument_webhook_data_entity_form_dict = instrument_webhook_data_entity.from_dict(instrument_webhook_data_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


