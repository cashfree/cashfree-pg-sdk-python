# SavedInstrumentMeta

Card instrument meta information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_network** | **str** | card scheme/network of the saved card. Example visa, mastercard | [optional] 
**card_bank_name** | **str** | Issuing bank name of saved card | [optional] 
**card_country** | **str** | Issuing country of saved card | [optional] 
**card_type** | **str** | Type of saved card | [optional] 
**card_token_details** | **object** |  | [optional] 

## Example

```python
from cashfree_pg.models.saved_instrument_meta import SavedInstrumentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SavedInstrumentMeta from a JSON string
saved_instrument_meta_instance = SavedInstrumentMeta.from_json(json)
# print the JSON string representation of the object
print SavedInstrumentMeta.to_json()

# convert the object into a dict
saved_instrument_meta_dict = saved_instrument_meta_instance.to_dict()
# create an instance of SavedInstrumentMeta from a dict
saved_instrument_meta_form_dict = saved_instrument_meta.from_dict(saved_instrument_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


