# PaymentEntityPaymentSurcharge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_surcharge_service_charge** | **float** |  | [optional] 
**payment_surcharge_service_tax** | **float** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_entity_payment_surcharge import PaymentEntityPaymentSurcharge

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEntityPaymentSurcharge from a JSON string
payment_entity_payment_surcharge_instance = PaymentEntityPaymentSurcharge.from_json(json)
# print the JSON string representation of the object
print PaymentEntityPaymentSurcharge.to_json()

# convert the object into a dict
payment_entity_payment_surcharge_dict = payment_entity_payment_surcharge_instance.to_dict()
# create an instance of PaymentEntityPaymentSurcharge from a dict
payment_entity_payment_surcharge_form_dict = payment_entity_payment_surcharge.from_dict(payment_entity_payment_surcharge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


