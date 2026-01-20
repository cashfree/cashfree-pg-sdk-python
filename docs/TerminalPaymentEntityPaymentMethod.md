# TerminalPaymentEntityPaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**PaymentMethodCardInPaymentsEntityCard**](PaymentMethodCardInPaymentsEntityCard.md) |  | [optional] 
**netbanking** | [**PaymentMethodNetBankingInPaymentsEntityNetbanking**](PaymentMethodNetBankingInPaymentsEntityNetbanking.md) |  | [optional] 
**upi** | [**PaymentMethodUPIInPaymentsEntityUpi**](PaymentMethodUPIInPaymentsEntityUpi.md) |  | [optional] 
**app** | [**PaymentMethodAppInPaymentsEntityApp**](PaymentMethodAppInPaymentsEntityApp.md) |  | [optional] 
**cardless_emi** | [**PaymentMethodAppInPaymentsEntityApp**](PaymentMethodAppInPaymentsEntityApp.md) |  | [optional] 
**paylater** | [**PaymentMethodAppInPaymentsEntityApp**](PaymentMethodAppInPaymentsEntityApp.md) |  | [optional] 
**emi** | [**PaymentMethodCardEMIInPaymentsEntityEmi**](PaymentMethodCardEMIInPaymentsEntityEmi.md) |  | [optional] 
**banktransfer** | [**PaymentMethodBankTransferInPaymentsEntityBanktransfer**](PaymentMethodBankTransferInPaymentsEntityBanktransfer.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.terminal_payment_entity_payment_method import TerminalPaymentEntityPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalPaymentEntityPaymentMethod from a JSON string
terminal_payment_entity_payment_method_instance = TerminalPaymentEntityPaymentMethod.from_json(json)
# print the JSON string representation of the object
print(TerminalPaymentEntityPaymentMethod.to_json())

# convert the object into a dict
terminal_payment_entity_payment_method_dict = terminal_payment_entity_payment_method_instance.to_dict()
# create an instance of TerminalPaymentEntityPaymentMethod from a dict
terminal_payment_entity_payment_method_from_dict = TerminalPaymentEntityPaymentMethod.from_dict(terminal_payment_entity_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


