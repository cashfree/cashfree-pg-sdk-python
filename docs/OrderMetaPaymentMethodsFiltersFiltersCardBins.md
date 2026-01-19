# OrderMetaPaymentMethodsFiltersFiltersCardBins

Allowed card bins for the order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | It accepts value of \&quot;ALLOW\&quot; and allows only those bins present in it&#39;s neighbouring parameter \&quot;values\&quot; | [optional] 
**values** | **List[str]** | List of card bins to be allowed for the order | [optional] 

## Example

```python
from cashfree_pg.models.order_meta_payment_methods_filters_filters_card_bins import OrderMetaPaymentMethodsFiltersFiltersCardBins

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMetaPaymentMethodsFiltersFiltersCardBins from a JSON string
order_meta_payment_methods_filters_filters_card_bins_instance = OrderMetaPaymentMethodsFiltersFiltersCardBins.from_json(json)
# print the JSON string representation of the object
print OrderMetaPaymentMethodsFiltersFiltersCardBins.to_json()

# convert the object into a dict
order_meta_payment_methods_filters_filters_card_bins_dict = order_meta_payment_methods_filters_filters_card_bins_instance.to_dict()
# create an instance of OrderMetaPaymentMethodsFiltersFiltersCardBins from a dict
order_meta_payment_methods_filters_filters_card_bins_form_dict = order_meta_payment_methods_filters_filters_card_bins.from_dict(order_meta_payment_methods_filters_filters_card_bins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


