# OfferMetaResponse

Offer meta response details object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_code** | **str** | Unique identifier for the Offer. | [optional] 
**offer_description** | **str** | Description for the Offer. | [optional] 
**offer_end_time** | **str** | Expiry Time for the Offer | [optional] 
**offer_start_time** | **str** | Start Time for the Offer | [optional] 
**offer_title** | **str** | Title for the Offer. | [optional] 

## Example

```python
from cashfree_pg.models.offer_meta_response import OfferMetaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferMetaResponse from a JSON string
offer_meta_response_instance = OfferMetaResponse.from_json(json)
# print the JSON string representation of the object
print OfferMetaResponse.to_json()

# convert the object into a dict
offer_meta_response_dict = offer_meta_response_instance.to_dict()
# create an instance of OfferMetaResponse from a dict
offer_meta_response_form_dict = offer_meta_response.from_dict(offer_meta_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


