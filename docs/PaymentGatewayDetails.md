# PaymentGatewayDetails

payment gateway details present in the webhook response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_name** | **str** |  | [optional] 
**gateway_order_id** | **str** |  | [optional] 
**gateway_payment_id** | **str** |  | [optional] 
**gateway_order_reference_id** | **str** |  | [optional] 
**gateway_status_code** | **str** |  | [optional] 
**gateway_settlement** | **str** |  | [optional] 
**gateway_reference_name** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.payment_gateway_details import PaymentGatewayDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentGatewayDetails from a JSON string
payment_gateway_details_instance = PaymentGatewayDetails.from_json(json)
# print the JSON string representation of the object
print PaymentGatewayDetails.to_json()

# convert the object into a dict
payment_gateway_details_dict = payment_gateway_details_instance.to_dict()
# create an instance of PaymentGatewayDetails from a dict
payment_gateway_details_form_dict = payment_gateway_details.from_dict(payment_gateway_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


