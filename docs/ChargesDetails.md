# ChargesDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_charges** | **float** |  | [optional] 
**service_tax** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**billed_to** | **str** |  | [optional] 
**is_postpaid** | **bool** |  | [optional] 

## Example

```python
from cashfree_pg.models.charges_details import ChargesDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ChargesDetails from a JSON string
charges_details_instance = ChargesDetails.from_json(json)
# print the JSON string representation of the object
print ChargesDetails.to_json()

# convert the object into a dict
charges_details_dict = charges_details_instance.to_dict()
# create an instance of ChargesDetails from a dict
charges_details_form_dict = charges_details.from_dict(charges_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


