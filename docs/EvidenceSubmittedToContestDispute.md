# EvidenceSubmittedToContestDispute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.evidence_submitted_to_contest_dispute import EvidenceSubmittedToContestDispute

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceSubmittedToContestDispute from a JSON string
evidence_submitted_to_contest_dispute_instance = EvidenceSubmittedToContestDispute.from_json(json)
# print the JSON string representation of the object
print(EvidenceSubmittedToContestDispute.to_json())

# convert the object into a dict
evidence_submitted_to_contest_dispute_dict = evidence_submitted_to_contest_dispute_instance.to_dict()
# create an instance of EvidenceSubmittedToContestDispute from a dict
evidence_submitted_to_contest_dispute_from_dict = EvidenceSubmittedToContestDispute.from_dict(evidence_submitted_to_contest_dispute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


