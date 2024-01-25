# CashbackDetails

Cashback detail boject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashback_type** | **str** | Type of discount | 
**cashback_value** | **float** | Value of Discount. | 
**max_cashback_amount** | **float** | Maximum Value of Cashback allowed. | 

## Example

```python
from cashfree_pg.models.cashback_details import CashbackDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CashbackDetails from a JSON string
cashback_details_instance = CashbackDetails.from_json(json)
# print the JSON string representation of the object
print CashbackDetails.to_json()

# convert the object into a dict
cashback_details_dict = cashback_details_instance.to_dict()
# create an instance of CashbackDetails from a dict
cashback_details_form_dict = cashback_details.from_dict(cashback_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


