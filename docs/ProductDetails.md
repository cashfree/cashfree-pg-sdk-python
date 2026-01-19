# ProductDetails

Specify the required configurations for this feature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Option to enable or disable the feature | [optional] 
**conditions** | [**List[ProductConditions]**](ProductConditions.md) | The conditions array allows to configure rules by adding condition objects with specific parameters for feature configurations. | [optional] 

## Example

```python
from cashfree_pg.models.product_details import ProductDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetails from a JSON string
product_details_instance = ProductDetails.from_json(json)
# print the JSON string representation of the object
print ProductDetails.to_json()

# convert the object into a dict
product_details_dict = product_details_instance.to_dict()
# create an instance of ProductDetails from a dict
product_details_form_dict = product_details.from_dict(product_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


