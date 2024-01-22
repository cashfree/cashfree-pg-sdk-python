# TerminateOrderRequest

Request to terminate an active order at Cashfree

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_status** | **str** | To terminate an order, pass order_status as \&quot;TERMINATE\&quot;. Please note, order might not be terminated - confirm with the order_status in response. \&quot;TERMINATION_REQUESTED\&quot; states that the request is recieved and we are working on it. If the order terminates successfully, status will change to \&quot;TERMINATED\&quot;. Incase there&#39;s any active transaction which moved to success - order might not get terminated. | 

## Example

```python
from cashfree_pg.models.terminate_order_request import TerminateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateOrderRequest from a JSON string
terminate_order_request_instance = TerminateOrderRequest.from_json(json)
# print the JSON string representation of the object
print TerminateOrderRequest.to_json()

# convert the object into a dict
terminate_order_request_dict = terminate_order_request_instance.to_dict()
# create an instance of TerminateOrderRequest from a dict
terminate_order_request_form_dict = terminate_order_request.from_dict(terminate_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


