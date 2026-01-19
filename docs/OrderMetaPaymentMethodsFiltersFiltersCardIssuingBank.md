# OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank

Allowed card issuing bank for the order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | It accepts value of \&quot;ALLOW\&quot; and allows only those issuing bank present in it&#39;s neighbouring parameter \&quot;values\&quot; | [optional] 
**values** | **List[str]** | List of card issuing bank to be allowed for the order | [optional] 

## Example

```python
from cashfree_pg.models.order_meta_payment_methods_filters_filters_card_issuing_bank import OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank from a JSON string
order_meta_payment_methods_filters_filters_card_issuing_bank_instance = OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank.from_json(json)
# print the JSON string representation of the object
print OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank.to_json()

# convert the object into a dict
order_meta_payment_methods_filters_filters_card_issuing_bank_dict = order_meta_payment_methods_filters_filters_card_issuing_bank_instance.to_dict()
# create an instance of OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank from a dict
order_meta_payment_methods_filters_filters_card_issuing_bank_form_dict = order_meta_payment_methods_filters_filters_card_issuing_bank.from_dict(order_meta_payment_methods_filters_filters_card_issuing_bank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


