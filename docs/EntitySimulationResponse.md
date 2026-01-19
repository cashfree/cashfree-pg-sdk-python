# EntitySimulationResponse

Entity Simulation it contains payment_status and payment_error_code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_status** | **str** | Payment Status | 
**payment_error_code** | **str** | Payment Error Code | [optional] 

## Example

```python
from cashfree_pg.models.entity_simulation_response import EntitySimulationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntitySimulationResponse from a JSON string
entity_simulation_response_instance = EntitySimulationResponse.from_json(json)
# print the JSON string representation of the object
print EntitySimulationResponse.to_json()

# convert the object into a dict
entity_simulation_response_dict = entity_simulation_response_instance.to_dict()
# create an instance of EntitySimulationResponse from a dict
entity_simulation_response_form_dict = entity_simulation_response.from_dict(entity_simulation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


