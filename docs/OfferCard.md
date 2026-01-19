# OfferCard

Offers related to cards

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**CardOffer**](CardOffer.md) |  | 

## Example

```python
from cashfree_pg.models.offer_card import OfferCard

# TODO update the JSON string below
json = "{}"
# create an instance of OfferCard from a JSON string
offer_card_instance = OfferCard.from_json(json)
# print the JSON string representation of the object
print OfferCard.to_json()

# convert the object into a dict
offer_card_dict = offer_card_instance.to_dict()
# create an instance of OfferCard from a dict
offer_card_form_dict = offer_card.from_dict(offer_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


