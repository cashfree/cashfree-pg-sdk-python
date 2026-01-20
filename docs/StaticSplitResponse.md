# StaticSplitResponse

Static Split Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**terminal_reference_id** | **float** |  | [optional] 
**product_type** | **str** |  | [optional] 
**scheme** | [**List[StaticSplitResponseSchemeInner]**](StaticSplitResponseSchemeInner.md) |  | [optional] 
**added_on** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.static_split_response import StaticSplitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSplitResponse from a JSON string
static_split_response_instance = StaticSplitResponse.from_json(json)
# print the JSON string representation of the object
print(StaticSplitResponse.to_json())

# convert the object into a dict
static_split_response_dict = static_split_response_instance.to_dict()
# create an instance of StaticSplitResponse from a dict
static_split_response_from_dict = StaticSplitResponse.from_dict(static_split_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


