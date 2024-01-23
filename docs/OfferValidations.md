# OfferValidations

Offer validation object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_amount** | **float** | Minimum Amount for Offer to be Applicable | [optional] 
**payment_method** | [**OfferValidationsPaymentMethod**](OfferValidationsPaymentMethod.md) |  | 

## Example

```python
from cashfree_pg.models.offer_validations import OfferValidations

# TODO update the JSON string below
json = "{}"
# create an instance of OfferValidations from a JSON string
offer_validations_instance = OfferValidations.from_json(json)
# print the JSON string representation of the object
print OfferValidations.to_json()

# convert the object into a dict
offer_validations_dict = offer_validations_instance.to_dict()
# create an instance of OfferValidations from a dict
offer_validations_form_dict = offer_validations.from_dict(offer_validations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


