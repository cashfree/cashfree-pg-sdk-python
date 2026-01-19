# CartDetails

The cart details that are necessary like shipping address, billing address and more.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_note** | **str** |  | [optional] 
**shipping_charge** | **float** |  | [optional] 
**cart_name** | **str** | Name of the cart. | [optional] 
**customer_shipping_address** | [**CartAddress**](CartAddress.md) |  | [optional] 
**customer_billing_address** | [**CartAddress**](CartAddress.md) |  | [optional] 
**cart_items** | [**List[CartItem]**](CartItem.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.cart_details import CartDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CartDetails from a JSON string
cart_details_instance = CartDetails.from_json(json)
# print the JSON string representation of the object
print CartDetails.to_json()

# convert the object into a dict
cart_details_dict = cart_details_instance.to_dict()
# create an instance of CartDetails from a dict
cart_details_form_dict = cart_details.from_dict(cart_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


