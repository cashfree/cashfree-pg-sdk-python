# CartItem

Each item in the cart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Unique identifier of the item | [optional] 
**item_name** | **str** | Name of the item | [optional] 
**item_description** | **str** | Description of the item | [optional] 
**item_tags** | **List[str]** | Tags attached to that item | [optional] 
**item_details_url** | **str** | Item details url | [optional] 
**item_image_url** | **str** | Item image url | [optional] 
**item_original_unit_price** | **float** | Original price | [optional] 
**item_discounted_unit_price** | **float** | Discounted Price | [optional] 
**item_currency** | **str** | Currency of the item. | [optional] 
**item_quantity** | **float** | Quantity if that item | [optional] 

## Example

```python
from cashfree_pg.models.cart_item import CartItem

# TODO update the JSON string below
json = "{}"
# create an instance of CartItem from a JSON string
cart_item_instance = CartItem.from_json(json)
# print the JSON string representation of the object
print(CartItem.to_json())

# convert the object into a dict
cart_item_dict = cart_item_instance.to_dict()
# create an instance of CartItem from a dict
cart_item_from_dict = CartItem.from_dict(cart_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


