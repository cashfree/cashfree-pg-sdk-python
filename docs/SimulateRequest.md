# SimulateRequest

simulate payment request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | Entity type should be PAYMENTS or SUBS_PAYMENTS only. | 
**entity_id** | **str** | If the entity type is PAYMENTS, the entity_id will be the transactionId. If the entity type is SUBS_PAYMENTS, the entity_id will be the merchantTxnId | 
**entity_simulation** | [**EntitySimulationRequest**](EntitySimulationRequest.md) |  | 

## Example

```python
from cashfree_pg.models.simulate_request import SimulateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateRequest from a JSON string
simulate_request_instance = SimulateRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateRequest.to_json())

# convert the object into a dict
simulate_request_dict = simulate_request_instance.to_dict()
# create an instance of SimulateRequest from a dict
simulate_request_from_dict = SimulateRequest.from_dict(simulate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


