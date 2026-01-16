# CreateSubscriptionPaymentResponse

The response returned is Create Subscription Auth or Charge APIs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_payment_id** | **str** | Cashfree subscription payment reference number | [optional] 
**failure_details** | [**SubscriptionPaymentEntityFailureDetails**](SubscriptionPaymentEntityFailureDetails.md) |  | [optional] 
**payment_amount** | **float** | The charge amount of the payment. | [optional] 
**payment_id** | **str** | A unique ID passed by merchant for identifying the transaction. | [optional] 
**payment_initiated_date** | **str** | The date on which the payment was initiated. | [optional] 
**payment_status** | **str** | Status of the payment. | [optional] 
**payment_type** | **str** | Payment type. Can be AUTH or CHARGE. | [optional] 
**subscription_id** | **str** | A unique ID passed by merchant for identifying the subscription. | [optional] 
**data** | **object** | Contains a payload for auth app links in case of AUTH. For charge, the payload is empty. | [optional] 
**payment_method** | **str** | Payment method used for the authorization. | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_payment_response import CreateSubscriptionPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPaymentResponse from a JSON string
create_subscription_payment_response_instance = CreateSubscriptionPaymentResponse.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPaymentResponse.to_json()

# convert the object into a dict
create_subscription_payment_response_dict = create_subscription_payment_response_instance.to_dict()
# create an instance of CreateSubscriptionPaymentResponse from a dict
create_subscription_payment_response_form_dict = create_subscription_payment_response.from_dict(create_subscription_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


