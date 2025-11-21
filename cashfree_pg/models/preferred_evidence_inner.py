try:
    from cashfree_pg.models.evidence import Evidence as PreferredEvidenceInner
except Exception:
    class PreferredEvidenceInner:
        pass
