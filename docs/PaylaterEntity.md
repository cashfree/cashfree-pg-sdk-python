# PaylaterEntity

Paylater Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.paylater_entity import PaylaterEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaylaterEntity from a JSON string
paylater_entity_instance = PaylaterEntity.from_json(json)
# print the JSON string representation of the object
print PaylaterEntity.to_json()

# convert the object into a dict
paylater_entity_dict = paylater_entity_instance.to_dict()
# create an instance of PaylaterEntity from a dict
paylater_entity_form_dict = paylater_entity.from_dict(paylater_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


