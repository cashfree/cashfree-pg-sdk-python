# EligibilityFetchOffersRequest

Eligiblty API request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**OfferQueries**](OfferQueries.md) |  | 
**filters** | [**OfferFilters**](OfferFilters.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_fetch_offers_request import EligibilityFetchOffersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityFetchOffersRequest from a JSON string
eligibility_fetch_offers_request_instance = EligibilityFetchOffersRequest.from_json(json)
# print the JSON string representation of the object
print EligibilityFetchOffersRequest.to_json()

# convert the object into a dict
eligibility_fetch_offers_request_dict = eligibility_fetch_offers_request_instance.to_dict()
# create an instance of EligibilityFetchOffersRequest from a dict
eligibility_fetch_offers_request_form_dict = eligibility_fetch_offers_request.from_dict(eligibility_fetch_offers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


