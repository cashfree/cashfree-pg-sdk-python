# PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emi_amount** | **float** |  | [optional] 
**emi_tenure** | **float** |  | [optional] 
**emi_interest** | **float** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_card_emiin_payments_entity_emi_emi_details import PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails from a JSON string
payment_method_card_emiin_payments_entity_emi_emi_details_instance = PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails.to_json()

# convert the object into a dict
payment_method_card_emiin_payments_entity_emi_emi_details_dict = payment_method_card_emiin_payments_entity_emi_emi_details_instance.to_dict()
# create an instance of PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails from a dict
payment_method_card_emiin_payments_entity_emi_emi_details_form_dict = payment_method_card_emiin_payments_entity_emi_emi_details.from_dict(payment_method_card_emiin_payments_entity_emi_emi_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


