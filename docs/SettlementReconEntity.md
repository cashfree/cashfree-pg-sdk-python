# SettlementReconEntity

Recon object for settlement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Specifies from where the next set of settlement details should be fetched. | [optional] 
**limit** | **int** | Number of settlements you want to fetch in the next iteration. | [optional] 
**data** | [**List[SettlementReconEntityDataInner]**](SettlementReconEntityDataInner.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.settlement_recon_entity import SettlementReconEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementReconEntity from a JSON string
settlement_recon_entity_instance = SettlementReconEntity.from_json(json)
# print the JSON string representation of the object
print SettlementReconEntity.to_json()

# convert the object into a dict
settlement_recon_entity_dict = settlement_recon_entity_instance.to_dict()
# create an instance of SettlementReconEntity from a dict
settlement_recon_entity_form_dict = settlement_recon_entity.from_dict(settlement_recon_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


