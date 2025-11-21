try:
    from cashfree_pg.models.evidence import Evidence as PreferredEvidence
except Exception:
    class PreferredEvidence:
        pass
