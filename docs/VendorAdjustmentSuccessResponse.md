# VendorAdjustmentSuccessResponse

Vendor Adjustment Success Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.vendor_adjustment_success_response import VendorAdjustmentSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VendorAdjustmentSuccessResponse from a JSON string
vendor_adjustment_success_response_instance = VendorAdjustmentSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(VendorAdjustmentSuccessResponse.to_json())

# convert the object into a dict
vendor_adjustment_success_response_dict = vendor_adjustment_success_response_instance.to_dict()
# create an instance of VendorAdjustmentSuccessResponse from a dict
vendor_adjustment_success_response_from_dict = VendorAdjustmentSuccessResponse.from_dict(vendor_adjustment_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


