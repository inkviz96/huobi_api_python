class NotValidSignature(Exception):
    def __init__(self):
        self.text = 'invalid signature'


class ServerError(Exception):
    def __init__(self):
        self.text = 'Server internal error'


class UserIsUnautherized(Exception):
    def __init__(self):
        self.text = 'unauthorized'


class ParameterIsInvalid(Exception):
    def __init__(self):
        self.text = 'invalid field value in "field name"'


class ParameterIsMissing(Exception):
    def __init__(self):
        self.text = 'missing mandatory field "field name"'


class Forbidden(Exception):
    def __init__(self):
        self.text = 'operation is forbidden, such as the account Id and UID does not match'


status_bad = {
    'wallet': {
        '500': ServerError,
        '1002': UserIsUnautherized,
        '1003': NotValidSignature,
        '2002': ParameterIsInvalid,
        '2003': ParameterIsMissing,
    },
    'account': {
        '500': ServerError,
        '1002': Forbidden,
        '2002': ParameterIsInvalid,
    },
    'reference': {
        '500': ServerError,
    },
    'market': {
        '200': ParameterIsInvalid,
    },
}


def exception_status_code(api: str, status_sode: int, response_status: str) -> None:
    if status_sode != 200 or response_status == 'error':
        raise status_bad[api][str(status_sode)]
