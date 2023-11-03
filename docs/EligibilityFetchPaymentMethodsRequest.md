# EligibilityFetchPaymentMethodsRequest

eligibilty request to find eligible payment method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**PaymentMethodsQueries**](PaymentMethodsQueries.md) |  | 
**filters** | [**PaymentMethodsFilters**](PaymentMethodsFilters.md) |  | [optional] 

## Example

```python
from cashfree_pg.models.eligibility_fetch_payment_methods_request import EligibilityFetchPaymentMethodsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityFetchPaymentMethodsRequest from a JSON string
eligibility_fetch_payment_methods_request_instance = EligibilityFetchPaymentMethodsRequest.from_json(json)
# print the JSON string representation of the object
print EligibilityFetchPaymentMethodsRequest.to_json()

# convert the object into a dict
eligibility_fetch_payment_methods_request_dict = eligibility_fetch_payment_methods_request_instance.to_dict()
# create an instance of EligibilityFetchPaymentMethodsRequest from a dict
eligibility_fetch_payment_methods_request_form_dict = eligibility_fetch_payment_methods_request.from_dict(eligibility_fetch_payment_methods_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


