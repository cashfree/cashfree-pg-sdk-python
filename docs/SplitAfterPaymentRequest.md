# SplitAfterPaymentRequest

Split After Payment Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**split** | [**List[SplitAfterPaymentRequestSplitInner]**](SplitAfterPaymentRequestSplitInner.md) | Specify the vendors order split details. | 
**disable_split** | **bool** | Specify if you want to end the split or continue creating further splits in future. | [optional] 

## Example

```python
from cashfree_pg.models.split_after_payment_request import SplitAfterPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SplitAfterPaymentRequest from a JSON string
split_after_payment_request_instance = SplitAfterPaymentRequest.from_json(json)
# print the JSON string representation of the object
print SplitAfterPaymentRequest.to_json()

# convert the object into a dict
split_after_payment_request_dict = split_after_payment_request_instance.to_dict()
# create an instance of SplitAfterPaymentRequest from a dict
split_after_payment_request_form_dict = split_after_payment_request.from_dict(split_after_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


