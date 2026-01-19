# SubscriptionPaymentRefundEntity

Get/Create Subscription Payment Refund Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | A unique ID passed by merchant for identifying the transaction. | [optional] 
**cf_payment_id** | **str** | Cashfree subscription payment reference number. | [optional] 
**refund_id** | **str** | A unique ID passed by merchant for identifying the refund. | [optional] 
**cf_refund_id** | **str** | Cashfree subscription payment refund reference number. | [optional] 
**refund_amount** | **float** | The refund amount. | [optional] 
**refund_note** | **str** | Refund note. | [optional] 
**refund_speed** | **str** | Refund speed. Can be INSTANT or NORMAL. | [optional] 
**refund_status** | **str** | Status of the refund. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_payment_refund_entity import SubscriptionPaymentRefundEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaymentRefundEntity from a JSON string
subscription_payment_refund_entity_instance = SubscriptionPaymentRefundEntity.from_json(json)
# print the JSON string representation of the object
print SubscriptionPaymentRefundEntity.to_json()

# convert the object into a dict
subscription_payment_refund_entity_dict = subscription_payment_refund_entity_instance.to_dict()
# create an instance of SubscriptionPaymentRefundEntity from a dict
subscription_payment_refund_entity_form_dict = subscription_payment_refund_entity.from_dict(subscription_payment_refund_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


