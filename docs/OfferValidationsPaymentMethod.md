# OfferValidationsPaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **object** | All offers applicable | 
**card** | [**CardOffer**](CardOffer.md) |  | 
**netbanking** | [**OfferNBNetbanking**](OfferNBNetbanking.md) |  | 
**app** | [**WalletOffer**](WalletOffer.md) |  | 
**upi** | **object** |  | 
**paylater** | [**PaylaterOffer**](PaylaterOffer.md) |  | 
**emi** | [**EMIOffer**](EMIOffer.md) |  | 

## Example

```python
from cashfree_pg.models.offer_validations_payment_method import OfferValidationsPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of OfferValidationsPaymentMethod from a JSON string
offer_validations_payment_method_instance = OfferValidationsPaymentMethod.from_json(json)
# print the JSON string representation of the object
print OfferValidationsPaymentMethod.to_json()

# convert the object into a dict
offer_validations_payment_method_dict = offer_validations_payment_method_instance.to_dict()
# create an instance of OfferValidationsPaymentMethod from a dict
offer_validations_payment_method_form_dict = offer_validations_payment_method.from_dict(offer_validations_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


