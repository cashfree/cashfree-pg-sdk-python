# RefundEntity

The refund entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_payment_id** | **int** | Cashfree Payments ID of the payment for which refund is initiated | [optional] 
**cf_refund_id** | **str** | Cashfree Payments ID for a refund | [optional] 
**order_id** | **str** | Merchant’s order Id of the order for which refund is initiated | [optional] 
**refund_id** | **str** | Merchant’s refund ID of the refund | [optional] 
**entity** | **str** | Type of object | [optional] 
**refund_amount** | **float** | Amount that is refunded | [optional] 
**refund_currency** | **str** | Currency of the refund amount | [optional] 
**refund_note** | **str** | Note added by merchant for the refund | [optional] 
**refund_status** | **str** | This can be one of [\&quot;SUCCESS\&quot;, \&quot;PENDING\&quot;, \&quot;CANCELLED\&quot;, \&quot;ONHOLD\&quot;, \&quot;FAILED\&quot;] | [optional] 
**refund_arn** | **str** | The bank reference number for refund | [optional] 
**refund_charge** | **float** | Charges in INR for processing refund | [optional] 
**status_description** | **str** | Description of refund status | [optional] 
**metadata** | **object** | Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs | [optional] 
**refund_splits** | [**List[VendorSplit]**](VendorSplit.md) |  | [optional] 
**refund_type** | **str** | This can be one of [\&quot;PAYMENT_AUTO_REFUND\&quot;, \&quot;MERCHANT_INITIATED\&quot;, \&quot;UNRECONCILED_AUTO_REFUND\&quot;] | [optional] 
**refund_mode** | **str** | Method or speed of processing refund | [optional] 
**created_at** | **str** | Time of refund creation | [optional] 
**processed_at** | **str** | Time when refund was processed successfully | [optional] 
**refund_speed** | [**RefundSpeed**](RefundSpeed.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.refund_entity import RefundEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RefundEntity from a JSON string
refund_entity_instance = RefundEntity.from_json(json)
# print the JSON string representation of the object
print RefundEntity.to_json()

# convert the object into a dict
refund_entity_dict = refund_entity_instance.to_dict()
# create an instance of RefundEntity from a dict
refund_entity_form_dict = refund_entity.from_dict(refund_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


