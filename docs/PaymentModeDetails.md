# PaymentModeDetails

payment mode eligiblity object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nick** | **str** |  | [optional] 
**display** | **str** |  | [optional] 
**eligibility** | **bool** |  | [optional] 
**code** | **float** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_mode_details import PaymentModeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentModeDetails from a JSON string
payment_mode_details_instance = PaymentModeDetails.from_json(json)
# print the JSON string representation of the object
print PaymentModeDetails.to_json()

# convert the object into a dict
payment_mode_details_dict = payment_mode_details_instance.to_dict()
# create an instance of PaymentModeDetails from a dict
payment_mode_details_form_dict = payment_mode_details.from_dict(payment_mode_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


