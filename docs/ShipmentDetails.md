# ShipmentDetails

Shipment details associated with shipping of order like tracking company, tracking number,tracking urls etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_company** | **str** | Tracking company name associated with order. | 
**tracking_urls** | **List[str]** | Tracking Urls associated with order. | 
**tracking_numbers** | **List[str]** | Tracking Numbers associated with order. | 

## Example

```python
from cashfree_pg.models.shipment_details import ShipmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDetails from a JSON string
shipment_details_instance = ShipmentDetails.from_json(json)
# print the JSON string representation of the object
print(ShipmentDetails.to_json())

# convert the object into a dict
shipment_details_dict = shipment_details_instance.to_dict()
# create an instance of ShipmentDetails from a dict
shipment_details_from_dict = ShipmentDetails.from_dict(shipment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


