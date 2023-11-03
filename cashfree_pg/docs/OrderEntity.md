# OrderEntity

The complete order entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_order_id** | **int** | unique id generated by cashfree for your order | [optional] 
**order_id** | **str** | order_id sent during the api request | [optional] 
**entity** | **str** | Type of the entity. | [optional] 
**order_currency** | **str** | Currency of the order. Example INR | [optional] 
**order_amount** | **float** |  | [optional] 
**order_status** | **str** | Possible values are  - &#x60;ACTIVE&#x60;: Order does not have a sucessful transaction yet - &#x60;PAID&#x60;: Order is PAID with one successful transaction - &#x60;EXPIRED&#x60;: Order was not PAID and not it has expired. No transaction can be initiated for an EXPIRED order.  | [optional] 
**payment_session_id** | **str** |  | [optional] 
**order_expiry_time** | **datetime** |  | [optional] 
**order_note** | **str** | Additional note for order | [optional] 
**created_at** | **datetime** | When the order was created at cashfree&#39;s server | [optional] 
**order_splits** | [**List[VendorSplit]**](VendorSplit.md) |  | [optional] 
**customer_details** | [**CustomerDetails**](CustomerDetails.md) |  | [optional] 
**order_meta** | [**OrderMeta**](OrderMeta.md) |  | [optional] 
**payments** | [**PaymentURLObject**](PaymentURLObject.md) |  | [optional] 
**settlements** | [**SettlementURLObject**](SettlementURLObject.md) |  | [optional] 
**refunds** | [**RefundURLObject**](RefundURLObject.md) |  | [optional] 
**order_tags** | **Dict[str, str]** | Custom Tags in thr form of {\&quot;key\&quot;:\&quot;value\&quot;} which can be passed for an order. A maximum of 10 tags can be added | [optional] 

## Example

```python
from cashfree_pg.models.order_entity import OrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEntity from a JSON string
order_entity_instance = OrderEntity.from_json(json)
# print the JSON string representation of the object
print OrderEntity.to_json()

# convert the object into a dict
order_entity_dict = order_entity_instance.to_dict()
# create an instance of OrderEntity from a dict
order_entity_form_dict = order_entity.from_dict(order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

