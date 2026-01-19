# UPIAuthorizeDetails

object when you are using preauth in UPI in order pay

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approve_by** | **str** | Time by which this authorization should be approved by the customer. | [optional] 
**start_time** | **str** | This is the time when the UPI one time mandate will start | [optional] 
**end_time** | **str** | This is the time when the UPI mandate will be over. If the mandate has not been executed by this time, the funds will be returned back to the customer after this time. | [optional] 

## Example

```python
from cashfree_pg.models.upi_authorize_details import UPIAuthorizeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UPIAuthorizeDetails from a JSON string
upi_authorize_details_instance = UPIAuthorizeDetails.from_json(json)
# print the JSON string representation of the object
print UPIAuthorizeDetails.to_json()

# convert the object into a dict
upi_authorize_details_dict = upi_authorize_details_instance.to_dict()
# create an instance of UPIAuthorizeDetails from a dict
upi_authorize_details_form_dict = upi_authorize_details.from_dict(upi_authorize_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


