# CardEMIPaymentMethod

Complete card emi payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emi** | [**CardEMI**](CardEMI.md) |  | 

## Example

```python
from cashfree_pg.models.card_emi_payment_method import CardEMIPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of CardEMIPaymentMethod from a JSON string
card_emi_payment_method_instance = CardEMIPaymentMethod.from_json(json)
# print the JSON string representation of the object
print CardEMIPaymentMethod.to_json()

# convert the object into a dict
card_emi_payment_method_dict = card_emi_payment_method_instance.to_dict()
# create an instance of CardEMIPaymentMethod from a dict
card_emi_payment_method_form_dict = card_emi_payment_method.from_dict(card_emi_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


