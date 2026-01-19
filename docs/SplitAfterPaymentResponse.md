# SplitAfterPaymentResponse

Split After Payment Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.split_after_payment_response import SplitAfterPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SplitAfterPaymentResponse from a JSON string
split_after_payment_response_instance = SplitAfterPaymentResponse.from_json(json)
# print the JSON string representation of the object
print SplitAfterPaymentResponse.to_json()

# convert the object into a dict
split_after_payment_response_dict = split_after_payment_response_instance.to_dict()
# create an instance of SplitAfterPaymentResponse from a dict
split_after_payment_response_form_dict = split_after_payment_response.from_dict(split_after_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


