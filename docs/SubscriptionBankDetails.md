# SubscriptionBankDetails

Bank details object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_id** | **str** | ID of the bank. | [optional] 
**bank_name** | **str** | Name of the bank. | [optional] 
**account_auth_modes** | **List[str]** | List of account authentication modes supported by the bank. (e.g. DEBIT_CARD, NET_BANKING, AADHAAR) | [optional] 

## Example

```python
from cashfree_pg.models.subscription_bank_details import SubscriptionBankDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionBankDetails from a JSON string
subscription_bank_details_instance = SubscriptionBankDetails.from_json(json)
# print the JSON string representation of the object
print(SubscriptionBankDetails.to_json())

# convert the object into a dict
subscription_bank_details_dict = subscription_bank_details_instance.to_dict()
# create an instance of SubscriptionBankDetails from a dict
subscription_bank_details_from_dict = SubscriptionBankDetails.from_dict(subscription_bank_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


