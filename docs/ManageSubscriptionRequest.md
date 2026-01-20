# ManageSubscriptionRequest

Request body to manage a subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | The unique ID which was used to create subscription. | 
**action** | **str** | Action to be performed on the subscription. Possible values - CANCEL, PAUSE, ACTIVATE, CHANGE_PLAN. | 
**action_details** | [**ManageSubscriptionRequestActionDetails**](ManageSubscriptionRequestActionDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.manage_subscription_request import ManageSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManageSubscriptionRequest from a JSON string
manage_subscription_request_instance = ManageSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(ManageSubscriptionRequest.to_json())

# convert the object into a dict
manage_subscription_request_dict = manage_subscription_request_instance.to_dict()
# create an instance of ManageSubscriptionRequest from a dict
manage_subscription_request_from_dict = ManageSubscriptionRequest.from_dict(manage_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


