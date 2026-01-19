# ProductConditionsEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The Action key in the conditions array specifies whether a condition is allowed or denied for the specified rule or feature | [optional] 
**key** | **str** | key of the condition | [optional] 
**values** | **List[str]** | Values set for the condition | [optional] 

## Example

```python
from cashfree_pg.models.product_conditions_entity import ProductConditionsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ProductConditionsEntity from a JSON string
product_conditions_entity_instance = ProductConditionsEntity.from_json(json)
# print the JSON string representation of the object
print ProductConditionsEntity.to_json()

# convert the object into a dict
product_conditions_entity_dict = product_conditions_entity_instance.to_dict()
# create an instance of ProductConditionsEntity from a dict
product_conditions_entity_form_dict = product_conditions_entity.from_dict(product_conditions_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


