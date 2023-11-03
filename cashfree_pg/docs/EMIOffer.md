# EMIOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of emi offer. Possible values are &#x60;credit_card_emi&#x60;, &#x60;debit_card_emi&#x60;, &#x60;cardless_emi&#x60; | 
**issuer** | **str** | Bank Name | 
**tenures** | **List[int]** |  | 

## Example

```python
from cashfree_pg.models.emi_offer import EMIOffer

# TODO update the JSON string below
json = "{}"
# create an instance of EMIOffer from a JSON string
emi_offer_instance = EMIOffer.from_json(json)
# print the JSON string representation of the object
print EMIOffer.to_json()

# convert the object into a dict
emi_offer_dict = emi_offer_instance.to_dict()
# create an instance of EMIOffer from a dict
emi_offer_form_dict = emi_offer.from_dict(emi_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


