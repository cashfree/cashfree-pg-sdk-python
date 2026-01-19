# AuthenticationError

Error if api keys are wrong

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | **str** | authentication_error | [optional] 

## Example

```python
from cashfree_pg.models.authentication_error import AuthenticationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationError from a JSON string
authentication_error_instance = AuthenticationError.from_json(json)
# print the JSON string representation of the object
print AuthenticationError.to_json()

# convert the object into a dict
authentication_error_dict = authentication_error_instance.to_dict()
# create an instance of AuthenticationError from a dict
authentication_error_form_dict = authentication_error.from_dict(authentication_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


