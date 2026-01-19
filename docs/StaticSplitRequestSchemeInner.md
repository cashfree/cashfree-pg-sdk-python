# StaticSplitRequestSchemeInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_vendor_id** | **str** | Specify the merchant vendor ID to create the split scheme for the payment. | [optional] 
**percentage** | **str** | Specify the percentage of amount to be split. | [optional] 

## Example

```python
from cashfree_pg.models.static_split_request_scheme_inner import StaticSplitRequestSchemeInner

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSplitRequestSchemeInner from a JSON string
static_split_request_scheme_inner_instance = StaticSplitRequestSchemeInner.from_json(json)
# print the JSON string representation of the object
print StaticSplitRequestSchemeInner.to_json()

# convert the object into a dict
static_split_request_scheme_inner_dict = static_split_request_scheme_inner_instance.to_dict()
# create an instance of StaticSplitRequestSchemeInner from a dict
static_split_request_scheme_inner_form_dict = static_split_request_scheme_inner.from_dict(static_split_request_scheme_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


