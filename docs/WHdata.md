# WHdata

webhook object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**WHorder**](WHorder.md) |  | [optional] 
**payment** | [**PaymentEntity**](PaymentEntity.md) |  | [optional] 
**customer_details** | [**WHcustomerDetails**](WHcustomerDetails.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.w_hdata import WHdata

# TODO update the JSON string below
json = "{}"
# create an instance of WHdata from a JSON string
w_hdata_instance = WHdata.from_json(json)
# print the JSON string representation of the object
print WHdata.to_json()

# convert the object into a dict
w_hdata_dict = w_hdata_instance.to_dict()
# create an instance of WHdata from a dict
w_hdata_form_dict = w_hdata.from_dict(w_hdata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


