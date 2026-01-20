# LinkCustomerDetailsEntity

Payment link customer entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_phone** | **str** | Customer phone number | 
**customer_email** | **str** | Customer email address | [optional] 
**customer_name** | **str** | Customer name | [optional] 
**customer_bank_account_number** | **str** | Customer Bank Account Number | [optional] 
**customer_bank_ifsc** | **str** | Customer Bank Ifsc | [optional] 
**customer_bank_code** | **int** | Customer Bank Code | [optional] 

## Example

```python
from cashfree_pg.models.link_customer_details_entity import LinkCustomerDetailsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LinkCustomerDetailsEntity from a JSON string
link_customer_details_entity_instance = LinkCustomerDetailsEntity.from_json(json)
# print the JSON string representation of the object
print(LinkCustomerDetailsEntity.to_json())

# convert the object into a dict
link_customer_details_entity_dict = link_customer_details_entity_instance.to_dict()
# create an instance of LinkCustomerDetailsEntity from a dict
link_customer_details_entity_from_dict = LinkCustomerDetailsEntity.from_dict(link_customer_details_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


