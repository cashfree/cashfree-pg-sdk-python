# AdjustVendorBalanceRequest

Adjust Vendor Balance Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_from** | **str** | Mention to whom you want to transfer the on demand balance. Possible values - MERCHANT, VENDOR. | 
**transfer_type** | **str** | Mention the type of transfer. Possible values: ON_DEMAND. | 
**transfer_amount** | **float** | Mention the on demand transfer amount. | 
**remark** | **str** | Mention remarks if any for the on demand transfer. | [optional] 
**tags** | **object** | Provide additional data fields using tags. | [optional] 

## Example

```python
from cashfree_pg.models.adjust_vendor_balance_request import AdjustVendorBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustVendorBalanceRequest from a JSON string
adjust_vendor_balance_request_instance = AdjustVendorBalanceRequest.from_json(json)
# print the JSON string representation of the object
print AdjustVendorBalanceRequest.to_json()

# convert the object into a dict
adjust_vendor_balance_request_dict = adjust_vendor_balance_request_instance.to_dict()
# create an instance of AdjustVendorBalanceRequest from a dict
adjust_vendor_balance_request_form_dict = adjust_vendor_balance_request.from_dict(adjust_vendor_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


