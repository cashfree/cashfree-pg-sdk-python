# RefundURLObject

URL to get refunds for order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.refund_url_object import RefundURLObject

# TODO update the JSON string below
json = "{}"
# create an instance of RefundURLObject from a JSON string
refund_url_object_instance = RefundURLObject.from_json(json)
# print the JSON string representation of the object
print RefundURLObject.to_json()

# convert the object into a dict
refund_url_object_dict = refund_url_object_instance.to_dict()
# create an instance of RefundURLObject from a dict
refund_url_object_form_dict = refund_url_object.from_dict(refund_url_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


