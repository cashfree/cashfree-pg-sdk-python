# ReconEntityDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique ID associated with the event. | [optional] 
**event_type** | **str** | The event type can be SETTLEMENT, PAYMENT, REFUND, REFUND_REVERSAL, DISPUTE, DISPUTE_REVERSAL, CHARGEBACK, CHARGEBACK_REVERSAL, OTHER_ADJUSTMENT. | [optional] 
**event_settlement_amount** | **float** | Amount that is part of the settlement corresponding to the event. | [optional] 
**event_amount** | **float** | Amount of the event. Example, refund amount, dispute amount, payment amount, etc. | [optional] 
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
**closed_in_favor_of** | **str** | Specifies whether the dispute was closed in favor of the merchant or customer. /n Possible values - Merchant, Customer | [optional] 
**dispute_resolved_on** | **str** | Date and time when the dispute was resolved. | [optional] 
**dispute_category** | **str** | Category of the dispute - Dispute code and the reason for dispute is shown. | [optional] 
**dispute_note** | **str** | Note regarding the dispute. | [optional] 
**refund_processed_at** | **str** | Date and time when the refund was processed. | [optional] 
**refund_arn** | **str** | The bank reference number for the refund. | [optional] 
**refund_note** | **str** | A refund note for your reference. | [optional] 
**refund_id** | **str** | An unique ID to associate the refund with. | [optional] 
**adjustment_remarks** | **str** | Other adjustment remarks. | [optional] 
**adjustment** | **float** | Amount that is adjusted from the settlement amount because of any credit/debit event such as refund, refund_reverse etc. | [optional] 
**service_tax** | **float** | Service tax applicable on the settlement amount. | [optional] 
**service_charge** | **float** | Service charge applicable on the settlement amount. | [optional] 
**amount_settled** | **float** | Net amount that is settled after considering the adjustments, settlement charge and tax. | [optional] 
**payment_from** | **str** | The start time of the time range of the payments considered for the settlement. | [optional] 
**payment_till** | **str** | The end time of time range of the payments considered for the settlement. | [optional] 
**reason** | **str** | Reason for settlement failure. | [optional] 
**settlement_initiated_on** | **str** | Date and time when the settlement was initiated. | [optional] 
**settlement_type** | **str** | Type of settlement. Possible values - Standard, Instant, On demand. | [optional] 
**settlement_charge** | **float** | Settlement charges applicable on the settlement. | [optional] 
**settlement_tax** | **float** | Settlement tax applicable on the settlement. | [optional] 
**remarks** | **str** | Remarks on the settlement. | [optional] 

## Example

```python
from cashfree_pg.models.recon_entity_data_inner import ReconEntityDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReconEntityDataInner from a JSON string
recon_entity_data_inner_instance = ReconEntityDataInner.from_json(json)
# print the JSON string representation of the object
print ReconEntityDataInner.to_json()

# convert the object into a dict
recon_entity_data_inner_dict = recon_entity_data_inner_instance.to_dict()
# create an instance of ReconEntityDataInner from a dict
recon_entity_data_inner_form_dict = recon_entity_data_inner.from_dict(recon_entity_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


