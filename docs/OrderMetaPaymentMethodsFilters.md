# OrderMetaPaymentMethodsFilters

Allowed payment modes for this order. Along with multiple filters for cards can be added to this key. And this filtering will be honoured during transaction creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | [**OrderMetaPaymentMethodsFiltersMethods**](OrderMetaPaymentMethodsFiltersMethods.md) |  | [optional] 
**filters** | [**OrderMetaPaymentMethodsFiltersFilters**](OrderMetaPaymentMethodsFiltersFilters.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.order_meta_payment_methods_filters import OrderMetaPaymentMethodsFilters

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMetaPaymentMethodsFilters from a JSON string
order_meta_payment_methods_filters_instance = OrderMetaPaymentMethodsFilters.from_json(json)
# print the JSON string representation of the object
print OrderMetaPaymentMethodsFilters.to_json()

# convert the object into a dict
order_meta_payment_methods_filters_dict = order_meta_payment_methods_filters_instance.to_dict()
# create an instance of OrderMetaPaymentMethodsFilters from a dict
order_meta_payment_methods_filters_form_dict = order_meta_payment_methods_filters.from_dict(order_meta_payment_methods_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


