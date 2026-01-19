# OfferDetailsResponse

Offer details response and type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashback_details** | [**CashbackDetails**](CashbackDetails.md) |  | [optional] 
**discount_details** | [**DiscountDetails**](DiscountDetails.md) |  | [optional] 
**offer_type** | **str** | Offer Type for the Offer. | [optional] 

## Example

```python
from cashfree_pg.models.offer_details_response import OfferDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferDetailsResponse from a JSON string
offer_details_response_instance = OfferDetailsResponse.from_json(json)
# print the JSON string representation of the object
print OfferDetailsResponse.to_json()

# convert the object into a dict
offer_details_response_dict = offer_details_response_instance.to_dict()
# create an instance of OfferDetailsResponse from a dict
offer_details_response_form_dict = offer_details_response.from_dict(offer_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


