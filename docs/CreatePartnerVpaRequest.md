# CreatePartnerVpaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpa_count** | **int** | count of vpa , to create in bulk, max limit:50 | 

## Example

```python
from cashfree_pg.models.create_partner_vpa_request import CreatePartnerVpaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePartnerVpaRequest from a JSON string
create_partner_vpa_request_instance = CreatePartnerVpaRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePartnerVpaRequest.to_json())

# convert the object into a dict
create_partner_vpa_request_dict = create_partner_vpa_request_instance.to_dict()
# create an instance of CreatePartnerVpaRequest from a dict
create_partner_vpa_request_from_dict = CreatePartnerVpaRequest.from_dict(create_partner_vpa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


