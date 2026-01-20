# VendorEntityRelatedDocsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**doc_value** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**remarks** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.vendor_entity_related_docs_inner import VendorEntityRelatedDocsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorEntityRelatedDocsInner from a JSON string
vendor_entity_related_docs_inner_instance = VendorEntityRelatedDocsInner.from_json(json)
# print the JSON string representation of the object
print(VendorEntityRelatedDocsInner.to_json())

# convert the object into a dict
vendor_entity_related_docs_inner_dict = vendor_entity_related_docs_inner_instance.to_dict()
# create an instance of VendorEntityRelatedDocsInner from a dict
vendor_entity_related_docs_inner_from_dict = VendorEntityRelatedDocsInner.from_dict(vendor_entity_related_docs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


