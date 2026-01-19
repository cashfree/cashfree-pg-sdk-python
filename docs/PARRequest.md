# PARRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Card number, between 15 and 19 digits. | 
**card_cvv** | **str** | Card CVV, 3 or 4 digits. | 
**card_expiry_mm** | **str** | Two-digit card expiry month (01-12). | 
**card_expiry_yy** | **str** | Two-digit card expiry year. | 
**card_type** | **str** | Card type; allowed value is PLAIN_CARD. | 

## Example

```python
from cashfree_pg.models.par_request import PARRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PARRequest from a JSON string
par_request_instance = PARRequest.from_json(json)
# print the JSON string representation of the object
print PARRequest.to_json()

# convert the object into a dict
par_request_dict = par_request_instance.to_dict()
# create an instance of PARRequest from a dict
par_request_form_dict = par_request.from_dict(par_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


