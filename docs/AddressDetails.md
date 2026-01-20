# AddressDetails

Address associated with the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full Name of the customer associated with the address. | [optional] 
**address_line_one** | **str** | First line of the address. | [optional] 
**address_line_two** | **str** | Second line of the address. | [optional] 
**country** | **str** | Country Name. | [optional] 
**country_code** | **str** | Country Code. | [optional] 
**state** | **str** | State Name. | [optional] 
**state_code** | **str** | State Code. | [optional] 
**city** | **str** | City Name. | [optional] 
**pin_code** | **str** | Pin Code/Zip Code. | [optional] 
**phone** | **str** | Customer Phone Number. | [optional] 
**email** | **str** | Cutomer Email Address. | [optional] 

## Example

```python
from cashfree_pg.models.address_details import AddressDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AddressDetails from a JSON string
address_details_instance = AddressDetails.from_json(json)
# print the JSON string representation of the object
print(AddressDetails.to_json())

# convert the object into a dict
address_details_dict = address_details_instance.to_dict()
# create an instance of AddressDetails from a dict
address_details_from_dict = AddressDetails.from_dict(address_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


