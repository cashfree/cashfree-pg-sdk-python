# SubscriptionPaymentEntityFailureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_reason** | **str** | Failure reason of the payment if the payment_status is failed. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_payment_entity_failure_details import SubscriptionPaymentEntityFailureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaymentEntityFailureDetails from a JSON string
subscription_payment_entity_failure_details_instance = SubscriptionPaymentEntityFailureDetails.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPaymentEntityFailureDetails.to_json())

# convert the object into a dict
subscription_payment_entity_failure_details_dict = subscription_payment_entity_failure_details_instance.to_dict()
# create an instance of SubscriptionPaymentEntityFailureDetails from a dict
subscription_payment_entity_failure_details_from_dict = SubscriptionPaymentEntityFailureDetails.from_dict(subscription_payment_entity_failure_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


