# SubscriptionEligibilityResponse

Subscrition eligibility API response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**List[EligibilityMethodItem]**](EligibilityMethodItem.md) | List of eligibile payment methods for the subscription. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_eligibility_response import SubscriptionEligibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEligibilityResponse from a JSON string
subscription_eligibility_response_instance = SubscriptionEligibilityResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionEligibilityResponse.to_json())

# convert the object into a dict
subscription_eligibility_response_dict = subscription_eligibility_response_instance.to_dict()
# create an instance of SubscriptionEligibilityResponse from a dict
subscription_eligibility_response_from_dict = SubscriptionEligibilityResponse.from_dict(subscription_eligibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


