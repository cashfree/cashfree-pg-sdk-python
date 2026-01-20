# PlanEntity

The response returned for Get, Create and Manage Plan APIs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_currency** | **str** | Currency for the plan. | [optional] 
**plan_id** | **str** | Plan ID provided by merchant. | [optional] 
**plan_interval_type** | **str** | Interval type for the plan. | [optional] 
**plan_intervals** | **int** | Number of intervals for the plan. | [optional] 
**plan_max_amount** | **float** | Maximum amount for the plan. | [optional] 
**plan_max_cycles** | **int** | Maximum number of payment cycles for the plan. | [optional] 
**plan_name** | **str** | Name of the plan. | [optional] 
**plan_note** | **str** | Note for the plan. | [optional] 
**plan_recurring_amount** | **float** | Recurring amount for the plan. | [optional] 
**plan_status** | **str** | Status of the plan. | [optional] 
**plan_type** | **str** | Type of the plan. | [optional] 

## Example

```python
from cashfree_pg.models.plan_entity import PlanEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PlanEntity from a JSON string
plan_entity_instance = PlanEntity.from_json(json)
# print the JSON string representation of the object
print(PlanEntity.to_json())

# convert the object into a dict
plan_entity_dict = plan_entity_instance.to_dict()
# create an instance of PlanEntity from a dict
plan_entity_from_dict = PlanEntity.from_dict(plan_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


