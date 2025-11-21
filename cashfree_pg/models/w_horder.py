try:
    from cashfree_pg.models.payment_webhook_order_entity import PaymentWebhookOrderEntity as WHorder
except Exception:
    class WHorder:
        pass
