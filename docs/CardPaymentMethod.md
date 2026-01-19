# CardPaymentMethod

The card payment object is used to make payment using either plain card number, saved card instrument id or using cryptogram 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**Card**](Card.md) |  | 

## Example

```python
from cashfree_pg.models.card_payment_method import CardPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of CardPaymentMethod from a JSON string
card_payment_method_instance = CardPaymentMethod.from_json(json)
# print the JSON string representation of the object
print CardPaymentMethod.to_json()

# convert the object into a dict
card_payment_method_dict = card_payment_method_instance.to_dict()
# create an instance of CardPaymentMethod from a dict
card_payment_method_form_dict = card_payment_method.from_dict(card_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


