# UpdateVendorRequest

Update Vendor Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Specify the status of vendor that should be updated. Possible values: ACTIVE,BLOCKED, DELETED | 
**name** | **str** | Specify the name of the vendor to be updated. Name should not have any special character except . / - &amp; | 
**email** | **str** | Specify the vendor email ID that should be updated. String in email ID format (Ex:johndoe_1@cashfree.com) should contain @ and dot (.) | 
**phone** | **str** | Specify the beneficiaries phone number to be updated. Phone number registered in India (only digits, 8 - 12 characters after excluding +91). | 
**verify_account** | **bool** | Specify if the vendor bank account details should be verified. Possible values: true or false | [optional] 
**dashboard_access** | **bool** | Update if the vendor will have dashboard access or not. Possible values are: true or false | [optional] 
**schedule_option** | **float** | Specify the settlement cycle to be updated. View the settlement cycle details from the \&quot;Settlement Cycles Supported\&quot; table. If no schedule option is configured, the settlement cycle ID \&quot;1\&quot; will be in effect. Select \&quot;8\&quot; or \&quot;9\&quot; if you want to schedule instant vendor settlements. | 
**bank** | [**List[BankDetails]**](BankDetails.md) | Specify the vendor bank account details to be updated. | [optional] 
**upi** | [**List[UpiDetails]**](UpiDetails.md) | Updated beneficiary upi vpa. Alphanumeric, dot (.), hyphen (-), at sign (@), and underscore allowed (100 character limit). Note: underscore and dot (.) gets accepted before and after @, but hyphen (-) is only accepted before @ sign. | [optional] 
**kyc_details** | [**List[KycDetails]**](KycDetails.md) | Specify the kyc details that should be updated. | 

## Example

```python
from cashfree_pg.models.update_vendor_request import UpdateVendorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVendorRequest from a JSON string
update_vendor_request_instance = UpdateVendorRequest.from_json(json)
# print the JSON string representation of the object
print UpdateVendorRequest.to_json()

# convert the object into a dict
update_vendor_request_dict = update_vendor_request_instance.to_dict()
# create an instance of UpdateVendorRequest from a dict
update_vendor_request_form_dict = update_vendor_request.from_dict(update_vendor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


