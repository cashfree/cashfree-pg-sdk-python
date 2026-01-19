# Products

Use this to set configurations for the products like One Click Checkout, Verify and Pay, if they are enabled for your account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_click_checkout** | [**ProductDetails**](ProductDetails.md) |  | [optional] 
**verify_pay** | [**ProductDetails**](ProductDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.products import Products

# TODO update the JSON string below
json = "{}"
# create an instance of Products from a JSON string
products_instance = Products.from_json(json)
# print the JSON string representation of the object
print Products.to_json()

# convert the object into a dict
products_dict = products_instance.to_dict()
# create an instance of Products from a dict
products_form_dict = products.from_dict(products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


