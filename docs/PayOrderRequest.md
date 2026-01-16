# PayOrderRequest

Complete object for the pay api that uses payment method objects

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_session_id** | **str** |  | 
**payment_method** | [**PayOrderRequestPaymentMethod**](PayOrderRequestPaymentMethod.md) |  | 
**save_instrument** | **bool** |  | [optional] 
**offer_id** | **str** | This is required if any offers needs to be applied to the order. | [optional] 

## Example

```python
from cashfree_pg.models.pay_order_request import PayOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayOrderRequest from a JSON string
pay_order_request_instance = PayOrderRequest.from_json(json)
# print the JSON string representation of the object
print PayOrderRequest.to_json()

# convert the object into a dict
pay_order_request_dict = pay_order_request_instance.to_dict()
# create an instance of PayOrderRequest from a dict
pay_order_request_form_dict = pay_order_request.from_dict(pay_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


