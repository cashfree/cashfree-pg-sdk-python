# AppPaymentMethod

App payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**App**](App.md) |  | 

## Example

```python
from cashfree_pg.models.app_payment_method import AppPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AppPaymentMethod from a JSON string
app_payment_method_instance = AppPaymentMethod.from_json(json)
# print the JSON string representation of the object
print AppPaymentMethod.to_json()

# convert the object into a dict
app_payment_method_dict = app_payment_method_instance.to_dict()
# create an instance of AppPaymentMethod from a dict
app_payment_method_form_dict = app_payment_method.from_dict(app_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


