# OrderMetaPaymentMethodsFiltersFiltersCardSchemes

Allowed card schemes for the order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | It accepts value of \&quot;ALLOW\&quot; and allows only those schemes present in it&#39;s neighbouring parameter \&quot;values\&quot; | [optional] 
**values** | **List[str]** | List of card schemes to be allowed for the order | [optional] 

## Example

```python
from cashfree_pg.models.order_meta_payment_methods_filters_filters_card_schemes import OrderMetaPaymentMethodsFiltersFiltersCardSchemes

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMetaPaymentMethodsFiltersFiltersCardSchemes from a JSON string
order_meta_payment_methods_filters_filters_card_schemes_instance = OrderMetaPaymentMethodsFiltersFiltersCardSchemes.from_json(json)
# print the JSON string representation of the object
print OrderMetaPaymentMethodsFiltersFiltersCardSchemes.to_json()

# convert the object into a dict
order_meta_payment_methods_filters_filters_card_schemes_dict = order_meta_payment_methods_filters_filters_card_schemes_instance.to_dict()
# create an instance of OrderMetaPaymentMethodsFiltersFiltersCardSchemes from a dict
order_meta_payment_methods_filters_filters_card_schemes_form_dict = order_meta_payment_methods_filters_filters_card_schemes.from_dict(order_meta_payment_methods_filters_filters_card_schemes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


