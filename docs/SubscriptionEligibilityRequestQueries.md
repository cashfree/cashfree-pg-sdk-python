# SubscriptionEligibilityRequestQueries

Necessary parameters to fetch eligible payment methods.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | A unique ID passed by merchant for identifying the subscription | 

## Example

```python
from cashfree_pg.models.subscription_eligibility_request_queries import SubscriptionEligibilityRequestQueries

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEligibilityRequestQueries from a JSON string
subscription_eligibility_request_queries_instance = SubscriptionEligibilityRequestQueries.from_json(json)
# print the JSON string representation of the object
print SubscriptionEligibilityRequestQueries.to_json()

# convert the object into a dict
subscription_eligibility_request_queries_dict = subscription_eligibility_request_queries_instance.to_dict()
# create an instance of SubscriptionEligibilityRequestQueries from a dict
subscription_eligibility_request_queries_form_dict = subscription_eligibility_request_queries.from_dict(subscription_eligibility_request_queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


