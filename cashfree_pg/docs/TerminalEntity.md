# TerminalEntity

Create terminal response object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_on** | **str** |  | [optional] 
**cf_terminal_id** | **int** |  | [optional] 
**last_updated_on** | **str** |  | [optional] 
**terminal_address** | **str** |  | [optional] 
**terminal_email** | **str** |  | [optional] 
**terminal_type** | **str** |  | [optional] 
**teminal_id** | **str** |  | [optional] 
**terminal_name** | **str** |  | [optional] 
**terminal_note** | **str** |  | [optional] 
**terminal_phone_no** | **str** |  | [optional] 
**terminal_status** | **str** |  | [optional] 
**terminal_meta** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.terminal_entity import TerminalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalEntity from a JSON string
terminal_entity_instance = TerminalEntity.from_json(json)
# print the JSON string representation of the object
print TerminalEntity.to_json()

# convert the object into a dict
terminal_entity_dict = terminal_entity_instance.to_dict()
# create an instance of TerminalEntity from a dict
terminal_entity_form_dict = terminal_entity.from_dict(terminal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


