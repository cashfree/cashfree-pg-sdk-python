try:
    from cashfree_pg.models.fetch_settlements_request_filters import FetchSettlementsRequestFilters as SettlementFetchReconRequestFilters
except Exception:
    class SettlementFetchReconRequestFilters:
        pass
