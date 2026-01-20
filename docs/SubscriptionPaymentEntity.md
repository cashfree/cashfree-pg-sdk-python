# SubscriptionPaymentEntity

The response returned in Get, Create or Manage Subscription Payment APIs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_details** | [**AuthorizationDetails**](AuthorizationDetails.md) |  | [optional] 
**cf_payment_id** | **str** | Cashfree subscription payment reference number | [optional] 
**cf_subscription_id** | **str** | Cashfree subscription reference number | [optional] 
**cf_txn_id** | **str** | Cashfree subscription payment transaction ID | [optional] 
**cf_order_id** | **str** | Cashfree subscription payment order ID | [optional] 
**failure_details** | [**SubscriptionPaymentEntityFailureDetails**](SubscriptionPaymentEntityFailureDetails.md) |  | [optional] 
**payment_amount** | **float** | The charge amount of the payment. | [optional] 
**payment_id** | **str** | A unique ID passed by merchant for identifying the transaction. | [optional] 
**payment_initiated_date** | **str** | The date on which the payment was initiated. | [optional] 
**payment_remarks** | **str** | Payment remarks. | [optional] 
**payment_schedule_date** | **str** | The date on which the payment is scheduled to be processed. | [optional] 
**payment_status** | **str** | Status of the payment. | [optional] 
**payment_type** | **str** | Payment type. Can be AUTH or CHARGE. | [optional] 
**retry_attempts** | **int** | Retry attempts. | [optional] 
**subscription_id** | **str** | A unique ID passed by merchant for identifying the subscription. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_payment_entity import SubscriptionPaymentEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaymentEntity from a JSON string
subscription_payment_entity_instance = SubscriptionPaymentEntity.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPaymentEntity.to_json())

# convert the object into a dict
subscription_payment_entity_dict = subscription_payment_entity_instance.to_dict()
# create an instance of SubscriptionPaymentEntity from a dict
subscription_payment_entity_from_dict = SubscriptionPaymentEntity.from_dict(subscription_payment_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


