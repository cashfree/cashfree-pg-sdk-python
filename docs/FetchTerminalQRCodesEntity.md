# FetchTerminalQRCodesEntity

Fetch Static QR Codes using terminal ID or phone number

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank** | **str** | Name of the bank that is linked to the Static QR. | [optional] 
**qr_code** | **str** | Base-64 Encoded QR Code URL | [optional] 
**qr_code_url** | **str** | URL of the qr Code. | [optional] 
**status** | **str** | Status of the static QR. | [optional] 

## Example

```python
from cashfree_pg.models.fetch_terminal_qr_codes_entity import FetchTerminalQRCodesEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FetchTerminalQRCodesEntity from a JSON string
fetch_terminal_qr_codes_entity_instance = FetchTerminalQRCodesEntity.from_json(json)
# print the JSON string representation of the object
print FetchTerminalQRCodesEntity.to_json()

# convert the object into a dict
fetch_terminal_qr_codes_entity_dict = fetch_terminal_qr_codes_entity_instance.to_dict()
# create an instance of FetchTerminalQRCodesEntity from a dict
fetch_terminal_qr_codes_entity_form_dict = fetch_terminal_qr_codes_entity.from_dict(fetch_terminal_qr_codes_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


