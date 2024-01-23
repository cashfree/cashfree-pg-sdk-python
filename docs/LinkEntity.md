# LinkEntity

Payment link success creation response object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_link_id** | **int** |  | [optional] 
**link_id** | **str** |  | [optional] 
**link_status** | **str** |  | [optional] 
**link_currency** | **str** |  | [optional] 
**link_amount** | **float** |  | [optional] 
**link_amount_paid** | **float** |  | [optional] 
**link_partial_payments** | **bool** |  | [optional] 
**link_minimum_partial_amount** | **float** |  | [optional] 
**link_purpose** | **str** |  | [optional] 
**link_created_at** | **str** |  | [optional] 
**customer_details** | [**LinkCustomerDetailsEntity**](LinkCustomerDetailsEntity.md) |  | [optional] 
**link_meta** | **Dict[str, str]** | Payment link meta information object. | [optional] 
**link_url** | **str** |  | [optional] 
**link_expiry_time** | **str** |  | [optional] 
**link_notes** | **Dict[str, str]** | Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs | [optional] 
**link_auto_reminders** | **bool** |  | [optional] 
**link_notify** | [**LinkNotifyEntity**](LinkNotifyEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.link_entity import LinkEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LinkEntity from a JSON string
link_entity_instance = LinkEntity.from_json(json)
# print the JSON string representation of the object
print LinkEntity.to_json()

# convert the object into a dict
link_entity_dict = link_entity_instance.to_dict()
# create an instance of LinkEntity from a dict
link_entity_form_dict = link_entity.from_dict(link_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


