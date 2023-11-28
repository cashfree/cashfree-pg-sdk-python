# PaymentMethodsFilters

Filter for specific Payment Methods

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_methods** | **List[str]** | Array of payment methods to be filtered. This is optional, by default all payment methods will be returned. Possible values in [ &#39;debit_card&#39;, &#39;credit_card&#39;, &#39;prepaid_card&#39;, &#39;corporate_credit_card&#39;, &#39;upi&#39;, &#39;wallet&#39;, &#39;netbanking&#39;, &#39;banktransfer&#39;, &#39;paylater&#39;, &#39;paypal&#39;, &#39;debit_card_emi&#39;, &#39;credit_card_emi&#39;, &#39;upi_credit_card&#39;, &#39;upi_ppi&#39;, &#39;cardless_emi&#39;, &#39;account_based_payment&#39; ]  | [optional] 

## Example

```python
from cashfree_pg.models.payment_methods_filters import PaymentMethodsFilters

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodsFilters from a JSON string
payment_methods_filters_instance = PaymentMethodsFilters.from_json(json)
# print the JSON string representation of the object
print PaymentMethodsFilters.to_json()

# convert the object into a dict
payment_methods_filters_dict = payment_methods_filters_instance.to_dict()
# create an instance of PaymentMethodsFilters from a dict
payment_methods_filters_form_dict = payment_methods_filters.from_dict(payment_methods_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


