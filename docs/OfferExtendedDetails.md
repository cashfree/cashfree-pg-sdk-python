# OfferExtendedDetails

Details of the offer which got applied to the paid order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** |  | [optional] 
**offer_status** | **str** |  | [optional] 
**offer_meta** | [**OfferMeta**](OfferMeta.md) |  | [optional] 
**offer_tnc** | [**OfferTnc**](OfferTnc.md) |  | [optional] 
**offer_details** | [**OfferDetails**](OfferDetails.md) |  | [optional] 
**offer_validations** | [**OfferValidations**](OfferValidations.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.offer_extended_details import OfferExtendedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OfferExtendedDetails from a JSON string
offer_extended_details_instance = OfferExtendedDetails.from_json(json)
# print the JSON string representation of the object
print OfferExtendedDetails.to_json()

# convert the object into a dict
offer_extended_details_dict = offer_extended_details_instance.to_dict()
# create an instance of OfferExtendedDetails from a dict
offer_extended_details_form_dict = offer_extended_details.from_dict(offer_extended_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


