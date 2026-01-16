# FetchSettlementsRequest

Request to fetch settlement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**FetchSettlementsRequestPagination**](FetchSettlementsRequestPagination.md) |  | 
**filters** | [**FetchSettlementsRequestFilters**](FetchSettlementsRequestFilters.md) |  | 

## Example

```python
from cashfree_pg.models.fetch_settlements_request import FetchSettlementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchSettlementsRequest from a JSON string
fetch_settlements_request_instance = FetchSettlementsRequest.from_json(json)
# print the JSON string representation of the object
print FetchSettlementsRequest.to_json()

# convert the object into a dict
fetch_settlements_request_dict = fetch_settlements_request_instance.to_dict()
# create an instance of FetchSettlementsRequest from a dict
fetch_settlements_request_form_dict = fetch_settlements_request.from_dict(fetch_settlements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


