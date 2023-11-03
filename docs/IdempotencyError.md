# IdempotencyError

Error when idempotency fails. Different request body with the same idempotent key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | **str** | idempotency_error | [optional] 

## Example

```python
from cashfree_pg.models.idempotency_error import IdempotencyError

# TODO update the JSON string below
json = "{}"
# create an instance of IdempotencyError from a JSON string
idempotency_error_instance = IdempotencyError.from_json(json)
# print the JSON string representation of the object
print IdempotencyError.to_json()

# convert the object into a dict
idempotency_error_dict = idempotency_error_instance.to_dict()
# create an instance of IdempotencyError from a dict
idempotency_error_form_dict = idempotency_error.from_dict(idempotency_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


