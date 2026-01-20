# UpdateVendorResponse

Update Vendor Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**bank** | [**List[BankDetails]**](BankDetails.md) |  | [optional] 
**upi** | **str** |  | [optional] 
**added_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**vendor_type** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**business_type** | **str** |  | [optional] 
**phone** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**schedule_option** | [**List[ScheduleOption]**](ScheduleOption.md) |  | [optional] 
**kyc_details** | [**List[KycDetails]**](KycDetails.md) |  | [optional] 
**dashboard_access** | **bool** |  | [optional] 
**bank_details** | **str** |  | [optional] 
**related_docs** | [**List[VendorEntityRelatedDocsInner]**](VendorEntityRelatedDocsInner.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.update_vendor_response import UpdateVendorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVendorResponse from a JSON string
update_vendor_response_instance = UpdateVendorResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateVendorResponse.to_json())

# convert the object into a dict
update_vendor_response_dict = update_vendor_response_instance.to_dict()
# create an instance of UpdateVendorResponse from a dict
update_vendor_response_from_dict = UpdateVendorResponse.from_dict(update_vendor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


