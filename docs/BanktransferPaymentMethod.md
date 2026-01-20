# BanktransferPaymentMethod

banktransfer payment method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banktransfer** | [**Banktransfer**](Banktransfer.md) |  | 

## Example

```python
from cashfree_pg.models.banktransfer_payment_method import BanktransferPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of BanktransferPaymentMethod from a JSON string
banktransfer_payment_method_instance = BanktransferPaymentMethod.from_json(json)
# print the JSON string representation of the object
print(BanktransferPaymentMethod.to_json())

# convert the object into a dict
banktransfer_payment_method_dict = banktransfer_payment_method_instance.to_dict()
# create an instance of BanktransferPaymentMethod from a dict
banktransfer_payment_method_from_dict = BanktransferPaymentMethod.from_dict(banktransfer_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


