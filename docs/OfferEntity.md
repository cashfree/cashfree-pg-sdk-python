# OfferEntity

Offer entity object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** |  | [optional] 
**offer_status** | **str** |  | [optional] 
**order_amount** | **float** |  | [optional] 
**payable_amount** | **float** |  | [optional] 
**offer_meta** | [**OfferMetaResponse**](OfferMetaResponse.md) |  | [optional] 
**offer_tnc** | [**OfferTncResponse**](OfferTncResponse.md) |  | [optional] 
**offer_details** | [**OfferDetailsResponse**](OfferDetailsResponse.md) |  | [optional] 
**offer_validations** | [**OfferValidationsResponse**](OfferValidationsResponse.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.offer_entity import OfferEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEntity from a JSON string
offer_entity_instance = OfferEntity.from_json(json)
# print the JSON string representation of the object
print OfferEntity.to_json()

# convert the object into a dict
offer_entity_dict = offer_entity_instance.to_dict()
# create an instance of OfferEntity from a dict
offer_entity_form_dict = offer_entity.from_dict(offer_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


