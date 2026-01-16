# BankDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**account_holder** | **str** |  | [optional] 
**ifsc** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.bank_details import BankDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BankDetails from a JSON string
bank_details_instance = BankDetails.from_json(json)
# print the JSON string representation of the object
print BankDetails.to_json()

# convert the object into a dict
bank_details_dict = bank_details_instance.to_dict()
# create an instance of BankDetails from a dict
bank_details_form_dict = bank_details.from_dict(bank_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


