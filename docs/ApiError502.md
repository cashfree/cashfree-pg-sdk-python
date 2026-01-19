# ApiError502

Error when there is error at partner bank

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**code** | **str** | &#x60;bank_processing_failure&#x60; will be returned here to denote failure at bank.  | [optional] 
**type** | **str** | api_error | [optional] 

## Example

```python
from cashfree_pg.models.api_error502 import ApiError502

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError502 from a JSON string
api_error502_instance = ApiError502.from_json(json)
# print the JSON string representation of the object
print ApiError502.to_json()

# convert the object into a dict
api_error502_dict = api_error502_instance.to_dict()
# create an instance of ApiError502 from a dict
api_error502_form_dict = api_error502.from_dict(api_error502_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


