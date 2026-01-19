# CreateOrderSettlementRequestBodyMetaData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cbriks_id** | **str** | Meta data cbricks ID to be used for reporting purpose. | [optional] 
**settlement_date** | **date** | Requested Settlement Date. | [optional] 

## Example

```python
from cashfree_pg.models.create_order_settlement_request_body_meta_data import CreateOrderSettlementRequestBodyMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderSettlementRequestBodyMetaData from a JSON string
create_order_settlement_request_body_meta_data_instance = CreateOrderSettlementRequestBodyMetaData.from_json(json)
# print the JSON string representation of the object
print CreateOrderSettlementRequestBodyMetaData.to_json()

# convert the object into a dict
create_order_settlement_request_body_meta_data_dict = create_order_settlement_request_body_meta_data_instance.to_dict()
# create an instance of CreateOrderSettlementRequestBodyMetaData from a dict
create_order_settlement_request_body_meta_data_form_dict = create_order_settlement_request_body_meta_data.from_dict(create_order_settlement_request_body_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


