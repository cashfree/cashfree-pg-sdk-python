# UploadPnachImageResponse

Response of pnach image upload API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The payment_id against which the pnach image is uploaded. | [optional] 
**authorization_status** | **str** | Authorization status of the subscription. | [optional] 
**action** | **str** | Action performed on the file. | [optional] 
**payment_message** | **str** | Message of the API. | [optional] 

## Example

```python
from cashfree_pg.models.upload_pnach_image_response import UploadPnachImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPnachImageResponse from a JSON string
upload_pnach_image_response_instance = UploadPnachImageResponse.from_json(json)
# print the JSON string representation of the object
print UploadPnachImageResponse.to_json()

# convert the object into a dict
upload_pnach_image_response_dict = upload_pnach_image_response_instance.to_dict()
# create an instance of UploadPnachImageResponse from a dict
upload_pnach_image_response_form_dict = upload_pnach_image_response.from_dict(upload_pnach_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


