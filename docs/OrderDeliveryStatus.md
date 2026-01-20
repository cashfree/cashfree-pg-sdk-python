# OrderDeliveryStatus

Order delivery Status associated with order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Delivery status of order | 
**reason** | **str** | Reason of provided order delivery status. This is optional field. | [optional] 

## Example

```python
from cashfree_pg.models.order_delivery_status import OrderDeliveryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeliveryStatus from a JSON string
order_delivery_status_instance = OrderDeliveryStatus.from_json(json)
# print the JSON string representation of the object
print(OrderDeliveryStatus.to_json())

# convert the object into a dict
order_delivery_status_dict = order_delivery_status_instance.to_dict()
# create an instance of OrderDeliveryStatus from a dict
order_delivery_status_from_dict = OrderDeliveryStatus.from_dict(order_delivery_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


