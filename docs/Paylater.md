# Paylater

Paylater payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The channel for cardless EMI is always &#x60;link&#x60; | [optional] 
**provider** | **str** | One of [\&quot;kotak\&quot;, \&quot;flexipay\&quot;, \&quot;zestmoney\&quot;, \&quot;lazypay\&quot;, \&quot;olapostpaid\&quot;,\&quot;simpl\&quot;, \&quot;freechargepaylater\&quot;]. Please note that Flexipay is offered by HDFC bank | [optional] 
**phone** | **str** | Customers phone number for this payment instrument. If the customer is not eligible you will receive a 400 error with type as &#39;invalid_request_error&#39; and code as &#39;invalid_request_error&#39; | [optional] 

## Example

```python
from cashfree_pg.models.paylater import Paylater

# TODO update the JSON string below
json = "{}"
# create an instance of Paylater from a JSON string
paylater_instance = Paylater.from_json(json)
# print the JSON string representation of the object
print Paylater.to_json()

# convert the object into a dict
paylater_dict = paylater_instance.to_dict()
# create an instance of Paylater from a dict
paylater_form_dict = paylater.from_dict(paylater_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


