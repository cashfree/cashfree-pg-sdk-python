# PaymentMethodCardInPaymentsEntity

payment method card object in payment entity

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

## Example

```python
from cashfree_pg.models.payment_method_card_in_payments_entity import PaymentMethodCardInPaymentsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardInPaymentsEntity from a JSON string
payment_method_card_in_payments_entity_instance = PaymentMethodCardInPaymentsEntity.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardInPaymentsEntity.to_json()

# convert the object into a dict
payment_method_card_in_payments_entity_dict = payment_method_card_in_payments_entity_instance.to_dict()
# create an instance of PaymentMethodCardInPaymentsEntity from a dict
payment_method_card_in_payments_entity_form_dict = payment_method_card_in_payments_entity.from_dict(payment_method_card_in_payments_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


