# DemapSoundboxVpaRequest

Request body to demap soundbox vpa

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_terminal_id** | **str** | cashfree terminal id. | 
**device_serial_no** | **str** | Device Serial No of soundbox that need to demap. | 

## Example

```python
from cashfree_pg.models.demap_soundbox_vpa_request import DemapSoundboxVpaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DemapSoundboxVpaRequest from a JSON string
demap_soundbox_vpa_request_instance = DemapSoundboxVpaRequest.from_json(json)
# print the JSON string representation of the object
print DemapSoundboxVpaRequest.to_json()

# convert the object into a dict
demap_soundbox_vpa_request_dict = demap_soundbox_vpa_request_instance.to_dict()
# create an instance of DemapSoundboxVpaRequest from a dict
demap_soundbox_vpa_request_form_dict = demap_soundbox_vpa_request.from_dict(demap_soundbox_vpa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


