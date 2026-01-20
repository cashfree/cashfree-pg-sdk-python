# ESOrderReconRequestPagination

Set limit based on your requirement. Pagination limit will fetch a set of orders, next set of orders can be generated using the cursor shared in previous response of the same API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** |  | [optional] 
**limit** | **int** | Set the minimum/maximum limit for number of filtered data. Min value - 10, Max value - 100. | [optional] 

## Example

```python
from cashfree_pg.models.es_order_recon_request_pagination import ESOrderReconRequestPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ESOrderReconRequestPagination from a JSON string
es_order_recon_request_pagination_instance = ESOrderReconRequestPagination.from_json(json)
# print the JSON string representation of the object
print(ESOrderReconRequestPagination.to_json())

# convert the object into a dict
es_order_recon_request_pagination_dict = es_order_recon_request_pagination_instance.to_dict()
# create an instance of ESOrderReconRequestPagination from a dict
es_order_recon_request_pagination_from_dict = ESOrderReconRequestPagination.from_dict(es_order_recon_request_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


