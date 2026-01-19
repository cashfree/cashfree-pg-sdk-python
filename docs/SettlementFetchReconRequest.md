# SettlementFetchReconRequest

Recon Request Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**FetchSettlementsRequestPagination**](FetchSettlementsRequestPagination.md) |  | 
**filters** | [**FetchSettlementsRequestFilters**](FetchSettlementsRequestFilters.md) |  | 

## Example

```python
from cashfree_pg.models.settlement_fetch_recon_request import SettlementFetchReconRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementFetchReconRequest from a JSON string
settlement_fetch_recon_request_instance = SettlementFetchReconRequest.from_json(json)
# print the JSON string representation of the object
print SettlementFetchReconRequest.to_json()

# convert the object into a dict
settlement_fetch_recon_request_dict = settlement_fetch_recon_request_instance.to_dict()
# create an instance of SettlementFetchReconRequest from a dict
settlement_fetch_recon_request_form_dict = settlement_fetch_recon_request.from_dict(settlement_fetch_recon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


