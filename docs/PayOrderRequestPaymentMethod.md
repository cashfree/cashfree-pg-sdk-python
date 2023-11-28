# PayOrderRequestPaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**Card**](Card.md) |  | 
**upi** | [**Upi**](Upi.md) |  | 
**netbanking** | [**Netbanking**](Netbanking.md) |  | 
**app** | [**App**](App.md) |  | 
**emi** | [**CardEMI**](CardEMI.md) |  | 
**cardless_emi** | [**CardlessEMI**](CardlessEMI.md) |  | 
**paylater** | [**Paylater**](Paylater.md) |  | 

## Example

```python
from cashfree_pg.models.pay_order_request_payment_method import PayOrderRequestPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PayOrderRequestPaymentMethod from a JSON string
pay_order_request_payment_method_instance = PayOrderRequestPaymentMethod.from_json(json)
# print the JSON string representation of the object
print PayOrderRequestPaymentMethod.to_json()

# convert the object into a dict
pay_order_request_payment_method_dict = pay_order_request_payment_method_instance.to_dict()
# create an instance of PayOrderRequestPaymentMethod from a dict
pay_order_request_payment_method_form_dict = pay_order_request_payment_method.from_dict(pay_order_request_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


