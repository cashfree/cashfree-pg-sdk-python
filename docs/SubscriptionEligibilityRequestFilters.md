# SubscriptionEligibilityRequestFilters

Filters to refine eligible payment method selection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_methods** | **List[str]** | Possbile values in array - enach, pnach, upi, card. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_eligibility_request_filters import SubscriptionEligibilityRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEligibilityRequestFilters from a JSON string
subscription_eligibility_request_filters_instance = SubscriptionEligibilityRequestFilters.from_json(json)
# print the JSON string representation of the object
print(SubscriptionEligibilityRequestFilters.to_json())

# convert the object into a dict
subscription_eligibility_request_filters_dict = subscription_eligibility_request_filters_instance.to_dict()
# create an instance of SubscriptionEligibilityRequestFilters from a dict
subscription_eligibility_request_filters_from_dict = SubscriptionEligibilityRequestFilters.from_dict(subscription_eligibility_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


