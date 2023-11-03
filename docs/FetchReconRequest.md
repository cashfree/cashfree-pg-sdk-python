# FetchReconRequest

Recon object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**FetchReconRequestPagination**](FetchReconRequestPagination.md) |  | 
**filters** | [**FetchReconRequestFilters**](FetchReconRequestFilters.md) |  | 

## Example

```python
from cashfree_pg.models.fetch_recon_request import FetchReconRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchReconRequest from a JSON string
fetch_recon_request_instance = FetchReconRequest.from_json(json)
# print the JSON string representation of the object
print FetchReconRequest.to_json()

# convert the object into a dict
fetch_recon_request_dict = fetch_recon_request_instance.to_dict()
# create an instance of FetchReconRequest from a dict
fetch_recon_request_form_dict = fetch_recon_request.from_dict(fetch_recon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


