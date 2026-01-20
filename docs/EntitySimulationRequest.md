# EntitySimulationRequest

Entity Simulation it contains payment_status and payment_error_code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_status** | **str** | Payment Status | 
**payment_error_code** | **str** | Payment Error Code | [optional] 

## Example

```python
from cashfree_pg.models.entity_simulation_request import EntitySimulationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntitySimulationRequest from a JSON string
entity_simulation_request_instance = EntitySimulationRequest.from_json(json)
# print the JSON string representation of the object
print(EntitySimulationRequest.to_json())

# convert the object into a dict
entity_simulation_request_dict = entity_simulation_request_instance.to_dict()
# create an instance of EntitySimulationRequest from a dict
entity_simulation_request_from_dict = EntitySimulationRequest.from_dict(entity_simulation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


