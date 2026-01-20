# UploadTerminalDocsEntity

Upload the terminal documents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_terminal_id** | **int** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**doc_value** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.upload_terminal_docs_entity import UploadTerminalDocsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTerminalDocsEntity from a JSON string
upload_terminal_docs_entity_instance = UploadTerminalDocsEntity.from_json(json)
# print the JSON string representation of the object
print(UploadTerminalDocsEntity.to_json())

# convert the object into a dict
upload_terminal_docs_entity_dict = upload_terminal_docs_entity_instance.to_dict()
# create an instance of UploadTerminalDocsEntity from a dict
upload_terminal_docs_entity_from_dict = UploadTerminalDocsEntity.from_dict(upload_terminal_docs_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


