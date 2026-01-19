# FetchReconRequestFilters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Specify the start date from when you want the settlement reconciliation details. | 
**end_date** | **str** | Specify the end date till when you want the settlement reconciliation details. | 

## Example

```python
from cashfree_pg.models.fetch_recon_request_filters import FetchReconRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of FetchReconRequestFilters from a JSON string
fetch_recon_request_filters_instance = FetchReconRequestFilters.from_json(json)
# print the JSON string representation of the object
print FetchReconRequestFilters.to_json()

# convert the object into a dict
fetch_recon_request_filters_dict = fetch_recon_request_filters_instance.to_dict()
# create an instance of FetchReconRequestFilters from a dict
fetch_recon_request_filters_form_dict = fetch_recon_request_filters.from_dict(fetch_recon_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


