# InternationalPaymentEntity

International payment details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**international** | **bool** |  | [optional] 

## Example

```python
from cashfree_pg.models.international_payment_entity import InternationalPaymentEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalPaymentEntity from a JSON string
international_payment_entity_instance = InternationalPaymentEntity.from_json(json)
# print the JSON string representation of the object
print InternationalPaymentEntity.to_json()

# convert the object into a dict
international_payment_entity_dict = international_payment_entity_instance.to_dict()
# create an instance of InternationalPaymentEntity from a dict
international_payment_entity_form_dict = international_payment_entity.from_dict(international_payment_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


