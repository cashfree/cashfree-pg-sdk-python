# CreateLinkRequest

Request paramenters for link creation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **str** | Unique Identifier (provided by merchant) for the Link. Alphanumeric and only - and _ allowed (50 character limit). Use this for other link-related APIs. | 
**link_amount** | **float** | Amount to be collected using this link. Provide upto two decimals for paise. | 
**link_currency** | **str** | Currency for the payment link. Default is INR. Contact care@cashfree.com to enable new currencies. | 
**link_purpose** | **str** | A brief description for which payment must be collected. This is shown to the customer. | 
**customer_details** | [**LinkCustomerDetailsEntity**](LinkCustomerDetailsEntity.md) |  | 
**link_partial_payments** | **bool** | If \&quot;true\&quot;, customer can make partial payments for the link. | [optional] 
**link_minimum_partial_amount** | **float** | Minimum amount in first installment that needs to be paid by the customer if partial payments are enabled. This should be less than the link_amount. | [optional] 
**link_expiry_time** | **str** | Time after which the link expires. Customers will not be able to make the payment beyond the time specified here. You can provide them in a valid ISO 8601 time format. Default is 30 days. | [optional] 
**link_notify** | [**LinkNotifyEntity**](LinkNotifyEntity.md) |  | [optional] 
**link_auto_reminders** | **bool** | If \&quot;true\&quot;, reminders will be sent to customers for collecting payments. | [optional] 
**link_notes** | **Dict[str, str]** | Key-value pair that can be used to store additional information about the entity. Maximum 5 key-value pairs | [optional] 
**link_meta** | [**LinkMetaEntity**](LinkMetaEntity.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.create_link_request import CreateLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLinkRequest from a JSON string
create_link_request_instance = CreateLinkRequest.from_json(json)
# print the JSON string representation of the object
print CreateLinkRequest.to_json()

# convert the object into a dict
create_link_request_dict = create_link_request_instance.to_dict()
# create an instance of CreateLinkRequest from a dict
create_link_request_form_dict = create_link_request.from_dict(create_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


