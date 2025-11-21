try:
    from cashfree_pg.models.settlement_webhook import SettlementWebhook as SettlementURLObject
except Exception:
    class SettlementURLObject:
        pass
