# ApiError404

Error when resource requested is not found

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | **str** | invalid_request_error | [optional] 

## Example

```python
from cashfree_pg.models.api_error404 import ApiError404

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError404 from a JSON string
api_error404_instance = ApiError404.from_json(json)
# print the JSON string representation of the object
print ApiError404.to_json()

# convert the object into a dict
api_error404_dict = api_error404_instance.to_dict()
# create an instance of ApiError404 from a dict
api_error404_form_dict = api_error404.from_dict(api_error404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


