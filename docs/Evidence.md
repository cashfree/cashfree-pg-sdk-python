# Evidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.evidence import Evidence

# TODO update the JSON string below
json = "{}"
# create an instance of Evidence from a JSON string
evidence_instance = Evidence.from_json(json)
# print the JSON string representation of the object
print(Evidence.to_json())

# convert the object into a dict
evidence_dict = evidence_instance.to_dict()
# create an instance of Evidence from a dict
evidence_from_dict = Evidence.from_dict(evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


