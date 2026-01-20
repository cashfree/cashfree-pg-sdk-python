# Banktransfer

Banktransfer payment method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The channel for cardless EMI is always &#x60;link&#x60; | [optional] 

## Example

```python
from cashfree_pg.models.banktransfer import Banktransfer

# TODO update the JSON string below
json = "{}"
# create an instance of Banktransfer from a JSON string
banktransfer_instance = Banktransfer.from_json(json)
# print the JSON string representation of the object
print(Banktransfer.to_json())

# convert the object into a dict
banktransfer_dict = banktransfer_instance.to_dict()
# create an instance of Banktransfer from a dict
banktransfer_from_dict = Banktransfer.from_dict(banktransfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


