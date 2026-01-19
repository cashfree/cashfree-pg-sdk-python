# CreateSubscriptionPaymentRequestCard

payment method card.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel. can be link | [optional] 
**card_number** | **str** | Card number | [optional] 
**card_holder_name** | **str** | Card holder name | [optional] 
**card_expiry_mm** | **str** | Card expiry month | [optional] 
**card_expiry_yy** | **str** | Card expiry year | [optional] 
**card_cvv** | **str** | Card CVV | [optional] 
**card_network** | **str** | Card network | [optional] 
**card_type** | **str** | Card type | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_payment_request_card import CreateSubscriptionPaymentRequestCard

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPaymentRequestCard from a JSON string
create_subscription_payment_request_card_instance = CreateSubscriptionPaymentRequestCard.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPaymentRequestCard.to_json()

# convert the object into a dict
create_subscription_payment_request_card_dict = create_subscription_payment_request_card_instance.to_dict()
# create an instance of CreateSubscriptionPaymentRequestCard from a dict
create_subscription_payment_request_card_form_dict = create_subscription_payment_request_card.from_dict(create_subscription_payment_request_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


