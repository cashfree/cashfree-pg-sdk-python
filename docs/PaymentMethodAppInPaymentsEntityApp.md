# PaymentMethodAppInPaymentsEntityApp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_app_in_payments_entity_app import PaymentMethodAppInPaymentsEntityApp

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodAppInPaymentsEntityApp from a JSON string
payment_method_app_in_payments_entity_app_instance = PaymentMethodAppInPaymentsEntityApp.from_json(json)
# print the JSON string representation of the object
print PaymentMethodAppInPaymentsEntityApp.to_json()

# convert the object into a dict
payment_method_app_in_payments_entity_app_dict = payment_method_app_in_payments_entity_app_instance.to_dict()
# create an instance of PaymentMethodAppInPaymentsEntityApp from a dict
payment_method_app_in_payments_entity_app_form_dict = payment_method_app_in_payments_entity_app.from_dict(payment_method_app_in_payments_entity_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


