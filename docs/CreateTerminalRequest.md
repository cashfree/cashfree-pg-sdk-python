# CreateTerminalRequest

Request body to create a terminal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_id** | **str** | merchant’s internal terminal id | 
**terminal_phone_no** | **str** | phone number assigned to the terminal | 
**terminal_name** | **str** | terminal name to be assigned by merchants | 
**terminal_address** | **str** | address of the terminal. required for STOREFRONT | [optional] 
**terminal_email** | **str** | terminal email ID of the AGENT/STOREFRONT assigned by merchants. | 
**terminal_note** | **str** | additional note for terminal | [optional] 
**terminal_type** | **str** | mention the terminal type. possible values - AGENT, STOREFRONT. | 
**terminal_meta** | [**CreateTerminalRequestTerminalMeta**](CreateTerminalRequestTerminalMeta.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.create_terminal_request import CreateTerminalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTerminalRequest from a JSON string
create_terminal_request_instance = CreateTerminalRequest.from_json(json)
# print the JSON string representation of the object
print CreateTerminalRequest.to_json()

# convert the object into a dict
create_terminal_request_dict = create_terminal_request_instance.to_dict()
# create an instance of CreateTerminalRequest from a dict
create_terminal_request_form_dict = create_terminal_request.from_dict(create_terminal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


