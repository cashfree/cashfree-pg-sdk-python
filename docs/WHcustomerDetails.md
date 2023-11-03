# WHcustomerDetails

customer details object in webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_phone** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.w_hcustomer_details import WHcustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WHcustomerDetails from a JSON string
w_hcustomer_details_instance = WHcustomerDetails.from_json(json)
# print the JSON string representation of the object
print WHcustomerDetails.to_json()

# convert the object into a dict
w_hcustomer_details_dict = w_hcustomer_details_instance.to_dict()
# create an instance of WHcustomerDetails from a dict
w_hcustomer_details_form_dict = w_hcustomer_details.from_dict(w_hcustomer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


