# OrderCreateRefundRequest

create refund request object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_amount** | **float** | Amount to be refunded. Should be lesser than or equal to the transaction amount. (Decimals allowed) | 
**refund_id** | **str** | An unique ID to associate the refund with. Provie alphanumeric values | 
**refund_note** | **str** | A refund note for your reference. | [optional] 
**refund_speed** | **str** | Speed at which the refund is processed. It&#39;s an optional field with default being STANDARD | [optional] 
**refund_splits** | [**List[VendorSplit]**](VendorSplit.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.order_create_refund_request import OrderCreateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRefundRequest from a JSON string
order_create_refund_request_instance = OrderCreateRefundRequest.from_json(json)
# print the JSON string representation of the object
print OrderCreateRefundRequest.to_json()

# convert the object into a dict
order_create_refund_request_dict = order_create_refund_request_instance.to_dict()
# create an instance of OrderCreateRefundRequest from a dict
order_create_refund_request_form_dict = order_create_refund_request.from_dict(order_create_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


