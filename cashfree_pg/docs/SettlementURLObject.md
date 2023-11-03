# SettlementURLObject

Settlement URL object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.settlement_url_object import SettlementURLObject

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementURLObject from a JSON string
settlement_url_object_instance = SettlementURLObject.from_json(json)
# print the JSON string representation of the object
print SettlementURLObject.to_json()

# convert the object into a dict
settlement_url_object_dict = settlement_url_object_instance.to_dict()
# create an instance of SettlementURLObject from a dict
settlement_url_object_form_dict = settlement_url_object.from_dict(settlement_url_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


