try:
    from cashfree_pg.models.payment_webhook_customer_entity import PaymentWebhookCustomerEntity as WHcustomerDetails
except Exception:
    class WHcustomerDetails:
        pass
