try:
    from cashfree_pg.models.evidence import Evidence as DisputeEvidenceInner
except Exception:
    class DisputeEvidenceInner:
        pass
