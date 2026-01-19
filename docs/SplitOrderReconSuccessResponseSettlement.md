# SplitOrderReconSuccessResponseSettlement

Details of the settlement information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | Type of entity. Example: \&quot;settlement\&quot;. | [optional] 
**cf_settlement_id** | **int** | Unique Cashfree settlement ID. | [optional] 
**cf_payment_id** | **int** | Unique Cashfree payment ID associated with the order. | [optional] 
**order_id** | **str** | Unique identifier for the order. | [optional] 
**order_currency** | **str** | Currency of the order. Example: \&quot;INR\&quot;. | [optional] 
**transfer_id** | **str** | Unique transfer ID if available, otherwise null. | [optional] 
**order_amount** | **float** | Total amount of the order. | [optional] 
**service_charge** | **float** | Service charge for the order. | [optional] 
**service_tax** | **float** | Service tax for the order. | [optional] 
**settlement_amount** | **float** | Amount to be settled after charges and tax. | [optional] 
**settlement_currency** | **str** | Currency of the settlement. Example: \&quot;INR\&quot;. | [optional] 
**transfer_utr** | **str** | UTR (Unique Transaction Reference) for the transfer if available, otherwise null. | [optional] 
**transfer_time** | **str** | Time of transfer if available, otherwise null. | [optional] 
**payment_time** | **str** | Timestamp when payment was made. | [optional] 

## Example

```python
from cashfree_pg.models.split_order_recon_success_response_settlement import SplitOrderReconSuccessResponseSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of SplitOrderReconSuccessResponseSettlement from a JSON string
split_order_recon_success_response_settlement_instance = SplitOrderReconSuccessResponseSettlement.from_json(json)
# print the JSON string representation of the object
print SplitOrderReconSuccessResponseSettlement.to_json()

# convert the object into a dict
split_order_recon_success_response_settlement_dict = split_order_recon_success_response_settlement_instance.to_dict()
# create an instance of SplitOrderReconSuccessResponseSettlement from a dict
split_order_recon_success_response_settlement_form_dict = split_order_recon_success_response_settlement.from_dict(split_order_recon_success_response_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


