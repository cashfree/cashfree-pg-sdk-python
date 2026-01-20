# ESOrderReconResponseDataInnerOrderSplitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**split** | [**List[ESOrderReconResponseDataInnerOrderSplitsInnerSplitInner]**](ESOrderReconResponseDataInnerOrderSplitsInnerSplitInner.md) |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.es_order_recon_response_data_inner_order_splits_inner import ESOrderReconResponseDataInnerOrderSplitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ESOrderReconResponseDataInnerOrderSplitsInner from a JSON string
es_order_recon_response_data_inner_order_splits_inner_instance = ESOrderReconResponseDataInnerOrderSplitsInner.from_json(json)
# print the JSON string representation of the object
print(ESOrderReconResponseDataInnerOrderSplitsInner.to_json())

# convert the object into a dict
es_order_recon_response_data_inner_order_splits_inner_dict = es_order_recon_response_data_inner_order_splits_inner_instance.to_dict()
# create an instance of ESOrderReconResponseDataInnerOrderSplitsInner from a dict
es_order_recon_response_data_inner_order_splits_inner_from_dict = ESOrderReconResponseDataInnerOrderSplitsInner.from_dict(es_order_recon_response_data_inner_order_splits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


