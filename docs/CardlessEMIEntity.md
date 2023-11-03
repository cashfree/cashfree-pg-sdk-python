# CardlessEMIEntity

cardless EMI object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** |  | [optional] 
**emi_plans** | [**List[EMIPlansArray]**](EMIPlansArray.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.cardless_emi_entity import CardlessEMIEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CardlessEMIEntity from a JSON string
cardless_emi_entity_instance = CardlessEMIEntity.from_json(json)
# print the JSON string representation of the object
print CardlessEMIEntity.to_json()

# convert the object into a dict
cardless_emi_entity_dict = cardless_emi_entity_instance.to_dict()
# create an instance of CardlessEMIEntity from a dict
cardless_emi_entity_form_dict = cardless_emi_entity.from_dict(cardless_emi_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


