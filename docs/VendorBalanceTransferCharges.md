# VendorBalanceTransferCharges

Vendor Balance Transfer Charges entity object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_charges** | **float** |  | [optional] 
**service_tax** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**billed_to** | **str** |  | [optional] 
**is_postpaid** | **bool** |  | [optional] 

## Example

```python
from cashfree_pg.models.vendor_balance_transfer_charges import VendorBalanceTransferCharges

# TODO update the JSON string below
json = "{}"
# create an instance of VendorBalanceTransferCharges from a JSON string
vendor_balance_transfer_charges_instance = VendorBalanceTransferCharges.from_json(json)
# print the JSON string representation of the object
print VendorBalanceTransferCharges.to_json()

# convert the object into a dict
vendor_balance_transfer_charges_dict = vendor_balance_transfer_charges_instance.to_dict()
# create an instance of VendorBalanceTransferCharges from a dict
vendor_balance_transfer_charges_form_dict = vendor_balance_transfer_charges.from_dict(vendor_balance_transfer_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


