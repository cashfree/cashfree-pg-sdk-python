# OfferFilters

Filter for offers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_type** | [**List[OfferType]**](OfferType.md) | Array of offer_type to be filtered. | [optional] 

## Example

```python
from cashfree_pg.models.offer_filters import OfferFilters

# TODO update the JSON string below
json = "{}"
# create an instance of OfferFilters from a JSON string
offer_filters_instance = OfferFilters.from_json(json)
# print the JSON string representation of the object
print OfferFilters.to_json()

# convert the object into a dict
offer_filters_dict = offer_filters_instance.to_dict()
# create an instance of OfferFilters from a dict
offer_filters_form_dict = offer_filters.from_dict(offer_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


