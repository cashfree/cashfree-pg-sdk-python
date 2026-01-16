# ReconEntity

Settlement detailed recon response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Specifies from where the next set of settlement details should be fetched. | [optional] 
**limit** | **int** | Number of settlements you want to fetch in the next iteration. | [optional] 
**data** | [**List[ReconEntityDataInner]**](ReconEntityDataInner.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.recon_entity import ReconEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReconEntity from a JSON string
recon_entity_instance = ReconEntity.from_json(json)
# print the JSON string representation of the object
print ReconEntity.to_json()

# convert the object into a dict
recon_entity_dict = recon_entity_instance.to_dict()
# create an instance of ReconEntity from a dict
recon_entity_form_dict = recon_entity.from_dict(recon_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


