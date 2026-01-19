# CreateSubscriptionPaymentRequestPnach

payment method pnach.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_bank_code** | **str** | Account bank code | [optional] 
**account_holder_name** | **str** | Account holder name | [optional] 
**account_ifsc** | **str** | Account IFSC | [optional] 
**account_number** | **str** | Account number | [optional] 
**account_type** | **str** | Account type | [optional] 
**channel** | **str** | Channel. can be post | [optional] 
**mandate_creation_date** | **str** | Mandate creation date | [optional] 
**mandate_start_date** | **str** | Mandate start date | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_payment_request_pnach import CreateSubscriptionPaymentRequestPnach

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPaymentRequestPnach from a JSON string
create_subscription_payment_request_pnach_instance = CreateSubscriptionPaymentRequestPnach.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPaymentRequestPnach.to_json()

# convert the object into a dict
create_subscription_payment_request_pnach_dict = create_subscription_payment_request_pnach_instance.to_dict()
# create an instance of CreateSubscriptionPaymentRequestPnach from a dict
create_subscription_payment_request_pnach_form_dict = create_subscription_payment_request_pnach.from_dict(create_subscription_payment_request_pnach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


