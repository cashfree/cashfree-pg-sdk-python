# SplitAfterPaymentRequestSplitInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** | Specify the merchant vendor ID to split the payment. | [optional] 
**amount** | **float** | Specify the amount to be split to the vendor. | [optional] 
**percentage** | **float** | Specify the percentage of amount to be split. | [optional] 
**tags** | **Dict[str, str]** | Custom Tags in thr form of {\&quot;key\&quot;:\&quot;value\&quot;} which can be passed for an order. A maximum of 10 tags can be added | [optional] 

## Example

```python
from cashfree_pg.models.split_after_payment_request_split_inner import SplitAfterPaymentRequestSplitInner

# TODO update the JSON string below
json = "{}"
# create an instance of SplitAfterPaymentRequestSplitInner from a JSON string
split_after_payment_request_split_inner_instance = SplitAfterPaymentRequestSplitInner.from_json(json)
# print the JSON string representation of the object
print SplitAfterPaymentRequestSplitInner.to_json()

# convert the object into a dict
split_after_payment_request_split_inner_dict = split_after_payment_request_split_inner_instance.to_dict()
# create an instance of SplitAfterPaymentRequestSplitInner from a dict
split_after_payment_request_split_inner_form_dict = split_after_payment_request_split_inner.from_dict(split_after_payment_request_split_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


