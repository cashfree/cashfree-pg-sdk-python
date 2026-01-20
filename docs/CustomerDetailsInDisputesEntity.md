# CustomerDetailsInDisputesEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** |  | [optional] 
**customer_phone** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.customer_details_in_disputes_entity import CustomerDetailsInDisputesEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerDetailsInDisputesEntity from a JSON string
customer_details_in_disputes_entity_instance = CustomerDetailsInDisputesEntity.from_json(json)
# print the JSON string representation of the object
print(CustomerDetailsInDisputesEntity.to_json())

# convert the object into a dict
customer_details_in_disputes_entity_dict = customer_details_in_disputes_entity_instance.to_dict()
# create an instance of CustomerDetailsInDisputesEntity from a dict
customer_details_in_disputes_entity_from_dict = CustomerDetailsInDisputesEntity.from_dict(customer_details_in_disputes_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


