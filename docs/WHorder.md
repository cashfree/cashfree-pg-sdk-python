# WHorder

order entity in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**order_amount** | **float** |  | [optional] 
**order_currency** | **str** |  | [optional] 
**order_tags** | **Dict[str, str]** | Custom Tags in thr form of {\&quot;key\&quot;:\&quot;value\&quot;} which can be passed for an order. A maximum of 10 tags can be added | [optional] 

## Example

```python
from cashfree_pg.models.w_horder import WHorder

# TODO update the JSON string below
json = "{}"
# create an instance of WHorder from a JSON string
w_horder_instance = WHorder.from_json(json)
# print the JSON string representation of the object
print WHorder.to_json()

# convert the object into a dict
w_horder_dict = w_horder_instance.to_dict()
# create an instance of WHorder from a dict
w_horder_form_dict = w_horder.from_dict(w_horder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


