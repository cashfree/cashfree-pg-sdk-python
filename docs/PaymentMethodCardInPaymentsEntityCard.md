# PaymentMethodCardInPaymentsEntityCard


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
from cashfree_pg.models.payment_method_card_in_payments_entity_card import PaymentMethodCardInPaymentsEntityCard

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardInPaymentsEntityCard from a JSON string
payment_method_card_in_payments_entity_card_instance = PaymentMethodCardInPaymentsEntityCard.from_json(json)
# print the JSON string representation of the object
print PaymentMethodCardInPaymentsEntityCard.to_json()

# convert the object into a dict
payment_method_card_in_payments_entity_card_dict = payment_method_card_in_payments_entity_card_instance.to_dict()
# create an instance of PaymentMethodCardInPaymentsEntityCard from a dict
payment_method_card_in_payments_entity_card_form_dict = payment_method_card_in_payments_entity_card.from_dict(payment_method_card_in_payments_entity_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


