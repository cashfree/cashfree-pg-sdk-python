# SettlementReconEntityDataInner


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
**order_id** | **str** | Unique order ID. Alphanumeric and only &#39;-&#39; and &#39;_&#39; allowed. | [optional] 
**order_amount** | **float** | The amount which was passed at the order creation time. | [optional] 
**customer_phone** | **str** | Customer phone number. | [optional] 
**customer_email** | **str** | Customer email. | [optional] 
**customer_name** | **str** | Customer name. | [optional] 
**payment_amount** | **float** | Payment amount captured. | [optional] 
**payment_utr** | **str** | Unique transaction reference number of the payment. | [optional] 
**payment_time** | **str** | Date and time when the payment was initiated. | [optional] 
**payment_service_charge** | **float** | Service charge applicable for the payment. | [optional] 
**payment_service_tax** | **float** | Service tax applicable on the payment. | [optional] 
**cf_payment_id** | **str** | Cashfree Payments unique ID to identify a payment. | [optional] 
**cf_settlement_id** | **str** | Unique ID to identify the settlement. | [optional] 
**settlement_date** | **str** | Date and time when the settlement was processed. | [optional] 
**settlement_utr** | **str** | Unique transaction reference number of the settlement. | [optional] 
**split_service_charge** | **float** | Service charge that is applicable for splitting the payment. | [optional] 
**split_service_tax** | **float** | Service tax applicable for splitting the amount to vendors. | [optional] 
**vendor_commission** | **float** | Vendor commission applicable for this transaction. | [optional] 
**closed_in_favor_of** | **str** | Specifies whether the dispute was closed in favor of the merchant or customer. Possible values - Merchant, Customer. | [optional] 
**dispute_resolved_on** | **str** | Date and time when the dispute was resolved. | [optional] 
**dispute_category** | **str** | Category of the dispute - Dispute code and the reason for dispute is shown. | [optional] 
**dispute_note** | **str** | Note regarding the dispute. | [optional] 
**refund_processed_at** | **str** | Date and time when the refund was processed. | [optional] 
**refund_arn** | **str** | The bank reference number for refund. | [optional] 
**refund_note** | **str** | A refund note for your reference. | [optional] 
**refund_id** | **str** | An unique ID associated with the refund. | [optional] 
**adjustment_remarks** | **str** | Other adjustment remarks. | [optional] 

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


