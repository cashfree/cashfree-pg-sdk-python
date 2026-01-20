# ESOrderReconRequestFilters

Provide the filter object details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Specify the start data from which you want to get the recon data. | [optional] 
**end_date** | **str** | Specify the end data till which you want to get the recon data. | [optional] 
**order_ids** | **List[str]** | Please provide list of order ids for which you want to get the recon data. | [optional] 

## Example

```python
from cashfree_pg.models.es_order_recon_request_filters import ESOrderReconRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ESOrderReconRequestFilters from a JSON string
es_order_recon_request_filters_instance = ESOrderReconRequestFilters.from_json(json)
# print the JSON string representation of the object
print(ESOrderReconRequestFilters.to_json())

# convert the object into a dict
es_order_recon_request_filters_dict = es_order_recon_request_filters_instance.to_dict()
# create an instance of ESOrderReconRequestFilters from a dict
es_order_recon_request_filters_from_dict = ESOrderReconRequestFilters.from_dict(es_order_recon_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


