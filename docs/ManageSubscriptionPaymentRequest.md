# ManageSubscriptionPaymentRequest

Request body to manage a subscription payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | The unique ID which was used to create subscription. | 
**payment_id** | **str** | The unique ID which was used to create payment. | 
**action** | **str** | Action to be performed on the payment. Possible values - CANCEL, RETRY. | 
**action_details** | [**ManageSubscriptionPaymentRequestActionDetails**](ManageSubscriptionPaymentRequestActionDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.manage_subscription_payment_request import ManageSubscriptionPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManageSubscriptionPaymentRequest from a JSON string
manage_subscription_payment_request_instance = ManageSubscriptionPaymentRequest.from_json(json)
# print the JSON string representation of the object
print ManageSubscriptionPaymentRequest.to_json()

# convert the object into a dict
manage_subscription_payment_request_dict = manage_subscription_payment_request_instance.to_dict()
# create an instance of ManageSubscriptionPaymentRequest from a dict
manage_subscription_payment_request_form_dict = manage_subscription_payment_request.from_dict(manage_subscription_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


