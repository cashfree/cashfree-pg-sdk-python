# PaymentMethodsQueries

Payment Method Query Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the order. | [optional] 
**order_id** | **str** | OrderId of the order. Either of &#x60;order_id&#x60; or &#x60;order_amount&#x60; is mandatory. | [optional] 

## Example

```python
from cashfree_pg.models.payment_methods_queries import PaymentMethodsQueries

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodsQueries from a JSON string
payment_methods_queries_instance = PaymentMethodsQueries.from_json(json)
# print the JSON string representation of the object
print PaymentMethodsQueries.to_json()

# convert the object into a dict
payment_methods_queries_dict = payment_methods_queries_instance.to_dict()
# create an instance of PaymentMethodsQueries from a dict
payment_methods_queries_form_dict = payment_methods_queries.from_dict(payment_methods_queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


