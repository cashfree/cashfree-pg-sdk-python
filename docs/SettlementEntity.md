# SettlementEntity

Settlement entity object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_payment_id** | **int** |  | [optional] 
**cf_settlement_id** | **int** |  | [optional] 
**settlement_currency** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**entity** | **str** |  | [optional] 
**order_amount** | **float** |  | [optional] 
**payment_time** | **str** |  | [optional] 
**service_charge** | **float** |  | [optional] 
**service_tax** | **float** |  | [optional] 
**settlement_amount** | **float** |  | [optional] 
**settlement_id** | **int** |  | [optional] 
**transfer_id** | **int** |  | [optional] 
**transfer_time** | **str** |  | [optional] 
**transfer_utr** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.settlement_entity import SettlementEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementEntity from a JSON string
settlement_entity_instance = SettlementEntity.from_json(json)
# print the JSON string representation of the object
print SettlementEntity.to_json()

# convert the object into a dict
settlement_entity_dict = settlement_entity_instance.to_dict()
# create an instance of SettlementEntity from a dict
settlement_entity_form_dict = settlement_entity.from_dict(settlement_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


