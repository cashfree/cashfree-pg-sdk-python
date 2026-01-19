# OnboardSoundboxVpaRequest

Request body to onboard soundbox vpa

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpa** | **str** | Terminal Vpa ,that need to onboard on soundbox | 
**cf_terminal_id** | **str** | cashfree terminal id. | 
**device_serial_no** | **str** | Device Serial No of soundbox | 
**merchant_name** | **str** | Merchant Name that need to onboard on soundbox | [optional] 
**language** | **str** | language of soundbox,currently English, Hindi, Tamil | [optional] 

## Example

```python
from cashfree_pg.models.onboard_soundbox_vpa_request import OnboardSoundboxVpaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardSoundboxVpaRequest from a JSON string
onboard_soundbox_vpa_request_instance = OnboardSoundboxVpaRequest.from_json(json)
# print the JSON string representation of the object
print OnboardSoundboxVpaRequest.to_json()

# convert the object into a dict
onboard_soundbox_vpa_request_dict = onboard_soundbox_vpa_request_instance.to_dict()
# create an instance of OnboardSoundboxVpaRequest from a dict
onboard_soundbox_vpa_request_form_dict = onboard_soundbox_vpa_request.from_dict(onboard_soundbox_vpa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


