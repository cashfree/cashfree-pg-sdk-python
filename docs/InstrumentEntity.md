# InstrumentEntity

Saved card instrument object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | customer_id for which the instrument was saved | [optional] 
**afa_reference** | **str** | cf_payment_id of the successful transaction done while saving instrument | [optional] 
**instrument_id** | **str** | saved instrument id | [optional] 
**instrument_type** | **str** | Type of the saved instrument | [optional] 
**instrument_uid** | **str** | Unique id for the saved instrument | [optional] 
**instrument_display** | **str** | masked card number displayed to the customer | [optional] 
**instrument_status** | **str** | Status of the saved instrument. | [optional] 
**created_at** | **str** | Timestamp at which instrument was saved. | [optional] 
**instrument_meta** | [**SavedInstrumentMeta**](SavedInstrumentMeta.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.instrument_entity import InstrumentEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentEntity from a JSON string
instrument_entity_instance = InstrumentEntity.from_json(json)
# print the JSON string representation of the object
print InstrumentEntity.to_json()

# convert the object into a dict
instrument_entity_dict = instrument_entity_instance.to_dict()
# create an instance of InstrumentEntity from a dict
instrument_entity_form_dict = instrument_entity.from_dict(instrument_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


