# StaticQrResponseEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cf_terminal_id** | **int** | cashfree terminal id | [optional] 
**vpa** | **str** | Virtual Address | [optional] 
**status** | **str** | Status of vpa | [optional] 
**qr_code** | **str** | qrcode | [optional] 

## Example

```python
from cashfree_pg.models.static_qr_response_entity import StaticQrResponseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of StaticQrResponseEntity from a JSON string
static_qr_response_entity_instance = StaticQrResponseEntity.from_json(json)
# print the JSON string representation of the object
print(StaticQrResponseEntity.to_json())

# convert the object into a dict
static_qr_response_entity_dict = static_qr_response_entity_instance.to_dict()
# create an instance of StaticQrResponseEntity from a dict
static_qr_response_entity_from_dict = StaticQrResponseEntity.from_dict(static_qr_response_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


