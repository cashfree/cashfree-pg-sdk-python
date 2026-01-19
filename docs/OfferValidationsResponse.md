# OfferValidationsResponse

Offer validation object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_allowed** | **float** | Maximum Amount for Offer to be Applicable | [optional] 
**min_amount** | **float** | Minimum Amount for Offer to be Applicable | [optional] 
**payment_method** | [**OfferValidationsResponsePaymentMethod**](OfferValidationsResponsePaymentMethod.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.offer_validations_response import OfferValidationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferValidationsResponse from a JSON string
offer_validations_response_instance = OfferValidationsResponse.from_json(json)
# print the JSON string representation of the object
print OfferValidationsResponse.to_json()

# convert the object into a dict
offer_validations_response_dict = offer_validations_response_instance.to_dict()
# create an instance of OfferValidationsResponse from a dict
offer_validations_response_form_dict = offer_validations_response.from_dict(offer_validations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


