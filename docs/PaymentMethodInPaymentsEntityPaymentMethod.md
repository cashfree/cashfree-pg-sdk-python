# PaymentMethodInPaymentsEntityPaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | 
**card_number** | **str** |  | [optional] 
**card_network** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**card_country** | **str** |  | [optional] 
**card_bank_name** | **str** |  | [optional] 
**card_network_reference_id** | **str** |  | [optional] 
**netbanking_bank_code** | **int** |  | 
**netbanking_bank_name** | **str** |  | 
**upi_id** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

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


