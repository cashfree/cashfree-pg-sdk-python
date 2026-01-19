# VendorEntity

Vendor entity object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**vendor_id** | **str** |  | [optional] 
**added_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**bank** | [**List[BankDetails]**](BankDetails.md) |  | [optional] 
**upi** | **str** |  | [optional] 
**schedule_option** | [**List[ScheduleOption]**](ScheduleOption.md) |  | [optional] 
**vendor_type** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**business_type** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 
**related_docs** | [**List[VendorEntityRelatedDocsInner]**](VendorEntityRelatedDocsInner.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.vendor_entity import VendorEntity

# TODO update the JSON string below
json = "{}"
# create an instance of VendorEntity from a JSON string
vendor_entity_instance = VendorEntity.from_json(json)
# print the JSON string representation of the object
print VendorEntity.to_json()

# convert the object into a dict
vendor_entity_dict = vendor_entity_instance.to_dict()
# create an instance of VendorEntity from a dict
vendor_entity_form_dict = vendor_entity.from_dict(vendor_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


