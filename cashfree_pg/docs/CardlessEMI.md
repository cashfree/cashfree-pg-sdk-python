# CardlessEMI

Request body for cardless emi payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The channel for cardless EMI is always &#x60;link&#x60; | [optional] 
**provider** | **str** | One of [&#x60;flexmoney&#x60;, &#x60;zestmoney&#x60;, &#x60;hdfc&#x60;, &#x60;icici&#x60;, &#x60;cashe&#x60;, &#x60;idfc&#x60;, &#x60;kotak&#x60;] | [optional] 
**phone** | **str** | Customers phone number for this payment instrument. If the customer is not eligible you will receive a 400 error with type as &#39;invalid_request_error&#39; and code as &#39;invalid_request_error&#39; | [optional] 
**emi_tenure** | **int** | EMI tenure for the selected provider. This is mandatory when provider is one of [&#x60;hdfc&#x60;, &#x60;icici&#x60;, &#x60;cashe&#x60;, &#x60;idfc&#x60;, &#x60;kotak&#x60;] | [optional] 

## Example

```python
from cashfree_pg.models.cardless_emi import CardlessEMI

# TODO update the JSON string below
json = "{}"
# create an instance of CardlessEMI from a JSON string
cardless_emi_instance = CardlessEMI.from_json(json)
# print the JSON string representation of the object
print CardlessEMI.to_json()

# convert the object into a dict
cardless_emi_dict = cardless_emi_instance.to_dict()
# create an instance of CardlessEMI from a dict
cardless_emi_form_dict = cardless_emi.from_dict(cardless_emi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


