# SettlementReconEntityDataInnerCustomerDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_phone** | **str** | Customer phone number. | [optional] 
**customer_email** | **str** | Customer email. | [optional] 
**customer_name** | **str** | Customer name. | [optional] 
**customer_id** | **str** | Customer&#39;s id. | [optional] 
**customer_bank_account_number** | **str** | Customer bank account number. | [optional] 
**customer_bank_code** | **str** | Customer bank code. | [optional] 
**customer_bank_ifsc** | **str** | Customer bank ifsc\&quot; | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner_customer_details import SettlementReconEntityDataInnerCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInnerCustomerDetails from a JSON string
settlement_recon_entity_data_inner_customer_details_instance = SettlementReconEntityDataInnerCustomerDetails.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInnerCustomerDetails.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_customer_details_dict = settlement_recon_entity_data_inner_customer_details_instance.to_dict()
# create an instance of SettlementReconEntityDataInnerCustomerDetails from a dict
settlement_recon_entity_data_inner_customer_details_form_dict = settlement_recon_entity_data_inner_customer_details.from_dict(settlement_recon_entity_data_inner_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


