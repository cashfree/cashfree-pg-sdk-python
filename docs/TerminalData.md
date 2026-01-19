# TerminalData

Terminal Data in the create order response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_mobile_number** | **str** |  | [optional] 
**cf_terminal_id** | **int** |  | [optional] 
**merchant_terminal_id** | **str** |  | [optional] 
**terminal_type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.terminal_data import TerminalData

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalData from a JSON string
terminal_data_instance = TerminalData.from_json(json)
# print the JSON string representation of the object
print TerminalData.to_json()

# convert the object into a dict
terminal_data_dict = terminal_data_instance.to_dict()
# create an instance of TerminalData from a dict
terminal_data_form_dict = terminal_data.from_dict(terminal_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


