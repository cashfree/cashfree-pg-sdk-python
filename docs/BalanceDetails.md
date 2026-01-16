# BalanceDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **float** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**merchant_unsettled** | **float** |  | [optional] 
**vendor_unsettled** | **float** |  | [optional] 

## Example

```python
from cashfree_pg.models.balance_details import BalanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceDetails from a JSON string
balance_details_instance = BalanceDetails.from_json(json)
# print the JSON string representation of the object
print BalanceDetails.to_json()

# convert the object into a dict
balance_details_dict = balance_details_instance.to_dict()
# create an instance of BalanceDetails from a dict
balance_details_form_dict = balance_details.from_dict(balance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


