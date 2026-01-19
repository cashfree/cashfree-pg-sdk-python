# InstrumentWebhook

Instrument webhook object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InstrumentWebhookData**](InstrumentWebhookData.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.instrument_webhook import InstrumentWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentWebhook from a JSON string
instrument_webhook_instance = InstrumentWebhook.from_json(json)
# print the JSON string representation of the object
print InstrumentWebhook.to_json()

# convert the object into a dict
instrument_webhook_dict = instrument_webhook_instance.to_dict()
# create an instance of InstrumentWebhook from a dict
instrument_webhook_form_dict = instrument_webhook.from_dict(instrument_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


