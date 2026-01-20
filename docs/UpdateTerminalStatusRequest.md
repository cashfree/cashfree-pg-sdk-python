# UpdateTerminalStatusRequest

Request body to update terminal status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_status** | **str** | Status of the terminal to be updated. possible values - ACTIVE, INACTIVE. | 

## Example

```python
from cashfree_pg.models.update_terminal_status_request import UpdateTerminalStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTerminalStatusRequest from a JSON string
update_terminal_status_request_instance = UpdateTerminalStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTerminalStatusRequest.to_json())

# convert the object into a dict
update_terminal_status_request_dict = update_terminal_status_request_instance.to_dict()
# create an instance of UpdateTerminalStatusRequest from a dict
update_terminal_status_request_from_dict = UpdateTerminalStatusRequest.from_dict(update_terminal_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


