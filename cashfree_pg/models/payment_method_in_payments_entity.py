try:
    from cashfree_pg.models.payment_method_app_in_payments_entity import PaymentMethodAppInPaymentsEntity as PaymentMethodInPaymentsEntity
except Exception:
    class PaymentMethodInPaymentsEntity:
        pass
