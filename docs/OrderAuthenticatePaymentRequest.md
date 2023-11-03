# OrderAuthenticatePaymentRequest

OTP to be submitted for headless/native OTP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** | OTP to be submitted | 
**action** | **str** | The action for this workflow. Could be either SUBMIT_OTP or RESEND_OTP | 

## Example

```python
from cashfree_pg.models.order_authenticate_payment_request import OrderAuthenticatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderAuthenticatePaymentRequest from a JSON string
order_authenticate_payment_request_instance = OrderAuthenticatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print OrderAuthenticatePaymentRequest.to_json()

# convert the object into a dict
order_authenticate_payment_request_dict = order_authenticate_payment_request_instance.to_dict()
# create an instance of OrderAuthenticatePaymentRequest from a dict
order_authenticate_payment_request_form_dict = order_authenticate_payment_request.from_dict(order_authenticate_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


