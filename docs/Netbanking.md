# Netbanking

Netbanking payment method request body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The channel for netbanking will always be &#x60;link&#x60; | 
**netbanking_bank_code** | **int** | Bank code | [optional] 
**netbanking_bank_name** | **str** | String code for bank | [optional] 

## Example

```python
from cashfree_pg.models.netbanking import Netbanking

# TODO update the JSON string below
json = "{}"
# create an instance of Netbanking from a JSON string
netbanking_instance = Netbanking.from_json(json)
# print the JSON string representation of the object
print Netbanking.to_json()

# convert the object into a dict
netbanking_dict = netbanking_instance.to_dict()
# create an instance of Netbanking from a dict
netbanking_form_dict = netbanking.from_dict(netbanking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


