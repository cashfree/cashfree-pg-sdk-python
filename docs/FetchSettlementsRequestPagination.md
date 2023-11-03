# FetchSettlementsRequestPagination

To fetch the next set of settlements, pass the cursor received in the response to the next API call.   To receive the data for the first time, pass the cursor as null.   Limit would be number of settlements that you want to receive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of settlements you want to fetch. Maximum limit is 1000, default value is 10. | 
**cursor** | **str** | Specifies from where the next set of settlement details should be fetched. | [optional] 

## Example

```python
from cashfree_pg.models.fetch_settlements_request_pagination import FetchSettlementsRequestPagination

# TODO update the JSON string below
json = "{}"
# create an instance of FetchSettlementsRequestPagination from a JSON string
fetch_settlements_request_pagination_instance = FetchSettlementsRequestPagination.from_json(json)
# print the JSON string representation of the object
print FetchSettlementsRequestPagination.to_json()

# convert the object into a dict
fetch_settlements_request_pagination_dict = fetch_settlements_request_pagination_instance.to_dict()
# create an instance of FetchSettlementsRequestPagination from a dict
fetch_settlements_request_pagination_form_dict = fetch_settlements_request_pagination.from_dict(fetch_settlements_request_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

