# VendorAdjustmentRequest

Vendor Adjustment Request Body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** | The unique identifier of the vendor to whom the adjustment is applied | 
**adjustment_id** | **int** | The unique identifier for the adjustment transaction. | 
**amount** | **float** | The adjustment amount to be applied. | 
**type** | **str** | The type of adjustment. Possible values: CREDIT, DEBIT. | 
**remarks** | **str** | Remarks for the adjustment transaction, if any. | [optional] 

## Example

```python
from cashfree_pg.models.vendor_adjustment_request import VendorAdjustmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VendorAdjustmentRequest from a JSON string
vendor_adjustment_request_instance = VendorAdjustmentRequest.from_json(json)
# print the JSON string representation of the object
print(VendorAdjustmentRequest.to_json())

# convert the object into a dict
vendor_adjustment_request_dict = vendor_adjustment_request_instance.to_dict()
# create an instance of VendorAdjustmentRequest from a dict
vendor_adjustment_request_from_dict = VendorAdjustmentRequest.from_dict(vendor_adjustment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


