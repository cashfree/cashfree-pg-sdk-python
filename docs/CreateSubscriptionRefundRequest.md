# CreateSubscriptionRefundRequest

Request body to create a subscription refund.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | A unique ID passed by merchant for identifying the subscription. | 
**payment_id** | **str** | A unique ID passed by merchant for identifying the transaction. | [optional] 
**cf_payment_id** | **str** | Cashfree subscription payment reference number. | [optional] 
**refund_id** | **str** | A unique ID passed by merchant for identifying the refund. | 
**refund_amount** | **float** | The amount to be refunded. Can be partial or full amount of the payment. | 
**refund_note** | **str** | Refund note. | [optional] 
**refund_speed** | **str** | Refund speed. Can be INSTANT or STANDARD. UPI supports only STANDARD refunds, Enach and Pnach supports only INSTANT refunds. | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_refund_request import CreateSubscriptionRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRefundRequest from a JSON string
create_subscription_refund_request_instance = CreateSubscriptionRefundRequest.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionRefundRequest.to_json()

# convert the object into a dict
create_subscription_refund_request_dict = create_subscription_refund_request_instance.to_dict()
# create an instance of CreateSubscriptionRefundRequest from a dict
create_subscription_refund_request_form_dict = create_subscription_refund_request.from_dict(create_subscription_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


