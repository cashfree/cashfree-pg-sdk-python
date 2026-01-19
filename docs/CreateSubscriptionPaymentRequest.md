# CreateSubscriptionPaymentRequest

The request to be passed for the create subscription payment API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | A unique ID passed by merchant for identifying the subscription. | 
**subscription_session_id** | **str** | Session ID for the subscription. Required only for Auth. | [optional] 
**payment_id** | **str** | A unique ID passed by merchant for identifying the subscription payment. | 
**payment_amount** | **float** | The charge amount of the payment. Required in case of charge. | [optional] 
**payment_schedule_date** | **str** | The date on which the payment is scheduled to be processed. Required for UPI and CARD payment modes. | [optional] 
**payment_remarks** | **str** | Payment remarks. | [optional] 
**payment_type** | **str** | Payment type. Can be AUTH or CHARGE. | 
**payment_method** | [**CreateSubscriptionPaymentRequestPaymentMethod**](CreateSubscriptionPaymentRequestPaymentMethod.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_payment_request import CreateSubscriptionPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPaymentRequest from a JSON string
create_subscription_payment_request_instance = CreateSubscriptionPaymentRequest.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPaymentRequest.to_json()

# convert the object into a dict
create_subscription_payment_request_dict = create_subscription_payment_request_instance.to_dict()
# create an instance of CreateSubscriptionPaymentRequest from a dict
create_subscription_payment_request_form_dict = create_subscription_payment_request.from_dict(create_subscription_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


