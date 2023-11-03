# EligibilityCardlessEMIEntity

Carless EMI eligible entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility** | **bool** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_value** | **str** |  | [optional] 
**entity_details** | [**CardlessEMIEntity**](CardlessEMIEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_cardless_emi_entity import EligibilityCardlessEMIEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityCardlessEMIEntity from a JSON string
eligibility_cardless_emi_entity_instance = EligibilityCardlessEMIEntity.from_json(json)
# print the JSON string representation of the object
print EligibilityCardlessEMIEntity.to_json()

# convert the object into a dict
eligibility_cardless_emi_entity_dict = eligibility_cardless_emi_entity_instance.to_dict()
# create an instance of EligibilityCardlessEMIEntity from a dict
eligibility_cardless_emi_entity_form_dict = eligibility_cardless_emi_entity.from_dict(eligibility_cardless_emi_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


