# EligibilityMethodItemEntityDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_types** | **List[str]** | List of account types associated with the payment method. (e.g. SAVINGS or CURRENT) | [optional] 
**frequent_bank_details** | [**List[SubscriptionBankDetails]**](SubscriptionBankDetails.md) | List of the most frequently used banks. | [optional] 
**all_bank_details** | [**List[SubscriptionBankDetails]**](SubscriptionBankDetails.md) | Details about all banks associated with the payment method. | [optional] 
**available_handles** | [**List[EligibilityMethodItemEntityDetailsAvailableHandlesInner]**](EligibilityMethodItemEntityDetailsAvailableHandlesInner.md) | List of supported VPA handles. | [optional] 
**allowed_card_types** | **List[str]** | List of allowed card types. (e.g. DEBIT_CARD, CREDIT_CARD) | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_method_item_entity_details import EligibilityMethodItemEntityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityMethodItemEntityDetails from a JSON string
eligibility_method_item_entity_details_instance = EligibilityMethodItemEntityDetails.from_json(json)
# print the JSON string representation of the object
print EligibilityMethodItemEntityDetails.to_json()

# convert the object into a dict
eligibility_method_item_entity_details_dict = eligibility_method_item_entity_details_instance.to_dict()
# create an instance of EligibilityMethodItemEntityDetails from a dict
eligibility_method_item_entity_details_form_dict = eligibility_method_item_entity_details.from_dict(eligibility_method_item_entity_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


