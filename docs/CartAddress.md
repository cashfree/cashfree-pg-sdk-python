# CartAddress

Address given for cart details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**pincode** | **str** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.cart_address import CartAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CartAddress from a JSON string
cart_address_instance = CartAddress.from_json(json)
# print the JSON string representation of the object
print CartAddress.to_json()

# convert the object into a dict
cart_address_dict = cart_address_instance.to_dict()
# create an instance of CartAddress from a dict
cart_address_form_dict = cart_address.from_dict(cart_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


