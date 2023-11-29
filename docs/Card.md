# Card

Card Payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The channel for card payments can be \&quot;link\&quot; or \&quot;post\&quot;. Post is used for seamless OTP payments where merchant captures OTP on their own page. | 
**card_number** | **str** | Customer card number for plain card transactions. Token pan number for tokenized card transactions. | [optional] 
**card_holder_name** | **str** | Customer name mentioned on the card. | [optional] 
**card_expiry_mm** | **str** | Card expiry month for plain card transactions. Token expiry month for tokenized card transactions. | [optional] 
**card_expiry_yy** | **str** | Card expiry year for plain card transactions. Token expiry year for tokenized card transactions. | [optional] 
**card_cvv** | **str** | CVV mentioned on the card. | [optional] 
**instrument_id** | **str** | instrument id of saved card. Required only to make payment using saved instrument. | [optional] 
**cryptogram** | **str** | cryptogram received from card network. Required only for tokenized card transactions. | [optional] 
**token_requestor_id** | **str** | TRID issued by card networks. Required only for tokenized card transactions. | [optional] 
**token_type** | **str** |  | [optional] 
**card_display** | **str** | last 4 digits of original card number. Required only for tokenized card transactions. | [optional] 
**card_alias** | **str** | Card alias as returned by Cashfree Vault API. | [optional] 
**card_bank_name** | **str** | One of [\&quot;Kotak\&quot;, \&quot;ICICI\&quot;, \&quot;RBL\&quot;, \&quot;BOB\&quot;, \&quot;Standard Chartered\&quot;]. Card bank name, required for EMI payments. This is the bank user has selected for EMI | [optional] 
**emi_tenure** | **int** | EMI tenure selected by the user | [optional] 

## Example

```python
from cashfree_pg.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print Card.to_json()

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_form_dict = card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


