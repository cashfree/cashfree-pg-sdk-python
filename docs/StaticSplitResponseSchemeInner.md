# StaticSplitResponseSchemeInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_vendor_id** | **str** |  | [optional] 
**percentage** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.static_split_response_scheme_inner import StaticSplitResponseSchemeInner

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSplitResponseSchemeInner from a JSON string
static_split_response_scheme_inner_instance = StaticSplitResponseSchemeInner.from_json(json)
# print the JSON string representation of the object
print StaticSplitResponseSchemeInner.to_json()

# convert the object into a dict
static_split_response_scheme_inner_dict = static_split_response_scheme_inner_instance.to_dict()
# create an instance of StaticSplitResponseSchemeInner from a dict
static_split_response_scheme_inner_form_dict = static_split_response_scheme_inner.from_dict(static_split_response_scheme_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


