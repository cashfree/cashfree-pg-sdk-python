# PaymentWebhookOrderEntity

order entity in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**order_amount** | **float** |  | [optional] 
**order_currency** | **str** |  | [optional] 
**order_tags** | **Dict[str, str]** | Custom Tags in thr form of {\&quot;key\&quot;:\&quot;value\&quot;} which can be passed for an order. A maximum of 10 tags can be added | [optional] 

## Example

```python
from cashfree_pg.models.payment_webhook_order_entity import PaymentWebhookOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWebhookOrderEntity from a JSON string
payment_webhook_order_entity_instance = PaymentWebhookOrderEntity.from_json(json)
# print the JSON string representation of the object
print PaymentWebhookOrderEntity.to_json()

# convert the object into a dict
payment_webhook_order_entity_dict = payment_webhook_order_entity_instance.to_dict()
# create an instance of PaymentWebhookOrderEntity from a dict
payment_webhook_order_entity_form_dict = payment_webhook_order_entity.from_dict(payment_webhook_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


