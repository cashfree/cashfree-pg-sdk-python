# ChargesEntity

Charges accociated with the order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_charges** | **float** | Shipping charge of the order | [optional] 
**cod_handling_charges** | **float** | COD handling fee for order | [optional] 

## Example

```python
from cashfree_pg.models.charges_entity import ChargesEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ChargesEntity from a JSON string
charges_entity_instance = ChargesEntity.from_json(json)
# print the JSON string representation of the object
print ChargesEntity.to_json()

# convert the object into a dict
charges_entity_dict = charges_entity_instance.to_dict()
# create an instance of ChargesEntity from a dict
charges_entity_form_dict = charges_entity.from_dict(charges_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


