# CreateSubscriptionPaymentRequestPaymentMethod

Payment method. Can be one of [\"upi\", \"enach\", \"pnach\", \"card\"]

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upi_id** | **str** |  | [optional] 
**channel** | **str** | Channel. can be link | [optional] 
**auth_mode** | **str** | Authentication mode. can be debit_card, aadhaar, or net_banking | [optional] 
**account_holder_name** | **str** | Account holder name | [optional] 
**account_number** | **str** | Account number | [optional] 
**account_bank_code** | **str** | Account bank code | [optional] 
**account_type** | **str** | Account type | [optional] 
**account_ifsc** | **str** | Account IFSC | [optional] 
**mandate_creation_date** | **str** | Mandate creation date | [optional] 
**mandate_start_date** | **str** | Mandate start date | [optional] 
**card_number** | **str** | Card number | [optional] 
**card_holder_name** | **str** | Card holder name | [optional] 
**card_expiry_mm** | **str** | Card expiry month | [optional] 
**card_expiry_yy** | **str** | Card expiry year | [optional] 
**card_cvv** | **str** | Card CVV | [optional] 
**card_network** | **str** | Card network | [optional] 
**card_type** | **str** | Card type | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_payment_request_payment_method import CreateSubscriptionPaymentRequestPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPaymentRequestPaymentMethod from a JSON string
create_subscription_payment_request_payment_method_instance = CreateSubscriptionPaymentRequestPaymentMethod.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPaymentRequestPaymentMethod.to_json()

# convert the object into a dict
create_subscription_payment_request_payment_method_dict = create_subscription_payment_request_payment_method_instance.to_dict()
# create an instance of CreateSubscriptionPaymentRequestPaymentMethod from a dict
create_subscription_payment_request_payment_method_form_dict = create_subscription_payment_request_payment_method.from_dict(create_subscription_payment_request_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


