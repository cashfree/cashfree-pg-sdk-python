# CreateSubscriptionPaymentRequestEnach

payment method enach.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_bank_code** | **str** | Account bank code (required without AccountIFSC) | [optional] 
**account_holder_name** | **str** | Account holder name | [optional] 
**account_ifsc** | **str** | Account IFSC | [optional] 
**account_number** | **str** | Account number | [optional] 
**account_type** | **str** | Account type | [optional] 
**auth_mode** | **str** | Authentication mode. can be debit_card, aadhaar, or net_banking | [optional] 
**channel** | **str** | Channel. can be link | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_payment_request_enach import CreateSubscriptionPaymentRequestEnach

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPaymentRequestEnach from a JSON string
create_subscription_payment_request_enach_instance = CreateSubscriptionPaymentRequestEnach.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPaymentRequestEnach.to_json()

# convert the object into a dict
create_subscription_payment_request_enach_dict = create_subscription_payment_request_enach_instance.to_dict()
# create an instance of CreateSubscriptionPaymentRequestEnach from a dict
create_subscription_payment_request_enach_form_dict = create_subscription_payment_request_enach.from_dict(create_subscription_payment_request_enach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


