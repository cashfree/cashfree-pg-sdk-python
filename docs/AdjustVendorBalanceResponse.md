# AdjustVendorBalanceResponse

Adjust Vendor Balance Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_id** | **float** |  | [optional] 
**transfer_details** | [**TransferDetails**](TransferDetails.md) |  | [optional] 
**balances** | [**BalanceDetails**](BalanceDetails.md) |  | [optional] 
**charges** | [**ChargesDetails**](ChargesDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.adjust_vendor_balance_response import AdjustVendorBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustVendorBalanceResponse from a JSON string
adjust_vendor_balance_response_instance = AdjustVendorBalanceResponse.from_json(json)
# print the JSON string representation of the object
print AdjustVendorBalanceResponse.to_json()

# convert the object into a dict
adjust_vendor_balance_response_dict = adjust_vendor_balance_response_instance.to_dict()
# create an instance of AdjustVendorBalanceResponse from a dict
adjust_vendor_balance_response_form_dict = adjust_vendor_balance_response.from_dict(adjust_vendor_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


