# TerminalEntityTerminalMeta

Terminal metadata, required field for storefront.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_operator** | **str** | name of the STOREFRONT operator. | [optional] 

## Example

```python
from cashfree_pg.models.terminal_entity_terminal_meta import TerminalEntityTerminalMeta

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalEntityTerminalMeta from a JSON string
terminal_entity_terminal_meta_instance = TerminalEntityTerminalMeta.from_json(json)
# print the JSON string representation of the object
print TerminalEntityTerminalMeta.to_json()

# convert the object into a dict
terminal_entity_terminal_meta_dict = terminal_entity_terminal_meta_instance.to_dict()
# create an instance of TerminalEntityTerminalMeta from a dict
terminal_entity_terminal_meta_form_dict = terminal_entity_terminal_meta.from_dict(terminal_entity_terminal_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


