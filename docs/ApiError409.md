# ApiError409

duplicate request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | **str** | invalid_request_error | [optional] 

## Example

```python
from cashfree_pg.models.api_error409 import ApiError409

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError409 from a JSON string
api_error409_instance = ApiError409.from_json(json)
# print the JSON string representation of the object
print ApiError409.to_json()

# convert the object into a dict
api_error409_dict = api_error409_instance.to_dict()
# create an instance of ApiError409 from a dict
api_error409_form_dict = api_error409.from_dict(api_error409_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


