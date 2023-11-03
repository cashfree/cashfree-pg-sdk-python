# LinkMetaEntity

Payment link meta information object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_url** | **str** | Notification URL for server-server communication. It should be an https URL. | [optional] 
**upi_intent** | **bool** | If \&quot;true\&quot;, link will directly open UPI Intent flow on mobile, and normal link flow elsewhere | [optional] 
**return_url** | **str** | The URL to which user will be redirected to after the payment is done on the link. Maximum length: 250. | [optional] 
**payment_methods** | **str** | Allowed payment modes for this link. Pass comma-separated values among following options - \&quot;cc\&quot;, \&quot;dc\&quot;, \&quot;ccc\&quot;, \&quot;ppc\&quot;, \&quot;nb\&quot;, \&quot;upi\&quot;, \&quot;paypal\&quot;, \&quot;app\&quot;. Leave it blank to show all available payment methods | [optional] 

## Example

```python
from cashfree_pg.models.link_meta_entity import LinkMetaEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LinkMetaEntity from a JSON string
link_meta_entity_instance = LinkMetaEntity.from_json(json)
# print the JSON string representation of the object
print LinkMetaEntity.to_json()

# convert the object into a dict
link_meta_entity_dict = link_meta_entity_instance.to_dict()
# create an instance of LinkMetaEntity from a dict
link_meta_entity_form_dict = link_meta_entity.from_dict(link_meta_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


