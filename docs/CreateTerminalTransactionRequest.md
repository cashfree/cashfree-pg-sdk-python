# CreateTerminalTransactionRequest

Request body to create a terminal transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_order_id** | **int** | cashfree order ID that was returned while creating an order. | 
**cf_terminal_id** | **int** | cashfree terminal id. this is a required parameter when you do not provide the terminal phone number. | [optional] 
**payment_method** | **str** | mention the payment method used for the transaction. possible values - QR_CODE, LINK. | 
**terminal_phone_no** | **str** | agent mobile number assigned to the terminal. this is a required parameter when you do not provide the cf_terminal_id. | [optional] 

## Example

```python
from cashfree_pg.models.create_terminal_transaction_request import CreateTerminalTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTerminalTransactionRequest from a JSON string
create_terminal_transaction_request_instance = CreateTerminalTransactionRequest.from_json(json)
# print the JSON string representation of the object
print CreateTerminalTransactionRequest.to_json()

# convert the object into a dict
create_terminal_transaction_request_dict = create_terminal_transaction_request_instance.to_dict()
# create an instance of CreateTerminalTransactionRequest from a dict
create_terminal_transaction_request_form_dict = create_terminal_transaction_request.from_dict(create_terminal_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


