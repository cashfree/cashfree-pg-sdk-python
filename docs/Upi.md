# Upi

UPI collect payment method object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Specify the channel through which the payment must be processed. Can be one of [\&quot;link\&quot;, \&quot;collect\&quot;, \&quot;qrcode\&quot;] | 
**upi_id** | **str** | Customer UPI VPA to process payment.  ### Important This is a required parameter for channel &#x3D; &#x60;collect&#x60;  | [optional] 
**upi_redirect_url** | **bool** | use this if you want cashfree to show a loader. Sample response below. It is only supported for collect &#x60;action:collect&#x60; will be returned with &#x60;data.url&#x60; having the link for redirection  | [optional] 
**upi_expiry_minutes** | **float** | The UPI request will be valid for this expiry minutes. This parameter is only applicable for a UPI collect payment. The default value is 5 minutes. You should keep the minimum as 5 minutes, and maximum as 15 minutes | [optional] 
**authorize_only** | **bool** | For one time mandate on UPI. Set this as authorize_only &#x3D; true. Please note that you can only use the \&quot;collect\&quot; channel if you are sending a one time mandate request | [optional] 
**authorization** | [**UPIAuthorizeDetails**](UPIAuthorizeDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.upi import Upi

# TODO update the JSON string below
json = "{}"
# create an instance of Upi from a JSON string
upi_instance = Upi.from_json(json)
# print the JSON string representation of the object
print Upi.to_json()

# convert the object into a dict
upi_dict = upi_instance.to_dict()
# create an instance of Upi from a dict
upi_form_dict = upi.from_dict(upi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


