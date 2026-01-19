# OfferMeta

Offer meta details object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_title** | **str** | Title for the Offer. | 
**offer_description** | **str** | Description for the Offer. | 
**offer_code** | **str** | Unique identifier for the Offer. | 
**offer_start_time** | **str** | Start Time for the Offer | 
**offer_end_time** | **str** | Expiry Time for the Offer | 

## Example

```python
from cashfree_pg.models.offer_meta import OfferMeta

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMeta from a JSON string
offer_meta_instance = OfferMeta.from_json(json)
# print the JSON string representation of the object
print OfferMeta.to_json()

# convert the object into a dict
offer_meta_dict = offer_meta_instance.to_dict()
# create an instance of OfferMeta from a dict
offer_meta_form_dict = offer_meta.from_dict(offer_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


