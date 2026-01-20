# UpdateOrderExtendedRequest

Request Body to Update extended data related to order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_details** | [**List[ShipmentDetails]**](ShipmentDetails.md) | Shipment details, such as the tracking company, tracking number, and tracking URLs, associated with the shipping of an order. Either &#x60;shipment_details&#x60; or &#x60;order_delivery_status&#x60; is required. | 
**order_delivery_status** | [**OrderDeliveryStatus**](OrderDeliveryStatus.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.update_order_extended_request import UpdateOrderExtendedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderExtendedRequest from a JSON string
update_order_extended_request_instance = UpdateOrderExtendedRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderExtendedRequest.to_json())

# convert the object into a dict
update_order_extended_request_dict = update_order_extended_request_instance.to_dict()
# create an instance of UpdateOrderExtendedRequest from a dict
update_order_extended_request_from_dict = UpdateOrderExtendedRequest.from_dict(update_order_extended_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


