# VendorDocumentDownloadResponse

Download Vendor Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.vendor_document_download_response import VendorDocumentDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VendorDocumentDownloadResponse from a JSON string
vendor_document_download_response_instance = VendorDocumentDownloadResponse.from_json(json)
# print the JSON string representation of the object
print VendorDocumentDownloadResponse.to_json()

# convert the object into a dict
vendor_document_download_response_dict = vendor_document_download_response_instance.to_dict()
# create an instance of VendorDocumentDownloadResponse from a dict
vendor_document_download_response_form_dict = vendor_document_download_response.from_dict(vendor_document_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


