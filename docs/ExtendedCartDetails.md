# ExtendedCartDetails

The cart details that are necessary like shipping address, billing address and more.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the cart. | [optional] 
**items** | [**List[CartItem]**](CartItem.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.extended_cart_details import ExtendedCartDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedCartDetails from a JSON string
extended_cart_details_instance = ExtendedCartDetails.from_json(json)
# print the JSON string representation of the object
print ExtendedCartDetails.to_json()

# convert the object into a dict
extended_cart_details_dict = extended_cart_details_instance.to_dict()
# create an instance of ExtendedCartDetails from a dict
extended_cart_details_form_dict = extended_cart_details.from_dict(extended_cart_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


