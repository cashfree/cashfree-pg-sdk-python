# CreateSubscriptionPaymentRequestEnack

payment method enach.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel. can be link | [optional] 
**auth_mode** | **str** | Authentication mode. can be debit_card, aadhaar, or net_banking | [optional] 
**account_holder_name** | **str** | Account holder name | [optional] 
**account_number** | **str** | Account number | [optional] 
**account_bank_code** | **str** | Account bank code (required without AccountIFSC) | [optional] 
**account_type** | **str** | Account type | [optional] 
**account_ifsc** | **str** | Account IFSC | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_payment_request_enack import CreateSubscriptionPaymentRequestEnack

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPaymentRequestEnack from a JSON string
create_subscription_payment_request_enack_instance = CreateSubscriptionPaymentRequestEnack.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPaymentRequestEnack.to_json()

# convert the object into a dict
create_subscription_payment_request_enack_dict = create_subscription_payment_request_enack_instance.to_dict()
# create an instance of CreateSubscriptionPaymentRequestEnack from a dict
create_subscription_payment_request_enack_form_dict = create_subscription_payment_request_enack.from_dict(create_subscription_payment_request_enack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


