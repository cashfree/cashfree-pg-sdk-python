# CardEMI

Payment method for card emi

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The channel for card payments will always be \&quot;link\&quot; | 
**card_number** | **str** | Customer card number. | 
**card_holder_name** | **str** | Customer name mentioned on the card. | [optional] 
**card_expiry_mm** | **str** | Card expiry month. | 
**card_expiry_yy** | **str** | Card expiry year. | 
**card_cvv** | **str** | CVV mentioned on the card. | 
**card_alias** | **str** | Card alias as returned by Cashfree Vault API | [optional] 
**card_bank_name** | **str** | Card bank name, required for EMI payments. This is the bank user has selected for EMI. One of [\&quot;hdfc, \&quot;kotak\&quot;, \&quot;icici\&quot;, \&quot;rbl\&quot;, \&quot;bob\&quot;, \&quot;standard chartered\&quot;, \&quot;axis\&quot;, \&quot;au\&quot;, \&quot;yes\&quot;, \&quot;sbi\&quot;, \&quot;fed\&quot;, \&quot;hsbc\&quot;, \&quot;citi\&quot;, \&quot;amex\&quot;] | 
**emi_tenure** | **int** | EMI tenure selected by the user | 

## Example

```python
from cashfree_pg.models.card_emi import CardEMI

# TODO update the JSON string below
json = "{}"
# create an instance of CardEMI from a JSON string
card_emi_instance = CardEMI.from_json(json)
# print the JSON string representation of the object
print CardEMI.to_json()

# convert the object into a dict
card_emi_dict = card_emi_instance.to_dict()
# create an instance of CardEMI from a dict
card_emi_form_dict = card_emi.from_dict(card_emi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


