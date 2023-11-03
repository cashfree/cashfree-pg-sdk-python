# OfferPaylater

Offer object for paylater

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paylater** | [**PaylaterOffer**](PaylaterOffer.md) |  | 

## Example

```python
from cashfree_pg.models.offer_paylater import OfferPaylater

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPaylater from a JSON string
offer_paylater_instance = OfferPaylater.from_json(json)
# print the JSON string representation of the object
print OfferPaylater.to_json()

# convert the object into a dict
offer_paylater_dict = offer_paylater_instance.to_dict()
# create an instance of OfferPaylater from a dict
offer_paylater_form_dict = offer_paylater.from_dict(offer_paylater_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


