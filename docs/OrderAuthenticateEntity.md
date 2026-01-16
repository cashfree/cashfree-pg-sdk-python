# OrderAuthenticateEntity

This is the response shared when merchant inovkes the OTP submit or resend API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_payment_id** | **str** | The payment id for which this request was sent | [optional] 
**action** | **str** | The action that was invoked for this request. | [optional] 
**authenticate_status** | **str** | Status of the is action. Will be either failed or successful. If the action is successful, you should still call the authorization status to verify the final payment status. | [optional] 
**payment_message** | **str** | Human readable message which describes the status in more detail | [optional] 

## Example

```python
from cashfree_pg.models.order_authenticate_entity import OrderAuthenticateEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OrderAuthenticateEntity from a JSON string
order_authenticate_entity_instance = OrderAuthenticateEntity.from_json(json)
# print the JSON string representation of the object
print OrderAuthenticateEntity.to_json()

# convert the object into a dict
order_authenticate_entity_dict = order_authenticate_entity_instance.to_dict()
# create an instance of OrderAuthenticateEntity from a dict
order_authenticate_entity_form_dict = order_authenticate_entity.from_dict(order_authenticate_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


