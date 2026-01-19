# PaymentMethodBankTransferInPaymentsEntity

payment method bank transfer object in payment entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banktransfer** | [**PaymentMethodBankTransferInPaymentsEntityBanktransfer**](PaymentMethodBankTransferInPaymentsEntityBanktransfer.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_bank_transfer_in_payments_entity import PaymentMethodBankTransferInPaymentsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBankTransferInPaymentsEntity from a JSON string
payment_method_bank_transfer_in_payments_entity_instance = PaymentMethodBankTransferInPaymentsEntity.from_json(json)
# print the JSON string representation of the object
print PaymentMethodBankTransferInPaymentsEntity.to_json()

# convert the object into a dict
payment_method_bank_transfer_in_payments_entity_dict = payment_method_bank_transfer_in_payments_entity_instance.to_dict()
# create an instance of PaymentMethodBankTransferInPaymentsEntity from a dict
payment_method_bank_transfer_in_payments_entity_form_dict = payment_method_bank_transfer_in_payments_entity.from_dict(payment_method_bank_transfer_in_payments_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


