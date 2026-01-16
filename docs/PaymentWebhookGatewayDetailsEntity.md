# PaymentWebhookGatewayDetailsEntity

payment gatewat details present in the webhook response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_name** | **str** |  | [optional] 
**gateway_order_id** | **str** |  | [optional] 
**gateway_payment_id** | **str** |  | [optional] 
**gateway_status_code** | **str** |  | [optional] 
**gateway_settlement** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_webhook_gateway_details_entity import PaymentWebhookGatewayDetailsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWebhookGatewayDetailsEntity from a JSON string
payment_webhook_gateway_details_entity_instance = PaymentWebhookGatewayDetailsEntity.from_json(json)
# print the JSON string representation of the object
print PaymentWebhookGatewayDetailsEntity.to_json()

# convert the object into a dict
payment_webhook_gateway_details_entity_dict = payment_webhook_gateway_details_entity_instance.to_dict()
# create an instance of PaymentWebhookGatewayDetailsEntity from a dict
payment_webhook_gateway_details_entity_form_dict = payment_webhook_gateway_details_entity.from_dict(payment_webhook_gateway_details_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


