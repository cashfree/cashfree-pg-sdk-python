# DiscountDetails

detils of the discount object of offer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | **str** | Type of discount | 
**discount_value** | **float** | Value of Discount. | 
**max_discount_amount** | **float** | Maximum Value of Discount allowed. | 

## Example

```python
from cashfree_pg.models.discount_details import DiscountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountDetails from a JSON string
discount_details_instance = DiscountDetails.from_json(json)
# print the JSON string representation of the object
print DiscountDetails.to_json()

# convert the object into a dict
discount_details_dict = discount_details_instance.to_dict()
# create an instance of DiscountDetails from a dict
discount_details_form_dict = discount_details.from_dict(discount_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


