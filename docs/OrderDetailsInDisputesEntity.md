# OrderDetailsInDisputesEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**order_currency** | **str** |  | [optional] 
**order_amount** | **float** |  | [optional] 
**cf_payment_id** | **str** |  | [optional] 
**payment_currency** | **str** |  | [optional] 
**payment_amount** | **float** |  | [optional] 

## Example

```python
from cashfree_pg.models.order_details_in_disputes_entity import OrderDetailsInDisputesEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailsInDisputesEntity from a JSON string
order_details_in_disputes_entity_instance = OrderDetailsInDisputesEntity.from_json(json)
# print the JSON string representation of the object
print OrderDetailsInDisputesEntity.to_json()

# convert the object into a dict
order_details_in_disputes_entity_dict = order_details_in_disputes_entity_instance.to_dict()
# create an instance of OrderDetailsInDisputesEntity from a dict
order_details_in_disputes_entity_form_dict = order_details_in_disputes_entity.from_dict(order_details_in_disputes_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


