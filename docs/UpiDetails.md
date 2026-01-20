# UpiDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpa** | **str** |  | [optional] 
**account_holder** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.upi_details import UpiDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpiDetails from a JSON string
upi_details_instance = UpiDetails.from_json(json)
# print the JSON string representation of the object
print(UpiDetails.to_json())

# convert the object into a dict
upi_details_dict = upi_details_instance.to_dict()
# create an instance of UpiDetails from a dict
upi_details_from_dict = UpiDetails.from_dict(upi_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


