# ExtendedCustomerDetails

Recent Customer details associated with the order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A unique identifier for the customer. Use alphanumeric values only. | [optional] 
**customer_email** | **str** | Customer email address. | [optional] 
**customer_phone** | **str** | Customer phone number. | [optional] 
**customer_name** | **str** | Name of the customer. | [optional] 
**customer_uid** | **str** | Customer identifier at Cashfree. You will get this when you create/get customer | [optional] 

## Example

```python
from cashfree_pg.models.extended_customer_details import ExtendedCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedCustomerDetails from a JSON string
extended_customer_details_instance = ExtendedCustomerDetails.from_json(json)
# print the JSON string representation of the object
print ExtendedCustomerDetails.to_json()

# convert the object into a dict
extended_customer_details_dict = extended_customer_details_instance.to_dict()
# create an instance of ExtendedCustomerDetails from a dict
extended_customer_details_form_dict = extended_customer_details.from_dict(extended_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


