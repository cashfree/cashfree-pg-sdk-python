from pyexpat.errors import XML_ERROR_ENTITY_DECLARED_IN_PE
from enum import Enum


class CFenv(Enum):
    SANDBOX = 1
    PRODUCTION = 2


class CFConfig:
    x_client_id = ""
    x_client_secret = ""
    x_api_version = ""
    cf_env = CFenv.SANDBOX

    def __init__(self, x_client_id=None, x_client_secret=None, x_api_version=None, cf_env=CFenv.SANDBOX):
        self.x_client_id = x_client_id
        self.x_client_secret = x_client_secret
        self.x_api_version = x_api_version
        self.cf_env = cf_env
