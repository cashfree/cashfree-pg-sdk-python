# RefundSpeed

How fast refund has to be proecessed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | **str** | Requested speed of refund. | [optional] 
**accepted** | **str** | Accepted speed of refund. | [optional] 
**processed** | **str** | Processed speed of refund. | [optional] 
**message** | **str** | Error message, if any for refund_speed request | [optional] 

## Example

```python
from cashfree_pg.models.refund_speed import RefundSpeed

# TODO update the JSON string below
json = "{}"
# create an instance of RefundSpeed from a JSON string
refund_speed_instance = RefundSpeed.from_json(json)
# print the JSON string representation of the object
print RefundSpeed.to_json()

# convert the object into a dict
refund_speed_dict = refund_speed_instance.to_dict()
# create an instance of RefundSpeed from a dict
refund_speed_form_dict = refund_speed.from_dict(refund_speed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


