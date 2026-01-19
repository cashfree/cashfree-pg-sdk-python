# CreateSubscriptionRequestSubscriptionMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | The url to redirect after checkout. | [optional] 
**notification_channel** | **List[str]** | Notification channel for the subscription. SMS, EMAIL are possible values. | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_request_subscription_meta import CreateSubscriptionRequestSubscriptionMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequestSubscriptionMeta from a JSON string
create_subscription_request_subscription_meta_instance = CreateSubscriptionRequestSubscriptionMeta.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionRequestSubscriptionMeta.to_json()

# convert the object into a dict
create_subscription_request_subscription_meta_dict = create_subscription_request_subscription_meta_instance.to_dict()
# create an instance of CreateSubscriptionRequestSubscriptionMeta from a dict
create_subscription_request_subscription_meta_form_dict = create_subscription_request_subscription_meta.from_dict(create_subscription_request_subscription_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


