# CustomerDetailsCardlessEMI

Details of the customer for whom eligibility is being checked.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_phone** | **str** | Phone Number of the customer | 

## Example

```python
from cashfree_pg.models.customer_details_cardless_emi import CustomerDetailsCardlessEMI

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerDetailsCardlessEMI from a JSON string
customer_details_cardless_emi_instance = CustomerDetailsCardlessEMI.from_json(json)
# print the JSON string representation of the object
print CustomerDetailsCardlessEMI.to_json()

# convert the object into a dict
customer_details_cardless_emi_dict = customer_details_cardless_emi_instance.to_dict()
# create an instance of CustomerDetailsCardlessEMI from a dict
customer_details_cardless_emi_form_dict = customer_details_cardless_emi.from_dict(customer_details_cardless_emi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


