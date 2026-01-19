# CreateVendorResponse

Create Vendor Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**bank** | [**List[BankDetails]**](BankDetails.md) |  | [optional] 
**upi** | **str** |  | [optional] 
**phone** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**schedule_option** | [**List[ScheduleOption]**](ScheduleOption.md) |  | [optional] 
**kyc_details** | [**List[KycDetails]**](KycDetails.md) |  | [optional] 
**dashboard_access** | **bool** |  | [optional] 
**bank_details** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.create_vendor_response import CreateVendorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVendorResponse from a JSON string
create_vendor_response_instance = CreateVendorResponse.from_json(json)
# print the JSON string representation of the object
print CreateVendorResponse.to_json()

# convert the object into a dict
create_vendor_response_dict = create_vendor_response_instance.to_dict()
# create an instance of CreateVendorResponse from a dict
create_vendor_response_form_dict = create_vendor_response.from_dict(create_vendor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


