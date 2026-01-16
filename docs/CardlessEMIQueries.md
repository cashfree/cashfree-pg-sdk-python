# CardlessEMIQueries

cardless EMI query object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | OrderId of the order. Either of &#x60;order_id&#x60; or &#x60;amount&#x60; is mandatory. | [optional] 
**amount** | **float** | Amount of the order. OrderId of the order. Either of &#x60;order_id&#x60; or &#x60;amount&#x60; is mandatory. | [optional] 
**customer_details** | [**CustomerDetailsCardlessEMI**](CustomerDetailsCardlessEMI.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.cardless_emi_queries import CardlessEMIQueries

# TODO update the JSON string below
json = "{}"
# create an instance of CardlessEMIQueries from a JSON string
cardless_emi_queries_instance = CardlessEMIQueries.from_json(json)
# print the JSON string representation of the object
print CardlessEMIQueries.to_json()

# convert the object into a dict
cardless_emi_queries_dict = cardless_emi_queries_instance.to_dict()
# create an instance of CardlessEMIQueries from a dict
cardless_emi_queries_form_dict = cardless_emi_queries.from_dict(cardless_emi_queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


