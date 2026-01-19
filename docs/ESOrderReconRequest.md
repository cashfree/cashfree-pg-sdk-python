# ESOrderReconRequest

ES Order Recon Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ESOrderReconRequestFilters**](ESOrderReconRequestFilters.md) |  | 
**pagination** | [**ESOrderReconRequestPagination**](ESOrderReconRequestPagination.md) |  | 

## Example

```python
from cashfree_pg.models.es_order_recon_request import ESOrderReconRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ESOrderReconRequest from a JSON string
es_order_recon_request_instance = ESOrderReconRequest.from_json(json)
# print the JSON string representation of the object
print ESOrderReconRequest.to_json()

# convert the object into a dict
es_order_recon_request_dict = es_order_recon_request_instance.to_dict()
# create an instance of ESOrderReconRequest from a dict
es_order_recon_request_form_dict = es_order_recon_request.from_dict(es_order_recon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


