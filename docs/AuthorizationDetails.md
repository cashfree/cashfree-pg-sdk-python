# AuthorizationDetails

Details of the authorization done for the subscription. Returned in Get subscription and auth payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_amount** | **float** | Authorization amount for the auth payment. | [optional] 
**authorization_amount_refund** | **bool** | Indicates whether the authorization amount should be refunded to the customer automatically. Merchants can use this field to specify if the authorized funds should be returned to the customer after authorization of the subscription. | [optional] 
**authorization_reference** | **str** | Authorization reference. UMN for UPI, UMRN for EMandate/Physical Mandate and Enrollment ID for cards. | [optional] 
**authorization_time** | **str** | Authorization time. | [optional] 
**authorization_status** | **str** | Status of the authorization. | [optional] 
**payment_id** | **str** | A unique ID passed by merchant for identifying the transaction. | [optional] 
**payment_method** | **str** | Payment method used for the authorization. | [optional] 

## Example

```python
from cashfree_pg.models.authorization_details import AuthorizationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationDetails from a JSON string
authorization_details_instance = AuthorizationDetails.from_json(json)
# print the JSON string representation of the object
print(AuthorizationDetails.to_json())

# convert the object into a dict
authorization_details_dict = authorization_details_instance.to_dict()
# create an instance of AuthorizationDetails from a dict
authorization_details_from_dict = AuthorizationDetails.from_dict(authorization_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


