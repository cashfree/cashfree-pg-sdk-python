# PaymentWebhookDataEntity

data entity in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**PaymentWebhookOrderEntity**](PaymentWebhookOrderEntity.md) |  | [optional] 
**payment** | [**PaymentEntity**](PaymentEntity.md) |  | [optional] 
**customer_details** | [**PaymentWebhookCustomerEntity**](PaymentWebhookCustomerEntity.md) |  | [optional] 
**error_details** | [**PaymentWebhookErrorEntity**](PaymentWebhookErrorEntity.md) |  | [optional] 
**payment_gateway_details** | [**PaymentWebhookGatewayDetailsEntity**](PaymentWebhookGatewayDetailsEntity.md) |  | [optional] 
**payment_offers** | [**List[OfferEntity]**](OfferEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_webhook_data_entity import PaymentWebhookDataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWebhookDataEntity from a JSON string
payment_webhook_data_entity_instance = PaymentWebhookDataEntity.from_json(json)
# print the JSON string representation of the object
print PaymentWebhookDataEntity.to_json()

# convert the object into a dict
payment_webhook_data_entity_dict = payment_webhook_data_entity_instance.to_dict()
# create an instance of PaymentWebhookDataEntity from a dict
payment_webhook_data_entity_form_dict = payment_webhook_data_entity.from_dict(payment_webhook_data_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


