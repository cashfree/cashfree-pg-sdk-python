# CreateSubscriptionRequestAuthorizationDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_amount** | **float** | Authorization amount for the auth payment. | [optional] 
**authorization_amount_refund** | **bool** | Indicates whether the authorization amount should be refunded to the customer automatically. Merchants can use this field to specify if the authorized funds should be returned to the customer after authorization of the subscription. | [optional] 
**payment_methods** | **List[str]** | Payment methods for the subscription. enach, pnach, upi, card are possible values. | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_request_authorization_details import CreateSubscriptionRequestAuthorizationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequestAuthorizationDetails from a JSON string
create_subscription_request_authorization_details_instance = CreateSubscriptionRequestAuthorizationDetails.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionRequestAuthorizationDetails.to_json()

# convert the object into a dict
create_subscription_request_authorization_details_dict = create_subscription_request_authorization_details_instance.to_dict()
# create an instance of CreateSubscriptionRequestAuthorizationDetails from a dict
create_subscription_request_authorization_details_form_dict = create_subscription_request_authorization_details.from_dict(create_subscription_request_authorization_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


