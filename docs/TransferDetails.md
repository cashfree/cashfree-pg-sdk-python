# TransferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**transfer_from** | **str** |  | [optional] 
**transfer_type** | **str** |  | [optional] 
**transfer_amount** | **float** |  | [optional] 
**remark** | **str** |  | [optional] 
**tags** | [**List[TransferDetailsTagsInner]**](TransferDetailsTagsInner.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.transfer_details import TransferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDetails from a JSON string
transfer_details_instance = TransferDetails.from_json(json)
# print the JSON string representation of the object
print(TransferDetails.to_json())

# convert the object into a dict
transfer_details_dict = transfer_details_instance.to_dict()
# create an instance of TransferDetails from a dict
transfer_details_from_dict = TransferDetails.from_dict(transfer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


