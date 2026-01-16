# TransferDetailsTagsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** |  | [optional] 
**size** | **float** |  | [optional] 

## Example

```python
from cashfree_pg.models.transfer_details_tags_inner import TransferDetailsTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDetailsTagsInner from a JSON string
transfer_details_tags_inner_instance = TransferDetailsTagsInner.from_json(json)
# print the JSON string representation of the object
print TransferDetailsTagsInner.to_json()

# convert the object into a dict
transfer_details_tags_inner_dict = transfer_details_tags_inner_instance.to_dict()
# create an instance of TransferDetailsTagsInner from a dict
transfer_details_tags_inner_form_dict = transfer_details_tags_inner.from_dict(transfer_details_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


