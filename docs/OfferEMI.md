# OfferEMI

EMI offer object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emi** | [**EMIOffer**](EMIOffer.md) |  | 

## Example

```python
from cashfree_pg.models.offer_emi import OfferEMI

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEMI from a JSON string
offer_emi_instance = OfferEMI.from_json(json)
# print the JSON string representation of the object
print OfferEMI.to_json()

# convert the object into a dict
offer_emi_dict = offer_emi_instance.to_dict()
# create an instance of OfferEMI from a dict
offer_emi_form_dict = offer_emi.from_dict(offer_emi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


