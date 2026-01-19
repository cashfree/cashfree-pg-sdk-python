# ProductDetailsEntity

Configurations for this feature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the feature has been enabled for this order | [optional] 
**conditions** | [**List[ProductConditionsEntity]**](ProductConditionsEntity.md) | Configured condtions for the feature | [optional] 

## Example

```python
from cashfree_pg.models.product_details_entity import ProductDetailsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailsEntity from a JSON string
product_details_entity_instance = ProductDetailsEntity.from_json(json)
# print the JSON string representation of the object
print ProductDetailsEntity.to_json()

# convert the object into a dict
product_details_entity_dict = product_details_entity_instance.to_dict()
# create an instance of ProductDetailsEntity from a dict
product_details_entity_form_dict = product_details_entity.from_dict(product_details_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


