# UpdateTerminalRequest

Request body to update terminal details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_email** | **str** | Mention the updated email ID of the terminal. | [optional] 
**terminal_phone_no** | **str** | Terminal phone number to be updated. | [optional] 
**terminal_meta** | [**UpdateTerminalRequestTerminalMeta**](UpdateTerminalRequestTerminalMeta.md) |  | [optional] 
**terminal_type** | **str** | Mention the terminal type to be updated. Possible values - AGENT, STOREFRONT. | 

## Example

```python
from cashfree_pg.models.update_terminal_request import UpdateTerminalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTerminalRequest from a JSON string
update_terminal_request_instance = UpdateTerminalRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTerminalRequest.to_json()

# convert the object into a dict
update_terminal_request_dict = update_terminal_request_instance.to_dict()
# create an instance of UpdateTerminalRequest from a dict
update_terminal_request_form_dict = update_terminal_request.from_dict(update_terminal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


