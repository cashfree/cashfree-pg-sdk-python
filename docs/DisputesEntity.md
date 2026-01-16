# DisputesEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispute_id** | **int** |  | [optional] 
**dispute_type** | **str** |  | [optional] 
**reason_code** | **str** |  | [optional] 
**reason_description** | **str** |  | [optional] 
**dispute_amount** | **float** | Dispute amount may differ from transaction amount for partial cases. | [optional] 
**created_at** | **str** | This is the time when the dispute was created. | [optional] 
**respond_by** | **str** | This is the time by which evidence should be submitted to contest the dispute. | [optional] 
**updated_at** | **str** | This is the time when the dispute case was updated. | [optional] 
**resolved_at** | **str** | This is the time when the dispute case was closed. | [optional] 
**dispute_status** | **str** |  | [optional] 
**cf_dispute_remarks** | **str** |  | [optional] 
**preferred_evidence** | [**List[EvidencesToContestDispute]**](EvidencesToContestDispute.md) |  | [optional] 
**dispute_evidence** | [**List[Evidence]**](Evidence.md) |  | [optional] 
**order_details** | [**OrderDetailsInDisputesEntity**](OrderDetailsInDisputesEntity.md) |  | [optional] 
**customer_details** | [**CustomerDetailsInDisputesEntity**](CustomerDetailsInDisputesEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.disputes_entity import DisputesEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DisputesEntity from a JSON string
disputes_entity_instance = DisputesEntity.from_json(json)
# print the JSON string representation of the object
print DisputesEntity.to_json()

# convert the object into a dict
disputes_entity_dict = disputes_entity_instance.to_dict()
# create an instance of DisputesEntity from a dict
disputes_entity_form_dict = disputes_entity.from_dict(disputes_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


