# SubscriptionEntity

The response returned for Get, Create or Manage Subscription APIs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorisation_details** | [**AuthorizationDetails**](AuthorizationDetails.md) |  | [optional] 
**cf_subscription_id** | **str** | Cashfree subscription reference number | [optional] 
**customer_details** | [**SubscriptionCustomerDetails**](SubscriptionCustomerDetails.md) |  | [optional] 
**plan_details** | [**PlanEntity**](PlanEntity.md) |  | [optional] 
**subscription_expiry_time** | **str** | Time at which the subscription will expire. | [optional] 
**subscription_first_charge_time** | **str** | Time at which the first charge will be made for the subscription. Applicable only for PERIODIC plans. | [optional] 
**subscription_id** | **str** | A unique ID passed by merchant for identifying the subscription. | [optional] 
**subscription_meta** | [**SubscriptionEntitySubscriptionMeta**](SubscriptionEntitySubscriptionMeta.md) |  | [optional] 
**subscription_note** | **str** | Note for the subscription. | [optional] 
**subscription_session_id** | **str** | Subscription Session Id. | [optional] 
**subscription_payment_splits** | [**List[SubscriptionPaymentSplitItem]**](SubscriptionPaymentSplitItem.md) | Payment splits for the subscription. | [optional] 
**subscription_status** | **str** | Status of the subscription. | [optional] 
**subscription_tags** | **object** | Tags for the subscription. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_entity import SubscriptionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEntity from a JSON string
subscription_entity_instance = SubscriptionEntity.from_json(json)
# print the JSON string representation of the object
print SubscriptionEntity.to_json()

# convert the object into a dict
subscription_entity_dict = subscription_entity_instance.to_dict()
# create an instance of SubscriptionEntity from a dict
subscription_entity_form_dict = subscription_entity.from_dict(subscription_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


