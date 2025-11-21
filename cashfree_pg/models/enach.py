try:
    from cashfree_pg.models.upi import UPI as ENACH
except Exception:
    class ENACH:
        pass
