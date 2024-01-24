# PaymentMethodCardlessEMIInPaymentsEntity

payment method carless object in payment entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardless_emi** | [**PaymentMethodAppInPaymentsEntityApp**](PaymentMethodAppInPaymentsEntityApp.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_cardless_emiin_payments_entity import PaymentMethodCardlessEMIInPaymentsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardlessEMIInPaymentsEntity from a JSON string
payment_method_cardless_emiin_payments_entity_instance = PaymentMethodCardlessEMIInPaymentsEntity.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardlessEMIInPaymentsEntity.to_json()

# convert the object into a dict
payment_method_cardless_emiin_payments_entity_dict = payment_method_cardless_emiin_payments_entity_instance.to_dict()
# create an instance of PaymentMethodCardlessEMIInPaymentsEntity from a dict
payment_method_cardless_emiin_payments_entity_form_dict = payment_method_cardless_emiin_payments_entity.from_dict(payment_method_cardless_emiin_payments_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


