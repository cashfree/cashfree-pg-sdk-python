# EligibilityFetchCardlessEMIRequest

eligibilty request for cardless

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**CardlessEMIQueries**](CardlessEMIQueries.md) |  | 

## Example

```python
from cashfree_pg.models.eligibility_fetch_cardless_emi_request import EligibilityFetchCardlessEMIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityFetchCardlessEMIRequest from a JSON string
eligibility_fetch_cardless_emi_request_instance = EligibilityFetchCardlessEMIRequest.from_json(json)
# print the JSON string representation of the object
print EligibilityFetchCardlessEMIRequest.to_json()

# convert the object into a dict
eligibility_fetch_cardless_emi_request_dict = eligibility_fetch_cardless_emi_request_instance.to_dict()
# create an instance of EligibilityFetchCardlessEMIRequest from a dict
eligibility_fetch_cardless_emi_request_form_dict = eligibility_fetch_cardless_emi_request.from_dict(eligibility_fetch_cardless_emi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


