# ESOrderReconResponse

ES Order Recon Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** |  | [optional] 
**data** | [**List[ESOrderReconResponseDataInner]**](ESOrderReconResponseDataInner.md) |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from cashfree_pg.models.es_order_recon_response import ESOrderReconResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ESOrderReconResponse from a JSON string
es_order_recon_response_instance = ESOrderReconResponse.from_json(json)
# print the JSON string representation of the object
print(ESOrderReconResponse.to_json())

# convert the object into a dict
es_order_recon_response_dict = es_order_recon_response_instance.to_dict()
# create an instance of ESOrderReconResponse from a dict
es_order_recon_response_from_dict = ESOrderReconResponse.from_dict(es_order_recon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


