# OrderMeta

Optional meta details to control how the customer pays and how payment journey completes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | The URL to which user will be redirected to after the payment on bank OTP page. Maximum length: 250. We suggest to keep context of order_id in your return_url so that you can identify the order when customer lands on your page. Example of return_url format could be https://example.com/return?order_id&#x3D;myOrderId | [optional] 
**notify_url** | **str** | Notification URL for server-server communication. Useful when user&#39;s connection drops while re-directing. NotifyUrl should be an https URL. Maximum length: 250. | [optional] 
**payment_methods** | **object** | Allowed payment modes for this order. Pass comma-separated values among following options - \&quot;cc\&quot;, \&quot;dc\&quot;, \&quot;ccc\&quot;, \&quot;ppc\&quot;,\&quot;nb\&quot;,\&quot;upi\&quot;,\&quot;paypal\&quot;,\&quot;app\&quot;,\&quot;paylater\&quot;,\&quot;cardlessemi\&quot;,\&quot;dcemi\&quot;,\&quot;ccemi\&quot;,\&quot;banktransfer\&quot;. Leave it blank to show all available payment methods | [optional] 

## Example

```python
from cashfree_pg.models.order_meta import OrderMeta

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMeta from a JSON string
order_meta_instance = OrderMeta.from_json(json)
# print the JSON string representation of the object
print OrderMeta.to_json()

# convert the object into a dict
order_meta_dict = order_meta_instance.to_dict()
# create an instance of OrderMeta from a dict
order_meta_form_dict = order_meta.from_dict(order_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


