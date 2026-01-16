# CryptogramEntity

Crytogram Card object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | instrument_id of saved instrument | [optional] 
**token_requestor_id** | **str** | TRID issued by card networks | [optional] 
**card_number** | **str** | token pan number | [optional] 
**card_expiry_mm** | **str** | token pan expiry month | [optional] 
**card_expiry_yy** | **str** | token pan expiry year | [optional] 
**cryptogram** | **str** | cryptogram | [optional] 
**card_display** | **str** | last 4 digits of original card number | [optional] 

## Example

```python
from cashfree_pg.models.cryptogram_entity import CryptogramEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CryptogramEntity from a JSON string
cryptogram_entity_instance = CryptogramEntity.from_json(json)
# print the JSON string representation of the object
print CryptogramEntity.to_json()

# convert the object into a dict
cryptogram_entity_dict = cryptogram_entity_instance.to_dict()
# create an instance of CryptogramEntity from a dict
cryptogram_entity_form_dict = cryptogram_entity.from_dict(cryptogram_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


