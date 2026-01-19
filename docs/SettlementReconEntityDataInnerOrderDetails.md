# SettlementReconEntityDataInnerOrderDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Unique order ID. Alphanumeric and only &#39;-&#39; and &#39;_&#39; allowed. | [optional] 
**order_amount** | **float** | The amount which was passed at the order creation time. | [optional] 
**order_currency** | **str** | Order Curreny type - INR. | [optional] 
**order_tags** | **object** | The order tags provided during order creation | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity_data_inner_order_details import SettlementReconEntityDataInnerOrderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntityDataInnerOrderDetails from a JSON string
settlement_recon_entity_data_inner_order_details_instance = SettlementReconEntityDataInnerOrderDetails.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntityDataInnerOrderDetails.to_json()

# convert the object into a dict
settlement_recon_entity_data_inner_order_details_dict = settlement_recon_entity_data_inner_order_details_instance.to_dict()
# create an instance of SettlementReconEntityDataInnerOrderDetails from a dict
settlement_recon_entity_data_inner_order_details_form_dict = settlement_recon_entity_data_inner_order_details.from_dict(settlement_recon_entity_data_inner_order_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


