# SubscriptionCustomerDetails

Subscription customer details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** | Name of the customer. | [optional] 
**customer_email** | **str** | Email of the customer. | 
**customer_phone** | **str** | Phone number of the customer. | 
**customer_bank_account_holder_name** | **str** | Bank holder name of the customer. | [optional] 
**customer_bank_account_number** | **str** | Bank account number of the customer. | [optional] 
**customer_bank_ifsc** | **str** | IFSC code of the customer. | [optional] 
**customer_bank_code** | **str** | Bank code of the customer. Refer to https://www.npci.org.in/PDF/nach/live-members-e-mandates/Live-Banks-in-API-E-Mandate.pdf | [optional] 
**customer_bank_account_type** | **str** | Bank account type of the customer. | [optional] 

## Example

```python
from cashfree_pg.models.subscription_customer_details import SubscriptionCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCustomerDetails from a JSON string
subscription_customer_details_instance = SubscriptionCustomerDetails.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCustomerDetails.to_json())

# convert the object into a dict
subscription_customer_details_dict = subscription_customer_details_instance.to_dict()
# create an instance of SubscriptionCustomerDetails from a dict
subscription_customer_details_from_dict = SubscriptionCustomerDetails.from_dict(subscription_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


