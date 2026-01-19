# SettlementReconEntityDataInnerPaymentDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_amount** | **float** | Payment amount captured. | [optional] 
**payment_currency** | **str** | Payment Curreny type - INR. | [optional] 
**bank_reference** | **str** | Unique transaction reference number of the payment. | [optional] 
**payment_time** | **str** | Date and time when the payment was initiated. | [optional] 
**payment_mode** | **str** | Mode of the payment. | [optional] 
**payment_service_charge** | **float** | Service charge applicable for the payment. | [optional] 
**payment_service_tax** | **float** | Service tax applicable on the payment. | [optional] 
**cf_payment_id** | **str** | Cashfree Payments unique ID to identify a payment. | [optional] 
**status** | **str** | Status of the Payment. | [optional] 
**forex_conversion_handling_charge** | **str** | Forex Conversion Service Charge. | [optional] 
**forex_conversion_handling_tax** | **str** | Forex Conversion Service Tax. | [optional] 
**charges_currency** | **str** | Forex Charges Curreny type - INR. | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner_payment_details import SettlementReconEntityDataInnerPaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInnerPaymentDetails from a JSON string
settlement_recon_entity_data_inner_payment_details_instance = SettlementReconEntityDataInnerPaymentDetails.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInnerPaymentDetails.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_payment_details_dict = settlement_recon_entity_data_inner_payment_details_instance.to_dict()
# create an instance of SettlementReconEntityDataInnerPaymentDetails from a dict
settlement_recon_entity_data_inner_payment_details_form_dict = settlement_recon_entity_data_inner_payment_details.from_dict(settlement_recon_entity_data_inner_payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


