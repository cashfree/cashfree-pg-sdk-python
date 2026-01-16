# EligibilityMethodItem

Eligibile payment method object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility** | **bool** | Indicates whether the payment method is eligible. | [optional] 
**entity_type** | **str** | Type of entity (e.g., \&quot;payment_methods\&quot;). | [optional] 
**entity_value** | **str** | Payment method (e.g., enach, pnach, upi, card). | [optional] 
**entity_details** | [**EligibilityMethodItemEntityDetails**](EligibilityMethodItemEntityDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_method_item import EligibilityMethodItem

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityMethodItem from a JSON string
eligibility_method_item_instance = EligibilityMethodItem.from_json(json)
# print the JSON string representation of the object
print EligibilityMethodItem.to_json()

# convert the object into a dict
eligibility_method_item_dict = eligibility_method_item_instance.to_dict()
# create an instance of EligibilityMethodItem from a dict
eligibility_method_item_form_dict = eligibility_method_item.from_dict(eligibility_method_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


