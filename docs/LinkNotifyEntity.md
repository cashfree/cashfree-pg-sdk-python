# LinkNotifyEntity

Payment link Notify Object for SMS and Email

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_sms** | **bool** | If \&quot;true\&quot;, Cashfree will send sms on customer_phone | [optional] 
**send_email** | **bool** | If \&quot;true\&quot;, Cashfree will send email on customer_email | [optional] 

## Example

```python
from cashfree_pg.models.link_notify_entity import LinkNotifyEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LinkNotifyEntity from a JSON string
link_notify_entity_instance = LinkNotifyEntity.from_json(json)
# print the JSON string representation of the object
print LinkNotifyEntity.to_json()

# convert the object into a dict
link_notify_entity_dict = link_notify_entity_instance.to_dict()
# create an instance of LinkNotifyEntity from a dict
link_notify_entity_form_dict = link_notify_entity.from_dict(link_notify_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


