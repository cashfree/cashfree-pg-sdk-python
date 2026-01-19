# CreateSubscriptionRequest

Request body to create a new subscription.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | A unique ID for the subscription. It can include alphanumeric characters, underscore, dot, hyphen, and space. Maximum characters allowed is 250. | 
**customer_details** | [**SubscriptionCustomerDetails**](SubscriptionCustomerDetails.md) |  | 
**plan_details** | [**CreateSubscriptionRequestPlanDetails**](CreateSubscriptionRequestPlanDetails.md) |  | 
**authorization_details** | [**CreateSubscriptionRequestAuthorizationDetails**](CreateSubscriptionRequestAuthorizationDetails.md) |  | [optional] 
**subscription_meta** | [**CreateSubscriptionRequestSubscriptionMeta**](CreateSubscriptionRequestSubscriptionMeta.md) |  | [optional] 
**subscription_expiry_time** | **str** | Expiry date for the subscription. | [optional] 
**subscription_first_charge_time** | **str** | Time at which the first charge will be made for the subscription after authorization. Applicable only for PERIODIC plans. | [optional] 
**subscription_note** | **str** | Note for the subscription. | [optional] 
**subscription_tags** | **object** | Tags for the subscription. | [optional] 
**subscription_payment_splits** | [**List[SubscriptionPaymentSplitItem]**](SubscriptionPaymentSplitItem.md) | Payment splits for the subscription. | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_request import CreateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequest from a JSON string
create_subscription_request_instance = CreateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionRequest.to_json()

# convert the object into a dict
create_subscription_request_dict = create_subscription_request_instance.to_dict()
# create an instance of CreateSubscriptionRequest from a dict
create_subscription_request_form_dict = create_subscription_request.from_dict(create_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


