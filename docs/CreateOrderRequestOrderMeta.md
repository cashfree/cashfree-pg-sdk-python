# CreateOrderRequestOrderMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | The URL to which user will be redirected to after the payment on bank OTP page. Maximum length: 250. The return_url must contain placeholder {order_id}. When redirecting the customer back to the return url from the bank’s OTP page, Cashfree will replace this placeholder with the actual value for that order. | [optional] 
**notify_url** | **str** | Notification URL for server-server communication. Useful when user&#39;s connection drops while re-directing. NotifyUrl should be an https URL. Maximum length: 250. | [optional] 
**payment_methods** | **object** | Allowed payment modes for this order. Pass comma-separated values among following options - \&quot;cc\&quot;, \&quot;dc\&quot;, \&quot;ccc\&quot;, \&quot;ppc\&quot;,\&quot;nb\&quot;,\&quot;upi\&quot;,\&quot;paypal\&quot;,\&quot;app\&quot;,\&quot;paylater\&quot;,\&quot;cardlessemi\&quot;,\&quot;dcemi\&quot;,\&quot;ccemi\&quot;,\&quot;banktransfer\&quot;. Leave it blank to show all available payment methods | [optional] 

## Example

```python
from cashfree_pg.models.create_order_request_order_meta import CreateOrderRequestOrderMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequestOrderMeta from a JSON string
create_order_request_order_meta_instance = CreateOrderRequestOrderMeta.from_json(json)
# print the JSON string representation of the object
print CreateOrderRequestOrderMeta.to_json()

# convert the object into a dict
create_order_request_order_meta_dict = create_order_request_order_meta_instance.to_dict()
# create an instance of CreateOrderRequestOrderMeta from a dict
create_order_request_order_meta_form_dict = create_order_request_order_meta.from_dict(create_order_request_order_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


