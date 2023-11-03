# CardlessEMIPaymentMethod

cardless EMI payment method object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardless_emi** | [**CardlessEMI**](CardlessEMI.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.cardless_emi_payment_method import CardlessEMIPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of CardlessEMIPaymentMethod from a JSON string
cardless_emi_payment_method_instance = CardlessEMIPaymentMethod.from_json(json)
# print the JSON string representation of the object
print CardlessEMIPaymentMethod.to_json()

# convert the object into a dict
cardless_emi_payment_method_dict = cardless_emi_payment_method_instance.to_dict()
# create an instance of CardlessEMIPaymentMethod from a dict
cardless_emi_payment_method_form_dict = cardless_emi_payment_method.from_dict(cardless_emi_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


