# NetBankingPaymentMethod

Payment method for netbanking object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**netbanking** | [**Netbanking**](Netbanking.md) |  | 

## Example

```python
from cashfree_pg.models.net_banking_payment_method import NetBankingPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of NetBankingPaymentMethod from a JSON string
net_banking_payment_method_instance = NetBankingPaymentMethod.from_json(json)
# print the JSON string representation of the object
print NetBankingPaymentMethod.to_json()

# convert the object into a dict
net_banking_payment_method_dict = net_banking_payment_method_instance.to_dict()
# create an instance of NetBankingPaymentMethod from a dict
net_banking_payment_method_form_dict = net_banking_payment_method.from_dict(net_banking_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


