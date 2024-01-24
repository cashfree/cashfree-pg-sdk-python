# PaymentMethodCardEMIInPaymentsEntityEmi


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**card_number** | **str** |  | [optional] 
**card_network** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**card_country** | **str** |  | [optional] 
**card_bank_name** | **str** |  | [optional] 
**card_network_reference_id** | **str** |  | [optional] 
**emi_tenure** | **float** |  | [optional] 
**emi_details** | [**PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails**](PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_card_emiin_payments_entity_emi import PaymentMethodCardEMIInPaymentsEntityEmi

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardEMIInPaymentsEntityEmi from a JSON string
payment_method_card_emiin_payments_entity_emi_instance = PaymentMethodCardEMIInPaymentsEntityEmi.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardEMIInPaymentsEntityEmi.to_json()

# convert the object into a dict
payment_method_card_emiin_payments_entity_emi_dict = payment_method_card_emiin_payments_entity_emi_instance.to_dict()
# create an instance of PaymentMethodCardEMIInPaymentsEntityEmi from a dict
payment_method_card_emiin_payments_entity_emi_form_dict = payment_method_card_emiin_payments_entity_emi.from_dict(payment_method_card_emiin_payments_entity_emi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


