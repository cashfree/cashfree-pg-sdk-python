try:
    from cashfree_pg.models.payment_link_order_entity import PaymentLinkOrderEntity as PaymentURLObject
except Exception:
    class PaymentURLObject:
        pass
