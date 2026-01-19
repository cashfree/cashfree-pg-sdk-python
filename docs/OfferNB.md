# OfferNB

Offer object ofr NetBanking

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**netbanking** | [**OfferNBNetbanking**](OfferNBNetbanking.md) |  | 

## Example

```python
from cashfree_pg.models.offer_nb import OfferNB

# TODO update the JSON string below
json = "{}"
# create an instance of OfferNB from a JSON string
offer_nb_instance = OfferNB.from_json(json)
# print the JSON string representation of the object
print OfferNB.to_json()

# convert the object into a dict
offer_nb_dict = offer_nb_instance.to_dict()
# create an instance of OfferNB from a dict
offer_nb_form_dict = offer_nb.from_dict(offer_nb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


