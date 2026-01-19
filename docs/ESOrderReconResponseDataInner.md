# ESOrderReconResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**settlement_eligibility_time** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**merchant_order_id** | **str** |  | [optional] 
**tx_time** | **str** |  | [optional] 
**settled** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**merchant_settlement_utr** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**sale_type** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_phone** | **str** |  | [optional] 
**merchant_vendor_commission** | **str** |  | [optional] 
**split_service_charge** | **str** |  | [optional] 
**split_service_tax** | **str** |  | [optional] 
**pg_service_tax** | **str** |  | [optional] 
**pg_service_charge** | **str** |  | [optional] 
**pg_charge_postpaid** | **str** |  | [optional] 
**merchant_settlement_id** | **str** |  | [optional] 
**added_on** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**settlement_initiated_on** | **str** |  | [optional] 
**settlement_time** | **str** |  | [optional] 
**order_splits** | [**List[ESOrderReconResponseDataInnerOrderSplitsInner]**](ESOrderReconResponseDataInnerOrderSplitsInner.md) |  | [optional] 
**eligible_split_balance** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.es_order_recon_response_data_inner import ESOrderReconResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ESOrderReconResponseDataInner from a JSON string
es_order_recon_response_data_inner_instance = ESOrderReconResponseDataInner.from_json(json)
# print the JSON string representation of the object
print ESOrderReconResponseDataInner.to_json()

# convert the object into a dict
es_order_recon_response_data_inner_dict = es_order_recon_response_data_inner_instance.to_dict()
# create an instance of ESOrderReconResponseDataInner from a dict
es_order_recon_response_data_inner_form_dict = es_order_recon_response_data_inner.from_dict(es_order_recon_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


