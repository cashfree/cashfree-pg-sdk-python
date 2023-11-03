# ErrorDetailsInPaymentsEntity

The error details are present only for failed payments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 
**error_reason** | **str** |  | [optional] 
**error_source** | **str** |  | [optional] 
**error_code_raw** | **str** |  | [optional] 
**error_description_raw** | **str** |  | [optional] 
**error_subcode_raw** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.error_details_in_payments_entity import ErrorDetailsInPaymentsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailsInPaymentsEntity from a JSON string
error_details_in_payments_entity_instance = ErrorDetailsInPaymentsEntity.from_json(json)
# print the JSON string representation of the object
print ErrorDetailsInPaymentsEntity.to_json()

# convert the object into a dict
error_details_in_payments_entity_dict = error_details_in_payments_entity_instance.to_dict()
# create an instance of ErrorDetailsInPaymentsEntity from a dict
error_details_in_payments_entity_form_dict = error_details_in_payments_entity.from_dict(error_details_in_payments_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


