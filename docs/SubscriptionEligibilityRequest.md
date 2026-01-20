# SubscriptionEligibilityRequest

Request body to fetch subscription eligibile payment method details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**SubscriptionEligibilityRequestQueries**](SubscriptionEligibilityRequestQueries.md) |  | 
**filters** | [**SubscriptionEligibilityRequestFilters**](SubscriptionEligibilityRequestFilters.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.subscription_eligibility_request import SubscriptionEligibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEligibilityRequest from a JSON string
subscription_eligibility_request_instance = SubscriptionEligibilityRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionEligibilityRequest.to_json())

# convert the object into a dict
subscription_eligibility_request_dict = subscription_eligibility_request_instance.to_dict()
# create an instance of SubscriptionEligibilityRequest from a dict
subscription_eligibility_request_from_dict = SubscriptionEligibilityRequest.from_dict(subscription_eligibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


