# TerminalTransactionEntity

Create terminal response object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_payment_id** | **int** |  | [optional] 
**payment_amount** | **int** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**payment_url** | **str** |  | [optional] 
**qrcode** | **str** |  | [optional] 
**timeout** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.terminal_transaction_entity import TerminalTransactionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalTransactionEntity from a JSON string
terminal_transaction_entity_instance = TerminalTransactionEntity.from_json(json)
# print the JSON string representation of the object
print TerminalTransactionEntity.to_json()

# convert the object into a dict
terminal_transaction_entity_dict = terminal_transaction_entity_instance.to_dict()
# create an instance of TerminalTransactionEntity from a dict
terminal_transaction_entity_form_dict = terminal_transaction_entity.from_dict(terminal_transaction_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


