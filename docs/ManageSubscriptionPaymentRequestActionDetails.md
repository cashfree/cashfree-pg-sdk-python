# ManageSubscriptionPaymentRequestActionDetails

Details of the action to be performed. Needed for retry action.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_scheduled_time** | **str** | Next scheduled time for the retry of the FAILED payment. Required for retry action. | [optional] 

## Example

```python
from cashfree_pg.models.manage_subscription_payment_request_action_details import ManageSubscriptionPaymentRequestActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ManageSubscriptionPaymentRequestActionDetails from a JSON string
manage_subscription_payment_request_action_details_instance = ManageSubscriptionPaymentRequestActionDetails.from_json(json)
# print the JSON string representation of the object
print ManageSubscriptionPaymentRequestActionDetails.to_json()

# convert the object into a dict
manage_subscription_payment_request_action_details_dict = manage_subscription_payment_request_action_details_instance.to_dict()
# create an instance of ManageSubscriptionPaymentRequestActionDetails from a dict
manage_subscription_payment_request_action_details_form_dict = manage_subscription_payment_request_action_details.from_dict(manage_subscription_payment_request_action_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


