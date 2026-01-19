# PaymentMethodBankTransferInPaymentsEntityBanktransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**banktransfer_bank_name** | **str** |  | [optional] 
**banktransfer_ifsc** | **str** |  | [optional] 
**banktransfer_account_number** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_bank_transfer_in_payments_entity_banktransfer import PaymentMethodBankTransferInPaymentsEntityBanktransfer

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBankTransferInPaymentsEntityBanktransfer from a JSON string
payment_method_bank_transfer_in_payments_entity_banktransfer_instance = PaymentMethodBankTransferInPaymentsEntityBanktransfer.from_json(json)
# print the JSON string representation of the object
print PaymentMethodBankTransferInPaymentsEntityBanktransfer.to_json()

# convert the object into a dict
payment_method_bank_transfer_in_payments_entity_banktransfer_dict = payment_method_bank_transfer_in_payments_entity_banktransfer_instance.to_dict()
# create an instance of PaymentMethodBankTransferInPaymentsEntityBanktransfer from a dict
payment_method_bank_transfer_in_payments_entity_banktransfer_form_dict = payment_method_bank_transfer_in_payments_entity_banktransfer.from_dict(payment_method_bank_transfer_in_payments_entity_banktransfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


