# CartDetailsEntity

Cart Details in the Order Entity Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart_id** | **str** | ID of the cart that was created | [optional] 

## Example

```python
from cashfree_pg.models.cart_details_entity import CartDetailsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CartDetailsEntity from a JSON string
cart_details_entity_instance = CartDetailsEntity.from_json(json)
# print the JSON string representation of the object
print CartDetailsEntity.to_json()

# convert the object into a dict
cart_details_entity_dict = cart_details_entity_instance.to_dict()
# create an instance of CartDetailsEntity from a dict
cart_details_entity_form_dict = cart_details_entity.from_dict(cart_details_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


