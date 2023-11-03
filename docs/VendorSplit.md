# VendorSplit

Use to split order when cashfree's Easy Split is enabled for your account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** | Vendor id created in Cashfree system | [optional] 
**amount** | **float** | Amount which will be associated with this vendor | [optional] 
**percentage** | **float** | Percentage of order amount which shall get added to vendor account | [optional] 

## Example

```python
from cashfree_pg.models.vendor_split import VendorSplit

# TODO update the JSON string below
json = "{}"
# create an instance of VendorSplit from a JSON string
vendor_split_instance = VendorSplit.from_json(json)
# print the JSON string representation of the object
print VendorSplit.to_json()

# convert the object into a dict
vendor_split_dict = vendor_split_instance.to_dict()
# create an instance of VendorSplit from a dict
vendor_split_form_dict = vendor_split.from_dict(vendor_split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


