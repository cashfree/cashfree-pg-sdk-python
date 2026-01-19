# UpdateTerminalRequestTerminalMeta

Terminal metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_operator** | **str** | Name of the operator for the storefront. | [optional] 

## Example

```python
from cashfree_pg.models.update_terminal_request_terminal_meta import UpdateTerminalRequestTerminalMeta

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTerminalRequestTerminalMeta from a JSON string
update_terminal_request_terminal_meta_instance = UpdateTerminalRequestTerminalMeta.from_json(json)
# print the JSON string representation of the object
print UpdateTerminalRequestTerminalMeta.to_json()

# convert the object into a dict
update_terminal_request_terminal_meta_dict = update_terminal_request_terminal_meta_instance.to_dict()
# create an instance of UpdateTerminalRequestTerminalMeta from a dict
update_terminal_request_terminal_meta_form_dict = update_terminal_request_terminal_meta.from_dict(update_terminal_request_terminal_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


