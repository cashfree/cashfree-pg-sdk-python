# InstrumentWebhookData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InstrumentWebhookDataEntity**](InstrumentWebhookDataEntity.md) |  | [optional] 
**event_time** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.instrument_webhook_data import InstrumentWebhookData

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentWebhookData from a JSON string
instrument_webhook_data_instance = InstrumentWebhookData.from_json(json)
# print the JSON string representation of the object
print InstrumentWebhookData.to_json()

# convert the object into a dict
instrument_webhook_data_dict = instrument_webhook_data_instance.to_dict()
# create an instance of InstrumentWebhookData from a dict
instrument_webhook_data_form_dict = instrument_webhook_data.from_dict(instrument_webhook_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


