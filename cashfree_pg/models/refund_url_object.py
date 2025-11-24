try:
    from cashfree_pg.models.refund_webhook import RefundWebhook as RefundURLObject
except Exception:
    class RefundURLObject:
        pass
