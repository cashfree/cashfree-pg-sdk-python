from cashfree_pg_sdk_python import api_client
from cashfree_pg_sdk_python.interface.cfconfig import CFenv
from cashfree_pg_sdk_python.configuration import Configuration
from cashfree_pg_sdk_python.interface.cfconfig import CFConfig
from cashfree_pg_sdk_python.interface.cfconfig import CFenv
from cashfree_pg_sdk_python.interface.cferror import CFError
from cashfree_pg_sdk_python.interface.cfheaders import CFHeaders
from cashfree_pg_sdk_python.api.orders_api import OrdersApi
from cashfree_pg_sdk_python.models.cf_order_request import CFOrderRequest
from cashfree_pg_sdk_python.exceptions import ApiException, ConfigException
from cashfree_pg_sdk_python.api.payments_api import PaymentsApi
from cashfree_pg_sdk_python.models.cf_order_pay_request import CFOrderPayRequest
from cashfree_pg_sdk_python.api.refunds_api import RefundsApi
from cashfree_pg_sdk_python.models.cf_refund_request import CFRefundRequest


def checkAndSetConfig(cfConfig: CFConfig):
    errorObject = CFError(401, "Unauthorised Request")
    if cfConfig.x_client_id is None or "":
        errorObject.data = {
            "message": "xCLientId is missing", "code": "xCLientId_missing", "type": "bad_request"}
        raise ConfigException(errorObject)
    if cfConfig.x_client_secret is None or "":
        errorObject.data = {
            "message": "xCLientSecret is missing", "code": "xCLientSecret_missing", "type": "bad_request"}
        raise ConfigException(errorObject)
    if cfConfig.cf_env is None or "":
        errorObject.data = {
            "message": "environment is missing", "code": "environment_missing", "type": "bad_request"}
        raise ConfigException(errorObject)

    if cfConfig.cf_env == CFenv.PRODUCTION:
        configuration = Configuration(
            host="https://api.cashfree.com/pg"
        )
    elif cfConfig.cf_env == CFenv.SANDBOX:
        configuration = Configuration(
            host="https://sandbox.cashfree.com/pg"
        )
    else:
        errorObject.data = {
            "message": "wrong environment passed", "code": "request_failed", "type": "bad_request"}
        raise ConfigException(errorObject)
    return configuration


def CreateOrder(cfConfig: CFConfig, cfHeaders: CFHeaders, cfOrderRequest: CFOrderRequest):
    """ Use this function to create orders with Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        While cfHeaders is not a mandatory object but it can help with setting x-request-id for efficient logging. Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders:
        :type cfHeaders: CFHeaders

        :param cfOrderRequest: (required)
        :type cfOrderRequest: CFOrderRequest
    """
    try:
        ordersApiInstance = OrdersApi(api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = ordersApiInstance.create_order_with_http_info(cfConfig.x_client_id, cfConfig.x_client_secret, x_api_version=cfConfig.x_api_version,
                                                                     x_idempotency_key=cfHeaders.x_idempotency_key, x_idempotency_replayed=False, x_request_id=cfHeaders.x_request_id, cf_order_request=cfOrderRequest)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e


def OrderPay(cfConfig: CFConfig, cfHeaders: CFHeaders, orderPayRequest: CFOrderPayRequest):
    """ Use this function to get order details of already created orders via Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders:
        :type cfHeaders: CFHeaders

        :param orderPayRequest: (required)
        :type orderPayRequest: CFOrderPayRequest
    """
    try:
        ordersApiInstance = OrdersApi(api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = ordersApiInstance.order_pay_with_http_info(x_api_version=cfConfig.x_api_version, x_request_id=cfHeaders.x_request_id,
                                                                  cf_order_pay_request=orderPayRequest)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e


def GetOrder(cfConfig: CFConfig, cfHeaders: CFHeaders, orderId: str):
    """ Use this function to get order details of already created orders via Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        While cfHeaders is not a mandatory object but it can help with setting x-request-id for efficient logging. Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders: 
        :type cfHeaders: CFHeaders

        :param orderID: (required)
        :type orderId: str
    """
    try:
        ordersApiInstance = OrdersApi(api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = ordersApiInstance.get_order_with_http_info(cfConfig.x_client_id, cfConfig.x_client_secret, x_api_version=cfConfig.x_api_version,
                                                                  x_idempotency_key=cfHeaders.x_idempotency_key, x_idempotency_replayed=False, x_request_id=cfHeaders.x_request_id, order_id=orderId)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e


def GetAllPayments(cfConfig: CFConfig, cfHeaders: CFHeaders, orderId: str):
    """ Use this function to get details for all transactions for a particular orderId via Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        While cfHeaders is not a mandatory object but it can help with setting x-request-id for efficient logging. Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders: 
        :type cfHeaders: CFHeaders

        :param orderID: (required)
        :type orderId: str
    """
    try:
        paymentsApiInstance = PaymentsApi(
            api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = paymentsApiInstance.get_paymentsfororder(cfConfig.x_client_id, cfConfig.x_client_secret, x_api_version=cfConfig.x_api_version,
                                                                x_idempotency_key=cfHeaders.x_idempotency_key, x_idempotency_replayed=False, x_request_id=cfHeaders.x_request_id, order_id=orderId)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e


def GetPaymentByPaymentId(cfConfig: CFConfig, cfHeaders: CFHeaders, orderId: str, paymentId: int):
    """ Use this function to get details for a transaction for a particular orderId and paymentId via Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        While cfHeaders is not a mandatory object but it can help with setting x-request-id for efficient logging. Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders: 
        :type cfHeaders: CFHeaders

        :param orderID: (required)
        :type orderId: str

        :param paymentId: (required)
        :type paymentId: int
    """
    try:
        paymentsApiInstance = PaymentsApi(
            api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = paymentsApiInstance.get_paymentby_id_with_http_info(cfConfig.x_client_id, cfConfig.x_client_secret, x_api_version=cfConfig.x_api_version,
                                                                           x_idempotency_key=cfHeaders.x_idempotency_key, x_idempotency_replayed=False, x_request_id=cfHeaders.x_request_id, order_id=orderId, cf_payment_id=paymentId)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e


def InitiateRefund(cfConfig: CFConfig, cfHeaders: CFHeaders, orderId: str, refundRequest: CFRefundRequest):
    """ Use this function to create refund for a successful transaction for an orderId via Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        While cfHeaders is not a mandatory object but it can help with setting x-request-id for efficient logging. Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders: 
        :type cfHeaders: CFHeaders

        :param orderID: (required)
        :type orderId: str

        :param refundRequest: (required)
        :type refundRequest: CFRefundRequest
    """
    try:
        refundsApiInstance = RefundsApi(
            api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = refundsApiInstance.createrefund_with_http_info(cfConfig.x_client_id, cfConfig.x_client_secret, x_api_version=cfConfig.x_api_version,
                                                                      x_idempotency_key=cfHeaders.x_idempotency_key, x_idempotency_replayed=False, x_request_id=cfHeaders.x_request_id, order_id=orderId, cf_refund_request=refundRequest)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e


def GetAllRefunds(cfConfig: CFConfig, cfHeaders: CFHeaders, orderId: str):
    """ Use this function to create refund for a successful transaction for an orderId via Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders: 
        :type cfHeaders: CFHeaders

        :param orderID: (required)
        :type orderId: str
    """
    try:
        refundsApiInstance = RefundsApi(
            api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = refundsApiInstance.getallrefundsfororder_with_http_info(cfConfig.x_client_id, cfConfig.x_client_secret, x_api_version=cfConfig.x_api_version,
                                                                               order_id=orderId)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e


def GetRefundByRefundId(cfConfig: CFConfig, cfHeaders: CFHeaders, orderId: str, refundId: str):
    """ Use this function to create refund for a successful transaction for an orderId and refundId via Cashfree from your backend. Make sure that env is properly set using cfconfig module's CFEnv.
        While cfHeaders is not a mandatory object but it can help with setting x-request-id for efficient logging. Refer the readme file for examples.

        :param cfConfig: (required)
        :type cfConfig: CFConfig

        :param cfHeaders: 
        :type cfHeaders: CFHeaders

        :param orderID: (required)
        :type orderId: str

        :param refundId: (required)
        :type refundId: str
    """
    try:
        refundsApiInstance = RefundsApi(
            api_client.ApiClient(checkAndSetConfig(cfConfig)))
        api_response = refundsApiInstance.get_refund_with_http_info(cfConfig.x_client_id, cfConfig.x_client_secret, x_api_version=cfConfig.x_api_version,
                                                                    x_idempotency_key=cfHeaders.x_idempotency_key, x_idempotency_replayed=False, x_request_id=cfHeaders.x_request_id, order_id=orderId, cf_refund_id=refundId)
        return api_response
    except ConfigException as c:
        return c
    except ApiException as e:
        return e
