# EvidencesToContestDispute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** |  | [optional] 
**document_description** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.evidences_to_contest_dispute import EvidencesToContestDispute

# TODO update the JSON string below
json = "{}"
# create an instance of EvidencesToContestDispute from a JSON string
evidences_to_contest_dispute_instance = EvidencesToContestDispute.from_json(json)
# print the JSON string representation of the object
print(EvidencesToContestDispute.to_json())

# convert the object into a dict
evidences_to_contest_dispute_dict = evidences_to_contest_dispute_instance.to_dict()
# create an instance of EvidencesToContestDispute from a dict
evidences_to_contest_dispute_from_dict = EvidencesToContestDispute.from_dict(evidences_to_contest_dispute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


