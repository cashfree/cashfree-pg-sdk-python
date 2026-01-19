# SubscriptionEntitySubscriptionMeta

Subscription metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | Return URL for the subscription. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_entity_subscription_meta import SubscriptionEntitySubscriptionMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEntitySubscriptionMeta from a JSON string
subscription_entity_subscription_meta_instance = SubscriptionEntitySubscriptionMeta.from_json(json)
# print the JSON string representation of the object
print SubscriptionEntitySubscriptionMeta.to_json()

# convert the object into a dict
subscription_entity_subscription_meta_dict = subscription_entity_subscription_meta_instance.to_dict()
# create an instance of SubscriptionEntitySubscriptionMeta from a dict
subscription_entity_subscription_meta_form_dict = subscription_entity_subscription_meta.from_dict(subscription_entity_subscription_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


