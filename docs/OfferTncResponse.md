# OfferTncResponse

Offer terms and condition object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_tnc_type** | **str** | TnC Type for the Offer. It can be either &#x60;text&#x60; or &#x60;link&#x60; | [optional] 
**offer_tnc_value** | **str** | TnC for the Offer. | [optional] 

## Example

```python
from cashfree_pg.models.offer_tnc_response import OfferTncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferTncResponse from a JSON string
offer_tnc_response_instance = OfferTncResponse.from_json(json)
# print the JSON string representation of the object
print OfferTncResponse.to_json()

# convert the object into a dict
offer_tnc_response_dict = offer_tnc_response_instance.to_dict()
# create an instance of OfferTncResponse from a dict
offer_tnc_response_form_dict = offer_tnc_response.from_dict(offer_tnc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


