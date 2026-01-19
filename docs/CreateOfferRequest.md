# CreateOfferRequest

create offer backend request object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_meta** | [**OfferMeta**](OfferMeta.md) |  | 
**offer_tnc** | [**OfferTnc**](OfferTnc.md) |  | 
**offer_details** | [**OfferDetails**](OfferDetails.md) |  | 
**offer_validations** | [**OfferValidations**](OfferValidations.md) |  | 

## Example

```python
from cashfree_pg.models.create_offer_request import CreateOfferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOfferRequest from a JSON string
create_offer_request_instance = CreateOfferRequest.from_json(json)
# print the JSON string representation of the object
print CreateOfferRequest.to_json()

# convert the object into a dict
create_offer_request_dict = create_offer_request_instance.to_dict()
# create an instance of CreateOfferRequest from a dict
create_offer_request_form_dict = create_offer_request.from_dict(create_offer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


