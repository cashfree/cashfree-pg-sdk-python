# SoundboxVpaEntity

soundbox response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpa** | **str** |  | [optional] 
**cf_terminal_id** | **str** |  | [optional] 
**device_serial_no** | **str** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.soundbox_vpa_entity import SoundboxVpaEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SoundboxVpaEntity from a JSON string
soundbox_vpa_entity_instance = SoundboxVpaEntity.from_json(json)
# print the JSON string representation of the object
print(SoundboxVpaEntity.to_json())

# convert the object into a dict
soundbox_vpa_entity_dict = soundbox_vpa_entity_instance.to_dict()
# create an instance of SoundboxVpaEntity from a dict
soundbox_vpa_entity_from_dict = SoundboxVpaEntity.from_dict(soundbox_vpa_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


