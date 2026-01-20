# SplitOrderReconSuccessResponseVendorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** | Unique identifier for the vendor. | [optional] 
**settlement_id** | **int** | Settlement ID associated with the vendor. | [optional] 
**settlement_amount** | **float** | Settlement amount allocated to the vendor. | [optional] 
**settlement_eligibility_date** | **datetime** | Date and time when the vendor is eligible for the settlement. | [optional] 

## Example

```python
from cashfree_pg.models.split_order_recon_success_response_vendors_inner import SplitOrderReconSuccessResponseVendorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SplitOrderReconSuccessResponseVendorsInner from a JSON string
split_order_recon_success_response_vendors_inner_instance = SplitOrderReconSuccessResponseVendorsInner.from_json(json)
# print the JSON string representation of the object
print(SplitOrderReconSuccessResponseVendorsInner.to_json())

# convert the object into a dict
split_order_recon_success_response_vendors_inner_dict = split_order_recon_success_response_vendors_inner_instance.to_dict()
# create an instance of SplitOrderReconSuccessResponseVendorsInner from a dict
split_order_recon_success_response_vendors_inner_from_dict = SplitOrderReconSuccessResponseVendorsInner.from_dict(split_order_recon_success_response_vendors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


