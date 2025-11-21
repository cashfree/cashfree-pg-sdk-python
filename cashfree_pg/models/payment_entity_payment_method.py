try:
    from cashfree_pg.models.payment_method_card_in_payments_entity_card import PaymentMethodCardInPaymentsEntityCard as PaymentEntityPaymentMethod
except Exception:
    class PaymentEntityPaymentMethod:
        pass
