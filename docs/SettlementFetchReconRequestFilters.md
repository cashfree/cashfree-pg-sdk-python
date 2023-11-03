# SettlementFetchReconRequestFilters

Specify either the Settlement ID, Settlement UTR, or start date and end date to fetch the settlement details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_settlement_ids** | **List[int]** | List of settlement IDs for which you want the settlement reconciliation details. | [optional] 
**settlement_utrs** | **List[str]** | List of settlement UTRs for which you want the settlement reconciliation details. | [optional] 
**start_date** | **str** | Specify the start date from when you want the settlement reconciliation details. | [optional] 
**end_date** | **str** | Specify the end date till when you want the settlement reconciliation details. | [optional] 

## Example

```python
from cashfree_pg.models.settlement_fetch_recon_request_filters import SettlementFetchReconRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementFetchReconRequestFilters from a JSON string
settlement_fetch_recon_request_filters_instance = SettlementFetchReconRequestFilters.from_json(json)
# print the JSON string representation of the object
print SettlementFetchReconRequestFilters.to_json()

# convert the object into a dict
settlement_fetch_recon_request_filters_dict = settlement_fetch_recon_request_filters_instance.to_dict()
# create an instance of SettlementFetchReconRequestFilters from a dict
settlement_fetch_recon_request_filters_form_dict = settlement_fetch_recon_request_filters.from_dict(settlement_fetch_recon_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


