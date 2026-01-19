# SettlementReconEntityDataInnerRefundDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_processed_at** | **str** | Date and time when the refund was processed. | [optional] 
**refund_arn** | **str** | The bank reference number for refund. | [optional] 
**refund_note** | **str** | A refund note for your reference. | [optional] 
**refund_id** | **str** | An unique ID associated with the refund. | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner_refund_details import SettlementReconEntityDataInnerRefundDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInnerRefundDetails from a JSON string
settlement_recon_entity_data_inner_refund_details_instance = SettlementReconEntityDataInnerRefundDetails.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInnerRefundDetails.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_refund_details_dict = settlement_recon_entity_data_inner_refund_details_instance.to_dict()
# create an instance of SettlementReconEntityDataInnerRefundDetails from a dict
settlement_recon_entity_data_inner_refund_details_form_dict = settlement_recon_entity_data_inner_refund_details.from_dict(settlement_recon_entity_data_inner_refund_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


