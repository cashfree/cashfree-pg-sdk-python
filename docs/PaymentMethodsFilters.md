# PaymentMethodsFilters

Filter for Payment Methods

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_methods** | **List[str]** | Array of payment methods to be filtered. | [optional] 

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


