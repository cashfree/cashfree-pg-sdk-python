# UpdateTerminalEntity

Update terminal response

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
**terminal_meta** | [**TerminalEntityTerminalMeta**](TerminalEntityTerminalMeta.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.update_terminal_entity import UpdateTerminalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTerminalEntity from a JSON string
update_terminal_entity_instance = UpdateTerminalEntity.from_json(json)
# print the JSON string representation of the object
print UpdateTerminalEntity.to_json()

# convert the object into a dict
update_terminal_entity_dict = update_terminal_entity_instance.to_dict()
# create an instance of UpdateTerminalEntity from a dict
update_terminal_entity_form_dict = update_terminal_entity.from_dict(update_terminal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


