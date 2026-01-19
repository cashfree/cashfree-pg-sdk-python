# KycDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** |  | [optional] 
**business_type** | **str** |  | [optional] 
**uidai** | **float** |  | [optional] 
**gst** | **str** |  | [optional] 
**cin** | **str** |  | [optional] 
**pan** | **str** |  | [optional] 
**passport_number** | **str** |  | [optional] 
**driving_license** | **str** |  | [optional] 
**voter_id** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.kyc_details import KycDetails

# TODO update the JSON string below
json = "{}"
# create an instance of KycDetails from a JSON string
kyc_details_instance = KycDetails.from_json(json)
# print the JSON string representation of the object
print KycDetails.to_json()

# convert the object into a dict
kyc_details_dict = kyc_details_instance.to_dict()
# create an instance of KycDetails from a dict
kyc_details_form_dict = kyc_details.from_dict(kyc_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


