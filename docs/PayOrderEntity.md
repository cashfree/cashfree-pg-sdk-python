# PayOrderEntity

Order Pay response once you create a transaction for that order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_amount** | **float** | total amount payable | [optional] 
**cf_payment_id** | **int** | Payment identifier created by Cashfree | [optional] 
**payment_method** | **str** | One of [\&quot;upi\&quot;, \&quot;netbanking\&quot;, \&quot;card\&quot;, \&quot;app\&quot;, \&quot;cardless_emi\&quot;, \&quot;paylater\&quot;, \&quot;banktransfer\&quot;]  | [optional] 
**channel** | **str** | One of [\&quot;link\&quot;, \&quot;collect\&quot;, \&quot;qrcode\&quot;]. In an older version we used to support different channels like &#39;gpay&#39;, &#39;phonepe&#39; etc. However, we now support only the following channels - link, collect and qrcode. To process payments using gpay, you will have to provide channel as &#39;link&#39; and provider as &#39;gpay&#39; | [optional] 
**action** | **str** | One of [\&quot;link\&quot;, \&quot;custom\&quot;, \&quot;form\&quot;] | [optional] 
**data** | [**OrderPayData**](OrderPayData.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.pay_order_entity import PayOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayOrderEntity from a JSON string
pay_order_entity_instance = PayOrderEntity.from_json(json)
# print the JSON string representation of the object
print PayOrderEntity.to_json()

# convert the object into a dict
pay_order_entity_dict = pay_order_entity_instance.to_dict()
# create an instance of PayOrderEntity from a dict
pay_order_entity_form_dict = pay_order_entity.from_dict(pay_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


