# SettlementReconEntityDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_details** | [**SettlementReconEntityDataInnerEventDetails**](SettlementReconEntityDataInnerEventDetails.md) |  | [optional] 
**order_details** | [**SettlementReconEntityDataInnerOrderDetails**](SettlementReconEntityDataInnerOrderDetails.md) |  | [optional] 
**customer_details** | [**SettlementReconEntityDataInnerCustomerDetails**](SettlementReconEntityDataInnerCustomerDetails.md) |  | [optional] 
**payment_details** | [**SettlementReconEntityDataInnerPaymentDetails**](SettlementReconEntityDataInnerPaymentDetails.md) |  | [optional] 
**settlement_details** | [**SettlementReconEntityDataInnerSettlementDetails**](SettlementReconEntityDataInnerSettlementDetails.md) |  | [optional] 
**dispute_details** | [**SettlementReconEntityDataInnerDisputeDetails**](SettlementReconEntityDataInnerDisputeDetails.md) |  | [optional] 
**refund_details** | [**SettlementReconEntityDataInnerRefundDetails**](SettlementReconEntityDataInnerRefundDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner import SettlementReconEntityDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInner from a JSON string
settlement_recon_entity_data_inner_instance = SettlementReconEntityDataInner.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInner.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_dict = settlement_recon_entity_data_inner_instance.to_dict()
# create an instance of SettlementReconEntityDataInner from a dict
settlement_recon_entity_data_inner_form_dict = settlement_recon_entity_data_inner.from_dict(settlement_recon_entity_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


