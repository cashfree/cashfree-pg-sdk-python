# TerminalDetails

Use this if you are creating an order for cashfree's softPOS

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_on** | **str** | date time at which terminal is added | [optional] 
**cf_terminal_id** | **int** | cashfree terminal id | [optional] 
**last_updated_on** | **str** | last instant when this terminal was updated | [optional] 
**terminal_address** | **str** | location of terminal | [optional] 
**terminal_id** | **str** | terminal id for merchant reference | 
**terminal_name** | **str** | name of terminal/agent/storefront | [optional] 
**terminal_note** | **str** | note given by merchant while creating the terminal | [optional] 
**terminal_phone_no** | **str** | mobile num of the terminal/agent/storefront | 
**terminal_status** | **str** | status of terminal active/inactive | [optional] 
**terminal_type** | **str** | To identify the type of terminal product in use, in this case it is SPOS. | 

## Example

```python
from cashfree_pg.models.terminal_details import TerminalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalDetails from a JSON string
terminal_details_instance = TerminalDetails.from_json(json)
# print the JSON string representation of the object
print TerminalDetails.to_json()

# convert the object into a dict
terminal_details_dict = terminal_details_instance.to_dict()
# create an instance of TerminalDetails from a dict
terminal_details_form_dict = terminal_details.from_dict(terminal_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


