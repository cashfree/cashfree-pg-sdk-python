# EligibilityPaylaterEntity

Eligible paylater payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility** | **bool** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_value** | **str** |  | [optional] 
**entity_details** | [**PaylaterEntity**](PaylaterEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_paylater_entity import EligibilityPaylaterEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityPaylaterEntity from a JSON string
eligibility_paylater_entity_instance = EligibilityPaylaterEntity.from_json(json)
# print the JSON string representation of the object
print EligibilityPaylaterEntity.to_json()

# convert the object into a dict
eligibility_paylater_entity_dict = eligibility_paylater_entity_instance.to_dict()
# create an instance of EligibilityPaylaterEntity from a dict
eligibility_paylater_entity_form_dict = eligibility_paylater_entity.from_dict(eligibility_paylater_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


