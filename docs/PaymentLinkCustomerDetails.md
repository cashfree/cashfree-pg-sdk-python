# PaymentLinkCustomerDetails

The customer details that are necessary. Note that you can pass dummy details if your use case does not require the customer details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A unique identifier for the customer. Use alphanumeric values only. | [optional] 
**customer_email** | **str** | Customer email address. | [optional] 
**customer_phone** | **str** | Customer phone number. | 
**customer_name** | **str** | Name of the customer. | [optional] 
**customer_bank_account_number** | **str** | Customer bank account. Required if you want to do a bank account check (TPV) | [optional] 
**customer_bank_ifsc** | **str** | Customer bank IFSC. Required if you want to do a bank account check (TPV) | [optional] 
**customer_bank_code** | **float** | Customer bank code. Required for net banking payments, if you want to do a bank account check (TPV) | [optional] 

## Example

```python
from cashfree_pg.models.payment_link_customer_details import PaymentLinkCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkCustomerDetails from a JSON string
payment_link_customer_details_instance = PaymentLinkCustomerDetails.from_json(json)
# print the JSON string representation of the object
print PaymentLinkCustomerDetails.to_json()

# convert the object into a dict
payment_link_customer_details_dict = payment_link_customer_details_instance.to_dict()
# create an instance of PaymentLinkCustomerDetails from a dict
payment_link_customer_details_form_dict = payment_link_customer_details.from_dict(payment_link_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


