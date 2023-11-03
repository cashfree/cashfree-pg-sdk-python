# OfferTnc

Offer terms and condition object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_tnc_type** | **str** | TnC Type for the Offer. It can be either &#x60;text&#x60; or &#x60;link&#x60; | 
**offer_tnc_value** | **str** | TnC for the Offer. | 

## Example

```python
from cashfree_pg.models.offer_tnc import OfferTnc

# TODO update the JSON string below
json = "{}"
# create an instance of OfferTnc from a JSON string
offer_tnc_instance = OfferTnc.from_json(json)
# print the JSON string representation of the object
print OfferTnc.to_json()

# convert the object into a dict
offer_tnc_dict = offer_tnc_instance.to_dict()
# create an instance of OfferTnc from a dict
offer_tnc_form_dict = offer_tnc.from_dict(offer_tnc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


