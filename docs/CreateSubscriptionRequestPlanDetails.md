# CreateSubscriptionRequestPlanDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | The unique identifier used to create plan. You only need to pass this field if you had already created plan. Otherwise use the other fields here to define the plan. | [optional] 
**plan_name** | **str** | Specify plan name for easy reference. | [optional] 
**plan_type** | **str** | Possible values ON_DEMAND or PERIODIC. PERIODIC - Payments are triggered automatically at fixed intervals defined by the merchant. ON_DEMAND - Merchant needs to trigger/charge the customer explicitly with the required amount. | [optional] 
**plan_currency** | **str** | INR by default. | [optional] 
**plan_amount** | **float** | The amount to be charged for PERIODIC plan. This is a conditional parameter, only required for PERIODIC plans. | [optional] 
**plan_max_amount** | **float** | This is the maximum amount that can be charged on a subscription. | [optional] 
**plan_max_cycles** | **int** | Maximum number of debits set for the plan. The subscription will automatically change to COMPLETED status once this limit is reached. | [optional] 
**plan_intervals** | **int** | Number of intervals of intervalType between every subscription payment. For example, to charge a customer bi-weekly use intervalType as “week” and intervals as 2. Required for PERIODIC plan. The default value is 1. | [optional] 
**plan_interval_type** | **str** | The type of interval for a PERIODIC plan like DAY, WEEK, MONTH, or YEAR. This is a conditional parameter only applicable for PERIODIC plans. | [optional] 
**plan_note** | **str** | Note for the plan. | [optional] 

## Example

```python
from cashfree_pg.models.create_subscription_request_plan_details import CreateSubscriptionRequestPlanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequestPlanDetails from a JSON string
create_subscription_request_plan_details_instance = CreateSubscriptionRequestPlanDetails.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionRequestPlanDetails.to_json()

# convert the object into a dict
create_subscription_request_plan_details_dict = create_subscription_request_plan_details_instance.to_dict()
# create an instance of CreateSubscriptionRequestPlanDetails from a dict
create_subscription_request_plan_details_form_dict = create_subscription_request_plan_details.from_dict(create_subscription_request_plan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


