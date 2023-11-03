# UPIPaymentMethod

Complete payment method for UPI collect

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upi** | [**Upi**](Upi.md) |  | 

## Example

```python
from cashfree_pg.models.upi_payment_method import UPIPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of UPIPaymentMethod from a JSON string
upi_payment_method_instance = UPIPaymentMethod.from_json(json)
# print the JSON string representation of the object
print UPIPaymentMethod.to_json()

# convert the object into a dict
upi_payment_method_dict = upi_payment_method_instance.to_dict()
# create an instance of UPIPaymentMethod from a dict
upi_payment_method_form_dict = upi_payment_method.from_dict(upi_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


