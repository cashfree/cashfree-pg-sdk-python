# EligibilityPaymentMethodsEntityEntityDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_details** | [**List[PaymentModeDetails]**](PaymentModeDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_payment_methods_entity_entity_details import EligibilityPaymentMethodsEntityEntityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityPaymentMethodsEntityEntityDetails from a JSON string
eligibility_payment_methods_entity_entity_details_instance = EligibilityPaymentMethodsEntityEntityDetails.from_json(json)
# print the JSON string representation of the object
print EligibilityPaymentMethodsEntityEntityDetails.to_json()

# convert the object into a dict
eligibility_payment_methods_entity_entity_details_dict = eligibility_payment_methods_entity_entity_details_instance.to_dict()
# create an instance of EligibilityPaymentMethodsEntityEntityDetails from a dict
eligibility_payment_methods_entity_entity_details_form_dict = eligibility_payment_methods_entity_entity_details.from_dict(eligibility_payment_methods_entity_entity_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


