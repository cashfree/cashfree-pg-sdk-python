# ScheduleOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_schedule_message** | **str** |  | [optional] 
**schedule_id** | **float** |  | [optional] 
**merchant_default** | **bool** |  | [optional] 

## Example

```python
from cashfree_pg.models.schedule_option import ScheduleOption

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleOption from a JSON string
schedule_option_instance = ScheduleOption.from_json(json)
# print the JSON string representation of the object
print(ScheduleOption.to_json())

# convert the object into a dict
schedule_option_dict = schedule_option_instance.to_dict()
# create an instance of ScheduleOption from a dict
schedule_option_from_dict = ScheduleOption.from_dict(schedule_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


