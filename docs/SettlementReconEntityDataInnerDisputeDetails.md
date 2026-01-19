# SettlementReconEntityDataInnerDisputeDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_in_favor_of** | **str** | Specifies whether the dispute was closed in favor of the merchant or customer. Possible values - Merchant, Customer. | [optional] 
**dispute_resolved_on** | **str** | Date and time when the dispute was resolved. | [optional] 
**dispute_category** | **str** | Category of the dispute - Dispute code and the reason for dispute is shown. | [optional] 
**dispute_note** | **str** | Note regarding the dispute. | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner_dispute_details import SettlementReconEntityDataInnerDisputeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInnerDisputeDetails from a JSON string
settlement_recon_entity_data_inner_dispute_details_instance = SettlementReconEntityDataInnerDisputeDetails.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInnerDisputeDetails.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_dispute_details_dict = settlement_recon_entity_data_inner_dispute_details_instance.to_dict()
# create an instance of SettlementReconEntityDataInnerDisputeDetails from a dict
settlement_recon_entity_data_inner_dispute_details_form_dict = settlement_recon_entity_data_inner_dispute_details.from_dict(settlement_recon_entity_data_inner_dispute_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


