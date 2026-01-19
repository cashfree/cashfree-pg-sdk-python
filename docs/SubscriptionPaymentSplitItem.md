# SubscriptionPaymentSplitItem

Subscription Payment Split Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** | Vendor ID | [optional] 
**percentage** | **float** | Percentage of the payment to be split to vendor | [optional] 

## Example

```python
from cashfree_pg.models.subscription_payment_split_item import SubscriptionPaymentSplitItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaymentSplitItem from a JSON string
subscription_payment_split_item_instance = SubscriptionPaymentSplitItem.from_json(json)
# print the JSON string representation of the object
print SubscriptionPaymentSplitItem.to_json()

# convert the object into a dict
subscription_payment_split_item_dict = subscription_payment_split_item_instance.to_dict()
# create an instance of SubscriptionPaymentSplitItem from a dict
subscription_payment_split_item_form_dict = subscription_payment_split_item.from_dict(subscription_payment_split_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


