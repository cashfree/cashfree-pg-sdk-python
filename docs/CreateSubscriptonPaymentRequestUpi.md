# CreateSubscriptonPaymentRequestUpi

payment method upi.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel. can be link, qrcode, or collect | [optional] 
**upi_id** | **str** |  | [optional] 

## Example

```python
from cashfree_pg.models.create_subscripton_payment_request_upi import CreateSubscriptonPaymentRequestUpi

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptonPaymentRequestUpi from a JSON string
create_subscripton_payment_request_upi_instance = CreateSubscriptonPaymentRequestUpi.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptonPaymentRequestUpi.to_json()

# convert the object into a dict
create_subscripton_payment_request_upi_dict = create_subscripton_payment_request_upi_instance.to_dict()
# create an instance of CreateSubscriptonPaymentRequestUpi from a dict
create_subscripton_payment_request_upi_form_dict = create_subscripton_payment_request_upi.from_dict(create_subscripton_payment_request_upi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


