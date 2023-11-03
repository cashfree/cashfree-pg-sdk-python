# WalletOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.wallet_offer import WalletOffer

# TODO update the JSON string below
json = "{}"
# create an instance of WalletOffer from a JSON string
wallet_offer_instance = WalletOffer.from_json(json)
# print the JSON string representation of the object
print WalletOffer.to_json()

# convert the object into a dict
wallet_offer_dict = wallet_offer_instance.to_dict()
# create an instance of WalletOffer from a dict
wallet_offer_form_dict = wallet_offer.from_dict(wallet_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


