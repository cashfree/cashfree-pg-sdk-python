# UpdateSoundboxVpaRequest

Request body to update soundbox vpa

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpa** | **str** | Terminal Vpa,for which we need to update details. | 
**cf_terminal_id** | **str** | cashfree terminal id. | 
**merchant_name** | **str** | Merchant Name that need to updated on soundbox | [optional] 
**language** | **str** | language of soundbox,currently English, Hindi, Tamil | [optional] 

## Example

```python
from cashfree_pg.models.update_soundbox_vpa_request import UpdateSoundboxVpaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSoundboxVpaRequest from a JSON string
update_soundbox_vpa_request_instance = UpdateSoundboxVpaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSoundboxVpaRequest.to_json())

# convert the object into a dict
update_soundbox_vpa_request_dict = update_soundbox_vpa_request_instance.to_dict()
# create an instance of UpdateSoundboxVpaRequest from a dict
update_soundbox_vpa_request_from_dict = UpdateSoundboxVpaRequest.from_dict(update_soundbox_vpa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


