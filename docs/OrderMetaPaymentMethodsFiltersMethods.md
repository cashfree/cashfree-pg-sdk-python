# OrderMetaPaymentMethodsFiltersMethods

Allowed payment modes for this order. credit_card, debit_card, netbanking, paylater, etc are the values that can be passed to this parameter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | It accepts value of \&quot;ALLOW\&quot; and allows only those modes present in it&#39;s neighbouring parameter \&quot;values\&quot; | [optional] 
**values** | **List[str]** | The accepted entries for this paramter are \&quot;debit_card, credit_card, prepaid_card, upi, wallet, netbanking, banktransfer, paylater, paypal, debit_card_emi, credit_card_emi, upi_credit_card, upi_ppi, cardless_emi, account_based_payment, corporate_credit_card, sbc_debit_card, sbc_emandate, sbc_upi, sbc_credit_card\&quot; | [optional] 

## Example

```python
from cashfree_pg.models.order_meta_payment_methods_filters_methods import OrderMetaPaymentMethodsFiltersMethods

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMetaPaymentMethodsFiltersMethods from a JSON string
order_meta_payment_methods_filters_methods_instance = OrderMetaPaymentMethodsFiltersMethods.from_json(json)
# print the JSON string representation of the object
print OrderMetaPaymentMethodsFiltersMethods.to_json()

# convert the object into a dict
order_meta_payment_methods_filters_methods_dict = order_meta_payment_methods_filters_methods_instance.to_dict()
# create an instance of OrderMetaPaymentMethodsFiltersMethods from a dict
order_meta_payment_methods_filters_methods_form_dict = order_meta_payment_methods_filters_methods.from_dict(order_meta_payment_methods_filters_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


