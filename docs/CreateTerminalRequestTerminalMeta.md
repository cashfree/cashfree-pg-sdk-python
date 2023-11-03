# CreateTerminalRequestTerminalMeta

terminal metadata. required field for storefront.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_operator** | **str** | name of the STOREFRONT operator. | [optional] 

## Example

```python
from cashfree_pg.models.create_terminal_request_terminal_meta import CreateTerminalRequestTerminalMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTerminalRequestTerminalMeta from a JSON string
create_terminal_request_terminal_meta_instance = CreateTerminalRequestTerminalMeta.from_json(json)
# print the JSON string representation of the object
print CreateTerminalRequestTerminalMeta.to_json()

# convert the object into a dict
create_terminal_request_terminal_meta_dict = create_terminal_request_terminal_meta_instance.to_dict()
# create an instance of CreateTerminalRequestTerminalMeta from a dict
create_terminal_request_terminal_meta_form_dict = create_terminal_request_terminal_meta.from_dict(create_terminal_request_terminal_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


