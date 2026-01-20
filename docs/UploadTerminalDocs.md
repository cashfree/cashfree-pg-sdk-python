# UploadTerminalDocs

Request body to upload terminal documents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_type** | **str** | Mention the document type you are uploading. Possible values - ADDRESSPROOF, PHOTOGRAPH. | 
**doc_value** | **str** | Enter the display name of the uploaded file. | 
**file** | **str** | Select the document that should be uploaded or provide the path of that file. You cannot upload a file that is more than 2MB in size. | 

## Example

```python
from cashfree_pg.models.upload_terminal_docs import UploadTerminalDocs

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTerminalDocs from a JSON string
upload_terminal_docs_instance = UploadTerminalDocs.from_json(json)
# print the JSON string representation of the object
print(UploadTerminalDocs.to_json())

# convert the object into a dict
upload_terminal_docs_dict = upload_terminal_docs_instance.to_dict()
# create an instance of UploadTerminalDocs from a dict
upload_terminal_docs_from_dict = UploadTerminalDocs.from_dict(upload_terminal_docs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


