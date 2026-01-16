# CreateCustomerRequest

Request body to create a customer at cashfree

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_phone** | **str** | Customer Phone Number | 
**customer_email** | **str** | Customer Email | [optional] 
**customer_name** | **str** | Customer Name | [optional] 

## Example

```python
from cashfree_pg.models.create_customer_request import CreateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerRequest from a JSON string
create_customer_request_instance = CreateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print CreateCustomerRequest.to_json()

# convert the object into a dict
create_customer_request_dict = create_customer_request_instance.to_dict()
# create an instance of CreateCustomerRequest from a dict
create_customer_request_form_dict = create_customer_request.from_dict(create_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


