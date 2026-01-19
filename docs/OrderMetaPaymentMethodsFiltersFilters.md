# OrderMetaPaymentMethodsFiltersFilters

This object takes details of all the filtering that has to be done for this order. Filters on card bins, card schemes, card issuing bank and card suffixes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_bins** | [**OrderMetaPaymentMethodsFiltersFiltersCardBins**](OrderMetaPaymentMethodsFiltersFiltersCardBins.md) |  | [optional] 
**card_schemes** | [**OrderMetaPaymentMethodsFiltersFiltersCardSchemes**](OrderMetaPaymentMethodsFiltersFiltersCardSchemes.md) |  | [optional] 
**card_suffix** | [**OrderMetaPaymentMethodsFiltersFiltersCardSuffix**](OrderMetaPaymentMethodsFiltersFiltersCardSuffix.md) |  | [optional] 
**card_issuing_bank** | [**OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank**](OrderMetaPaymentMethodsFiltersFiltersCardIssuingBank.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.order_meta_payment_methods_filters_filters import OrderMetaPaymentMethodsFiltersFilters

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMetaPaymentMethodsFiltersFilters from a JSON string
order_meta_payment_methods_filters_filters_instance = OrderMetaPaymentMethodsFiltersFilters.from_json(json)
# print the JSON string representation of the object
print OrderMetaPaymentMethodsFiltersFilters.to_json()

# convert the object into a dict
order_meta_payment_methods_filters_filters_dict = order_meta_payment_methods_filters_filters_instance.to_dict()
# create an instance of OrderMetaPaymentMethodsFiltersFilters from a dict
order_meta_payment_methods_filters_filters_form_dict = order_meta_payment_methods_filters_filters.from_dict(order_meta_payment_methods_filters_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


