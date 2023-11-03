# PaymentURLObject

URL for payment retrieval for an order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_url_object import PaymentURLObject

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentURLObject from a JSON string
payment_url_object_instance = PaymentURLObject.from_json(json)
# print the JSON string representation of the object
print PaymentURLObject.to_json()

# convert the object into a dict
payment_url_object_dict = payment_url_object_instance.to_dict()
# create an instance of PaymentURLObject from a dict
payment_url_object_form_dict = payment_url_object.from_dict(payment_url_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


