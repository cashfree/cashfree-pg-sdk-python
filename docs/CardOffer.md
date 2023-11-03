# CardOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** |  | 
**bank_name** | **str** | Bank Name of Card. | 
**scheme_name** | **List[str]** |  | 

## Example

```python
from cashfree_pg.models.card_offer import CardOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CardOffer from a JSON string
card_offer_instance = CardOffer.from_json(json)
# print the JSON string representation of the object
print CardOffer.to_json()

# convert the object into a dict
card_offer_dict = card_offer_instance.to_dict()
# create an instance of CardOffer from a dict
card_offer_form_dict = card_offer.from_dict(card_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


