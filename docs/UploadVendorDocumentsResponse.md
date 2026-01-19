# UploadVendorDocumentsResponse

Upload Vendor Document

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
from cashfree_pg.models.upload_vendor_documents_response import UploadVendorDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadVendorDocumentsResponse from a JSON string
upload_vendor_documents_response_instance = UploadVendorDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print UploadVendorDocumentsResponse.to_json()

# convert the object into a dict
upload_vendor_documents_response_dict = upload_vendor_documents_response_instance.to_dict()
# create an instance of UploadVendorDocumentsResponse from a dict
upload_vendor_documents_response_form_dict = upload_vendor_documents_response.from_dict(upload_vendor_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


