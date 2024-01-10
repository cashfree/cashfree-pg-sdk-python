# PaymentWebhookCustomerEntity

customer details object in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_phone** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_webhook_customer_entity import PaymentWebhookCustomerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWebhookCustomerEntity from a JSON string
payment_webhook_customer_entity_instance = PaymentWebhookCustomerEntity.from_json(json)
# print the JSON string representation of the object
print PaymentWebhookCustomerEntity.to_json()

# convert the object into a dict
payment_webhook_customer_entity_dict = payment_webhook_customer_entity_instance.to_dict()
# create an instance of PaymentWebhookCustomerEntity from a dict
payment_webhook_customer_entity_form_dict = payment_webhook_customer_entity.from_dict(payment_webhook_customer_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


