# TerminalPaymentEntity

terminal payment entity full object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_payment_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**entity** | **str** |  | [optional] 
**error_details** | [**ErrorDetailsInPaymentsEntity**](ErrorDetailsInPaymentsEntity.md) |  | [optional] 
**is_captured** | **bool** |  | [optional] 
**order_amount** | **float** | Order amount can be different from payment amount if you collect service fee from the customer | [optional] 
**payment_group** | **str** | Type of payment group. One of [&#39;prepaid_card&#39;, &#39;upi_ppi_offline&#39;, &#39;cash&#39;, &#39;upi_credit_card&#39;, &#39;paypal&#39;, &#39;net_banking&#39;, &#39;cardless_emi&#39;, &#39;credit_card&#39;, &#39;bank_transfer&#39;, &#39;pay_later&#39;, &#39;debit_card_emi&#39;, &#39;debit_card&#39;, &#39;wallet&#39;, &#39;upi_ppi&#39;, &#39;upi&#39;, &#39;credit_card_emi&#39;] | [optional] 
**payment_currency** | **str** |  | [optional] 
**payment_amount** | **float** |  | [optional] 
**payment_time** | **str** | This is the time when the payment was initiated | [optional] 
**payment_completion_time** | **str** | This is the time when the payment reaches its terminal state | [optional] 
**payment_status** | **str** | The transaction status can be one of  [\&quot;SUCCESS\&quot;, \&quot;NOT_ATTEMPTED\&quot;, \&quot;FAILED\&quot;, \&quot;USER_DROPPED\&quot;, \&quot;VOID\&quot;, \&quot;CANCELLED\&quot;, \&quot;PENDING\&quot;] | [optional] 
**payment_message** | **str** |  | [optional] 
**bank_reference** | **str** |  | [optional] 
**auth_id** | **str** |  | [optional] 
**authorization** | [**AuthorizationInPaymentsEntity**](AuthorizationInPaymentsEntity.md) |  | [optional] 
**customer_details** | [**CustomerDetails**](CustomerDetails.md) |  | [optional] 
**payment_method** | [**TerminalPaymentEntityPaymentMethod**](TerminalPaymentEntityPaymentMethod.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.terminal_payment_entity import TerminalPaymentEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalPaymentEntity from a JSON string
terminal_payment_entity_instance = TerminalPaymentEntity.from_json(json)
# print the JSON string representation of the object
print(TerminalPaymentEntity.to_json())

# convert the object into a dict
terminal_payment_entity_dict = terminal_payment_entity_instance.to_dict()
# create an instance of TerminalPaymentEntity from a dict
terminal_payment_entity_from_dict = TerminalPaymentEntity.from_dict(terminal_payment_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


