# OrderPayData

the data object pay api

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 
**content_type** | **str** |  | [optional] 
**method** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.order_pay_data import OrderPayData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderPayData from a JSON string
order_pay_data_instance = OrderPayData.from_json(json)
# print the JSON string representation of the object
print OrderPayData.to_json()

# convert the object into a dict
order_pay_data_dict = order_pay_data_instance.to_dict()
# create an instance of OrderPayData from a dict
order_pay_data_form_dict = order_pay_data.from_dict(order_pay_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


