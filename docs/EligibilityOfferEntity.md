# EligibilityOfferEntity

Eligible offer object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility** | **bool** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_value** | **str** |  | [optional] 
**entity_details** | [**OfferEntity**](OfferEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_offer_entity import EligibilityOfferEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityOfferEntity from a JSON string
eligibility_offer_entity_instance = EligibilityOfferEntity.from_json(json)
# print the JSON string representation of the object
print EligibilityOfferEntity.to_json()

# convert the object into a dict
eligibility_offer_entity_dict = eligibility_offer_entity_instance.to_dict()
# create an instance of EligibilityOfferEntity from a dict
eligibility_offer_entity_form_dict = eligibility_offer_entity.from_dict(eligibility_offer_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


