# CreateOrderSettlementRequestBody

Create Order Settlement Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | OrderId of the order. | 
**meta_data** | [**CreateOrderSettlementRequestBodyMetaData**](CreateOrderSettlementRequestBodyMetaData.md) |  | 

## Example

```python
from cashfree_pg.models.create_order_settlement_request_body import CreateOrderSettlementRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderSettlementRequestBody from a JSON string
create_order_settlement_request_body_instance = CreateOrderSettlementRequestBody.from_json(json)
# print the JSON string representation of the object
print CreateOrderSettlementRequestBody.to_json()

# convert the object into a dict
create_order_settlement_request_body_dict = create_order_settlement_request_body_instance.to_dict()
# create an instance of CreateOrderSettlementRequestBody from a dict
create_order_settlement_request_body_form_dict = create_order_settlement_request_body.from_dict(create_order_settlement_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


