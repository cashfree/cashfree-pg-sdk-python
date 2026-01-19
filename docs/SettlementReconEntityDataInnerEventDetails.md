# SettlementReconEntityDataInnerEventDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique ID associated with the event. | [optional] 
**event_type** | **str** | The event type can be PAYMENT, REFUND, REFUND_REVERSAL, DISPUTE, DISPUTE_REVERSAL, CHARGEBACK, CHARGEBACK_REVERSAL, OTHER_ADJUSTMENT. | [optional] 
**event_settlement_amount** | **float** | Amount that is part of the settlement corresponding to the event. | [optional] 
**event_amount** | **float** | Amount corresponding to the event. Example, refund amount, dispute amount, payment amount, etc. | [optional] 
**sale_type** | **str** | Indicates if it is CREDIT/DEBIT sale. | [optional] 
**event_status** | **str** | Status of the event. Example - SUCCESS, FAILED, PENDING, CANCELLED. | [optional] 
**entity** | **str** | Recon | [optional] 
**event_time** | **str** | Time associated with the event. Example, transaction time, dispute initiation time | [optional] 
**event_currency** | **str** | Curreny type - INR. | [optional] 
**event_service_charge** | **float** | Service charge for above event_type. | [optional] 
**event_service_tax** | **float** | Service tax for above event_type. | [optional] 
**event_remarks** | **float** | Remarks for above event_type. | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner_event_details import SettlementReconEntityDataInnerEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInnerEventDetails from a JSON string
settlement_recon_entity_data_inner_event_details_instance = SettlementReconEntityDataInnerEventDetails.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInnerEventDetails.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_event_details_dict = settlement_recon_entity_data_inner_event_details_instance.to_dict()
# create an instance of SettlementReconEntityDataInnerEventDetails from a dict
settlement_recon_entity_data_inner_event_details_form_dict = settlement_recon_entity_data_inner_event_details.from_dict(settlement_recon_entity_data_inner_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


