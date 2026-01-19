# ProductConditions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The Action key in the conditions array specifies whether a condition should \&quot;ALLOW\&quot; or \&quot;DENY\&quot; the specified rule or feature | [optional] 
**key** | **str** | Specify what you&#39;re trying to configure, such as \&quot;features\&quot; | [optional] 
**values** | **List[str]** | Define the values you need to set within the conditions in this array, such as \&quot;checkoutCollectAddress\&quot;, \&quot;checkoutAuthenticate\&quot; | [optional] 

## Example

```python
from cashfree_pg.models.product_conditions import ProductConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ProductConditions from a JSON string
product_conditions_instance = ProductConditions.from_json(json)
# print the JSON string representation of the object
print ProductConditions.to_json()

# convert the object into a dict
product_conditions_dict = product_conditions_instance.to_dict()
# create an instance of ProductConditions from a dict
product_conditions_form_dict = product_conditions.from_dict(product_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


