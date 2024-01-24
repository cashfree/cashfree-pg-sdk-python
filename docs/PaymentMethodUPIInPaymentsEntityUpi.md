# PaymentMethodUPIInPaymentsEntityUpi


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**upi_id** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_method_upiin_payments_entity_upi import PaymentMethodUPIInPaymentsEntityUpi

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodUPIInPaymentsEntityUpi from a JSON string
payment_method_upiin_payments_entity_upi_instance = PaymentMethodUPIInPaymentsEntityUpi.from_json(json)
# print the JSON string representation of the object
print PaymentMethodUPIInPaymentsEntityUpi.to_json()

# convert the object into a dict
payment_method_upiin_payments_entity_upi_dict = payment_method_upiin_payments_entity_upi_instance.to_dict()
# create an instance of PaymentMethodUPIInPaymentsEntityUpi from a dict
payment_method_upiin_payments_entity_upi_form_dict = payment_method_upiin_payments_entity_upi.from_dict(payment_method_upiin_payments_entity_upi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


