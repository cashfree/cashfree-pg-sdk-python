# ManageSubscriptionRequestActionDetails

Details of the action to be performed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_scheduled_time** | **str** | Next scheduled time for the action. Required for ACTIVATE action. | [optional] 
**plan_id** | **str** | Plan ID to update. Required for CHANGE_PLAN action. | [optional] 

## Example

```python
from cashfree_pg.models.manage_subscription_request_action_details import ManageSubscriptionRequestActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ManageSubscriptionRequestActionDetails from a JSON string
manage_subscription_request_action_details_instance = ManageSubscriptionRequestActionDetails.from_json(json)
# print the JSON string representation of the object
print ManageSubscriptionRequestActionDetails.to_json()

# convert the object into a dict
manage_subscription_request_action_details_dict = manage_subscription_request_action_details_instance.to_dict()
# create an instance of ManageSubscriptionRequestActionDetails from a dict
manage_subscription_request_action_details_form_dict = manage_subscription_request_action_details.from_dict(manage_subscription_request_action_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


