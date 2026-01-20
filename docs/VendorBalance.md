# VendorBalance

Vendor Balance entity object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **float** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**merchant_unsettled** | **float** |  | [optional] 
**vendor_unsettled** | **float** |  | [optional] 

## Example

```python
from cashfree_pg.models.vendor_balance import VendorBalance

# TODO update the JSON string below
json = "{}"
# create an instance of VendorBalance from a JSON string
vendor_balance_instance = VendorBalance.from_json(json)
# print the JSON string representation of the object
print(VendorBalance.to_json())

# convert the object into a dict
vendor_balance_dict = vendor_balance_instance.to_dict()
# create an instance of VendorBalance from a dict
vendor_balance_from_dict = VendorBalance.from_dict(vendor_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


