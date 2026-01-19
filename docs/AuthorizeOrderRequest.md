# AuthorizeOrderRequest

Request to capture or void transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Type of authorization to run. Can be one of &#39;CAPTURE&#39; , &#39;VOID&#39; | [optional] 
**amount** | **float** | The amount if you are running a &#39;CAPTURE&#39; | [optional] 

## Example

```python
from cashfree_pg.models.authorize_order_request import AuthorizeOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeOrderRequest from a JSON string
authorize_order_request_instance = AuthorizeOrderRequest.from_json(json)
# print the JSON string representation of the object
print AuthorizeOrderRequest.to_json()

# convert the object into a dict
authorize_order_request_dict = authorize_order_request_instance.to_dict()
# create an instance of AuthorizeOrderRequest from a dict
authorize_order_request_form_dict = authorize_order_request.from_dict(authorize_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


