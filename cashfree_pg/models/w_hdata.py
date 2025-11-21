try:
    from cashfree_pg.models.payment_webhook_data_entity import PaymentWebhookDataEntity as WHdata
except Exception:
    class WHdata:
        pass
