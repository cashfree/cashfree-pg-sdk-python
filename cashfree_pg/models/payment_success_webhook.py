try:
    from cashfree_pg.models.payment_webhook import PaymentWebhook as PaymentSuccessWebhook
except Exception:
    class PaymentSuccessWebhook:
        pass
