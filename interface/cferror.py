import urllib3


class CFError:
    status: int
    reason: str
    data: str
    headers = None

    def __init__(self, status=None, reason=None, data=None, headers=None):
        self.status = status
        self.reason = reason
        self.data = data
        self.headers = headers
