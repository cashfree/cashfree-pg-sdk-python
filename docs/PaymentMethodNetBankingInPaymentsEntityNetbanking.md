# PaymentMethodNetBankingInPaymentsEntityNetbanking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**netbanking_bank_code** | **int** |  | [optional] 
**netbanking_bank_name** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_net_banking_in_payments_entity_netbanking import PaymentMethodNetBankingInPaymentsEntityNetbanking

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodNetBankingInPaymentsEntityNetbanking from a JSON string
payment_method_net_banking_in_payments_entity_netbanking_instance = PaymentMethodNetBankingInPaymentsEntityNetbanking.from_json(json)
# print the JSON string representation of the object
print PaymentMethodNetBankingInPaymentsEntityNetbanking.to_json()

# convert the object into a dict
payment_method_net_banking_in_payments_entity_netbanking_dict = payment_method_net_banking_in_payments_entity_netbanking_instance.to_dict()
# create an instance of PaymentMethodNetBankingInPaymentsEntityNetbanking from a dict
payment_method_net_banking_in_payments_entity_netbanking_form_dict = payment_method_net_banking_in_payments_entity_netbanking.from_dict(payment_method_net_banking_in_payments_entity_netbanking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


