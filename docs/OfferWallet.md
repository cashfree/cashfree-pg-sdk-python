# OfferWallet

Offer object for wallet payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**WalletOffer**](WalletOffer.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.offer_wallet import OfferWallet

# TODO update the JSON string below
json = "{}"
# create an instance of OfferWallet from a JSON string
offer_wallet_instance = OfferWallet.from_json(json)
# print the JSON string representation of the object
print OfferWallet.to_json()

# convert the object into a dict
offer_wallet_dict = offer_wallet_instance.to_dict()
# create an instance of OfferWallet from a dict
offer_wallet_form_dict = offer_wallet.from_dict(offer_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


