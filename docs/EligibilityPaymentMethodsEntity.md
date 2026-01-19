# EligibilityPaymentMethodsEntity

Eligible payment methods details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility** | **bool** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_value** | **str** |  | [optional] 
**entity_details** | [**EligibilityPaymentMethodsEntityEntityDetails**](EligibilityPaymentMethodsEntityEntityDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_payment_methods_entity import EligibilityPaymentMethodsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityPaymentMethodsEntity from a JSON string
eligibility_payment_methods_entity_instance = EligibilityPaymentMethodsEntity.from_json(json)
# print the JSON string representation of the object
print EligibilityPaymentMethodsEntity.to_json()

# convert the object into a dict
eligibility_payment_methods_entity_dict = eligibility_payment_methods_entity_instance.to_dict()
# create an instance of EligibilityPaymentMethodsEntity from a dict
eligibility_payment_methods_entity_form_dict = eligibility_payment_methods_entity.from_dict(eligibility_payment_methods_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


