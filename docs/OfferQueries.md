# OfferQueries

Offer Query Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | OrderId of the order. Either of &#x60;order_id&#x60; or &#x60;order_amount&#x60; is mandatory. | [optional] 
**amount** | **float** | Amount of the order. OrderId of the order. Either of &#x60;order_id&#x60; or &#x60;order_amount&#x60; is mandatory. | [optional] 

## Example

```python
from cashfree_pg.models.offer_queries import OfferQueries

# TODO update the JSON string below
json = "{}"
# create an instance of OfferQueries from a JSON string
offer_queries_instance = OfferQueries.from_json(json)
# print the JSON string representation of the object
print OfferQueries.to_json()

# convert the object into a dict
offer_queries_dict = offer_queries_instance.to_dict()
# create an instance of OfferQueries from a dict
offer_queries_form_dict = offer_queries.from_dict(offer_queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


