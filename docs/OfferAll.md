# OfferAll

returns all offers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **object** | All offers applicable | 

## Example

```python
from cashfree_pg.models.offer_all import OfferAll

# TODO update the JSON string below
json = "{}"
# create an instance of OfferAll from a JSON string
offer_all_instance = OfferAll.from_json(json)
# print the JSON string representation of the object
print OfferAll.to_json()

# convert the object into a dict
offer_all_dict = offer_all_instance.to_dict()
# create an instance of OfferAll from a dict
offer_all_form_dict = offer_all.from_dict(offer_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


