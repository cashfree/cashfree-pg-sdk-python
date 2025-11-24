try:
    from cashfree_pg.models.evidence import Evidence as DisputeEvidence
except Exception:
    class DisputeEvidence:  # placeholder
        pass
