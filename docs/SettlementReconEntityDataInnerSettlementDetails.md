# SettlementReconEntityDataInnerSettlementDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_settlement_id** | **str** | Unique ID to identify the settlement. | [optional] 
**settlement_date** | **str** | Date and time when the settlement was processed. | [optional] 
**utr** | **str** | Unique transaction reference number of the settlement. | [optional] 
**split_service_charge** | **float** | Service charge that is applicable for splitting the payment. | [optional] 
**split_service_tax** | **float** | Service tax applicable for splitting the amount to vendors. | [optional] 
**vendor_commission** | **float** | Vendor commission applicable for this transaction. | [optional] 
**payment_from** | **str** | Date and time from settlement computed. | [optional] 
**payment_till** | **str** | Date and time till settlement computed. | [optional] 
**reason** | **str** | If any reason for settlement failure. | [optional] 
**remarks** | **str** | Remarks related for settlement. | [optional] 
**service_charge** | **float** | Service charge for the transactions. | [optional] 
**service_tax** | **float** | Service tax for the transactions. | [optional] 
**settlement_charge** | **float** | Settlement Service Charge. | [optional] 
**settlement_initiated_on** | **str** | Date and time when Settlement initiated. | [optional] 
**settlement_tax** | **float** | Settlement Service Tax. | [optional] 
**settlement_type** | **str** | Type of Settlement, Example - Normal Settlement. | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner_settlement_details import SettlementReconEntityDataInnerSettlementDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInnerSettlementDetails from a JSON string
settlement_recon_entity_data_inner_settlement_details_instance = SettlementReconEntityDataInnerSettlementDetails.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInnerSettlementDetails.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_settlement_details_dict = settlement_recon_entity_data_inner_settlement_details_instance.to_dict()
# create an instance of SettlementReconEntityDataInnerSettlementDetails from a dict
settlement_recon_entity_data_inner_settlement_details_form_dict = settlement_recon_entity_data_inner_settlement_details.from_dict(settlement_recon_entity_data_inner_settlement_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


