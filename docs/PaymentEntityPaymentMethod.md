# PaymentEntityPaymentMethod


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
from cashfree_pg.models.payment_entity_payment_method import PaymentEntityPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEntityPaymentMethod from a JSON string
payment_entity_payment_method_instance = PaymentEntityPaymentMethod.from_json(json)
# print the JSON string representation of the object
print PaymentEntityPaymentMethod.to_json()

# convert the object into a dict
payment_entity_payment_method_dict = payment_entity_payment_method_instance.to_dict()
# create an instance of PaymentEntityPaymentMethod from a dict
payment_entity_payment_method_form_dict = payment_entity_payment_method.from_dict(payment_entity_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


