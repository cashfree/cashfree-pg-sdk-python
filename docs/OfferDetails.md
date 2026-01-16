# OfferDetails

Offer details and type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_type** | **str** | Offer Type for the Offer. | 
**discount_details** | [**DiscountDetails**](DiscountDetails.md) |  | [optional] 
**cashback_details** | [**CashbackDetails**](CashbackDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.offer_details import OfferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OfferDetails from a JSON string
offer_details_instance = OfferDetails.from_json(json)
# print the JSON string representation of the object
print OfferDetails.to_json()

# convert the object into a dict
offer_details_dict = offer_details_instance.to_dict()
# create an instance of OfferDetails from a dict
offer_details_form_dict = offer_details.from_dict(offer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


