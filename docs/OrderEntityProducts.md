# OrderEntityProducts

Configurations for the products like One Click Checkout, Verify and Pay, if they are enabled for your account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_click_checkout** | [**ProductDetailsEntity**](ProductDetailsEntity.md) |  | [optional] 
**verify_pay** | [**ProductDetailsEntity**](ProductDetailsEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.order_entity_products import OrderEntityProducts

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEntityProducts from a JSON string
order_entity_products_instance = OrderEntityProducts.from_json(json)
# print the JSON string representation of the object
print OrderEntityProducts.to_json()

# convert the object into a dict
order_entity_products_dict = order_entity_products_instance.to_dict()
# create an instance of OrderEntityProducts from a dict
order_entity_products_form_dict = order_entity_products.from_dict(order_entity_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


