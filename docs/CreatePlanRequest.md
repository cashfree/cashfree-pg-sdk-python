# CreatePlanRequest

Request body to create a plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | Unique ID to identify the plan. Only alpha-numerics, dot, hyphen and underscore allowed. | 
**plan_name** | **str** | Name of the plan. | 
**plan_type** | **str** | Type of the plan. Possible values - PERIODIC, ON_DEMAND. | 
**plan_currency** | **str** | Currency of the plan. | [optional] 
**plan_recurring_amount** | **float** | Recurring amount for the plan. Required for PERIODIC plan_type. | [optional] 
**plan_max_amount** | **float** | Maximum amount for the plan. | 
**plan_max_cycles** | **int** | Maximum number of payment cycles for the plan. | [optional] 
**plan_intervals** | **int** | Number of billing cycles between charges. For instance, if set to 2 and the interval type is &#39;week&#39;, the service will be billed every 2 weeks. Similarly, if set to 3 and the interval type is &#39;month&#39;, the service will be billed every 3 months. Required for PERIODIC plan_type. | [optional] 
**plan_interval_type** | **str** | Interval type for the plan. Possible values - DAY, WEEK, MONTH, YEAR. | [optional] 
**plan_note** | **str** | Note for the plan. | [optional] 

## Example

```python
from cashfree_pg.models.create_plan_request import CreatePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlanRequest from a JSON string
create_plan_request_instance = CreatePlanRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePlanRequest.to_json())

# convert the object into a dict
create_plan_request_dict = create_plan_request_instance.to_dict()
# create an instance of CreatePlanRequest from a dict
create_plan_request_from_dict = CreatePlanRequest.from_dict(create_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


