# PaymentMethodCardEMIInPaymentsEntity

payment method card emi object in payment entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emi** | [**PaymentMethodCardEMIInPaymentsEntityEmi**](PaymentMethodCardEMIInPaymentsEntityEmi.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_card_emiin_payments_entity import PaymentMethodCardEMIInPaymentsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardEMIInPaymentsEntity from a JSON string
payment_method_card_emiin_payments_entity_instance = PaymentMethodCardEMIInPaymentsEntity.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardEMIInPaymentsEntity.to_json()

# convert the object into a dict
payment_method_card_emiin_payments_entity_dict = payment_method_card_emiin_payments_entity_instance.to_dict()
# create an instance of PaymentMethodCardEMIInPaymentsEntity from a dict
payment_method_card_emiin_payments_entity_form_dict = payment_method_card_emiin_payments_entity.from_dict(payment_method_card_emiin_payments_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


