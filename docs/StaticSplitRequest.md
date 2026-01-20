# StaticSplitRequest

Static Split Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Specify if the split is to be active or not. Possible values: true/false | 
**terminal_id** | **str** | For Subscription payments, the subscription reference ID is to be shared as the terminal ID. Incase for Payment Gateway terminal ID is non-mandatory. Mention as 0 if not applicable. | [optional] 
**terminal_reference_id** | **float** | You can share additional information using the reference ID. | [optional] 
**product_type** | **str** | Specify the product for which the split should be created. If you want split to be created for Payment Gateway pass value as \&quot;PG\&quot;. If you want split to be created for Subscription, pass value as \&quot;SBC\&quot;. Accepted values - \&quot;STATIC_QR\&quot;, \&quot;SBC\&quot;, \&quot;PG\&quot;, \&quot;EPOS\&quot;. | 
**scheme** | [**List[StaticSplitRequestSchemeInner]**](StaticSplitRequestSchemeInner.md) | Provide the split scheme details. | 

## Example

```python
from cashfree_pg.models.static_split_request import StaticSplitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaticSplitRequest from a JSON string
static_split_request_instance = StaticSplitRequest.from_json(json)
# print the JSON string representation of the object
print(StaticSplitRequest.to_json())

# convert the object into a dict
static_split_request_dict = static_split_request_instance.to_dict()
# create an instance of StaticSplitRequest from a dict
static_split_request_from_dict = StaticSplitRequest.from_dict(static_split_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


