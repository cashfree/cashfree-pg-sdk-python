# DisputeEvidenceInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.dispute_evidence_inner import DisputeEvidenceInner

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeEvidenceInner from a JSON string
dispute_evidence_inner_instance = DisputeEvidenceInner.from_json(json)
# print the JSON string representation of the object
print DisputeEvidenceInner.to_json()

# convert the object into a dict
dispute_evidence_inner_dict = dispute_evidence_inner_instance.to_dict()
# create an instance of DisputeEvidenceInner from a dict
dispute_evidence_inner_form_dict = dispute_evidence_inner.from_dict(dispute_evidence_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


