# PaymentMethodInPaymentsEntityPaymentMethod


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

## Example

```python
from cashfree_pg.models.payment_method_in_payments_entity_payment_method import PaymentMethodInPaymentsEntityPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodInPaymentsEntityPaymentMethod from a JSON string
payment_method_in_payments_entity_payment_method_instance = PaymentMethodInPaymentsEntityPaymentMethod.from_json(json)
# print the JSON string representation of the object
print PaymentMethodInPaymentsEntityPaymentMethod.to_json()

# convert the object into a dict
payment_method_in_payments_entity_payment_method_dict = payment_method_in_payments_entity_payment_method_instance.to_dict()
# create an instance of PaymentMethodInPaymentsEntityPaymentMethod from a dict
payment_method_in_payments_entity_payment_method_form_dict = payment_method_in_payments_entity_payment_method.from_dict(payment_method_in_payments_entity_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


