# OfferNBNetbanking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_name** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.offer_nb_netbanking import OfferNBNetbanking

# TODO update the JSON string below
json = "{}"
# create an instance of OfferNBNetbanking from a JSON string
offer_nb_netbanking_instance = OfferNBNetbanking.from_json(json)
# print the JSON string representation of the object
print OfferNBNetbanking.to_json()

# convert the object into a dict
offer_nb_netbanking_dict = offer_nb_netbanking_instance.to_dict()
# create an instance of OfferNBNetbanking from a dict
offer_nb_netbanking_form_dict = offer_nb_netbanking.from_dict(offer_nb_netbanking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


