# SplitOrderReconSuccessResponse

Split Order Reconciliation Request Body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement** | [**SplitOrderReconSuccessResponseSettlement**](SplitOrderReconSuccessResponseSettlement.md) |  | [optional] 
**refunds** | **List[object]** | List of refunds associated with the order, if any. | [optional] 
**vendors** | [**List[SplitOrderReconSuccessResponseVendorsInner]**](SplitOrderReconSuccessResponseVendorsInner.md) | List of vendor settlements associated with the split settlement. | [optional] 

## Example

```python
from cashfree_pg.models.split_order_recon_success_response import SplitOrderReconSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SplitOrderReconSuccessResponse from a JSON string
split_order_recon_success_response_instance = SplitOrderReconSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(SplitOrderReconSuccessResponse.to_json())

# convert the object into a dict
split_order_recon_success_response_dict = split_order_recon_success_response_instance.to_dict()
# create an instance of SplitOrderReconSuccessResponse from a dict
split_order_recon_success_response_from_dict = SplitOrderReconSuccessResponse.from_dict(split_order_recon_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


