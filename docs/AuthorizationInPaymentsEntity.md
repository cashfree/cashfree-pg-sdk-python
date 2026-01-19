# AuthorizationInPaymentsEntity

If preauth enabled for account you will get this body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | One of CAPTURE or VOID | [optional] 
**status** | **str** | One of SUCCESS or PENDING | [optional] 
**captured_amount** | **float** | The captured amount for this authorization request | [optional] 
**start_time** | **str** | Start time of this authorization hold (only for UPI) | [optional] 
**end_time** | **str** | End time of this authorization hold (only for UPI) | [optional] 
**approve_by** | **str** | Approve by time as passed in the authorization request (only for UPI) | [optional] 
**action_reference** | **str** | CAPTURE or VOID reference number based on action  | [optional] 
**action_time** | **str** | Time of action (CAPTURE or VOID) | [optional] 

## Example

```python
from cashfree_pg.models.authorization_in_payments_entity import AuthorizationInPaymentsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationInPaymentsEntity from a JSON string
authorization_in_payments_entity_instance = AuthorizationInPaymentsEntity.from_json(json)
# print the JSON string representation of the object
print AuthorizationInPaymentsEntity.to_json()

# convert the object into a dict
authorization_in_payments_entity_dict = authorization_in_payments_entity_instance.to_dict()
# create an instance of AuthorizationInPaymentsEntity from a dict
authorization_in_payments_entity_form_dict = authorization_in_payments_entity.from_dict(authorization_in_payments_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


