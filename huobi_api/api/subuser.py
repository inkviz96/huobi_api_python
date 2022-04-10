def deduction_for_parent_and_subuser(self, subUids: int, deductMode: str) -> dict:
    data = {
        'subUids': subUids,
        'deductMode': deductMode
    }
    return self.sign_request('subuser', 'GET', '/v2/sub-user/deduct-mode', data)


def apikey_query(self, uid: int, **kwargs) -> dict:
    """
    accessKey: str = None:
    """
    mandatory_data = {
        'uid': uid
    }
    data = {**mandatory_data, **kwargs}
    return self.sign_request('subuser', 'GET', '/v2/user/api-key', data)


def get_uid(self, code: int, data: int, message: str = None, **kwargs) -> dict:
    not_required_data = {
        'message': message
    } if message else {}
    mandatory_data = {
        'code': code,
    }
    mandatory_data = {**mandatory_data, **not_required_data, **{'data': data}}
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('subuser', 'GET', '/v2/user/uid', data)


def subuser_creation(self, userList: list) -> dict:
    data = {
        'userList': [user for user in userList]
    }
    return self.sign_request('subuser', 'POST', '/v2/sub-user/creation', body_data=data)


def get_subuser_list(self, **kwargs) -> dict:
    data = kwargs
    return self.sign_request('subuser', 'GET', '/v2/sub-user/user-list', data)


def lock_unlock_subuser(self, subUid: int, action: str) -> dict:
    data = {
        'subUid': subUid,
        'action': action
    }
    return self.sign_request('subuser', 'POST', '/v2/sub-user/management', body_data=data)


def get_subuser_status(self, subUid: int) -> dict:
    data = {
        'subUid': subUid
    }
    return self.sign_request('subuser', 'GET', '/v2/sub-user/user-state', data)


def set_tradable_market(self, subUids: str, accountType: str, activation: str) -> dict:
    data = {
        'subUids': subUids,
        'accountType': accountType,
        'activation': activation
    }
    return self.sign_request('subuser', 'POST', '/v2/sub-user/tradable-market', body_data=data)


def set_asset_transfer_permission(self, subUids: str, transferrable: bool, accountType: str = None) -> dict:
    not_required_data = {
        'accountType': accountType
    } if accountType else {}
    data = {**{'subUids': subUids}, **not_required_data, **{'transferrable': transferrable}}
    return self.sign_request('subuser', 'POST', '/v2/sub-user/transferability', body_data=data)


def get_subuser_account_list(self, subUid: str) -> dict:
    data = {
        'subUid': subUid
    }
    return self.sign_request('subuser', 'GET', '/v2/sub-user/account-list', data)


def subuser_apikey_creation(self, otpToken: str, subUid: int, note: str, permission: str) -> dict:
    data = {
        'otpToken': otpToken,
        'subuid': subUid,
        'note': note,
        'permission': permission
    }
    return self.sign_request('subuser', 'POST', '/v2/sub-user/api-key-generation', body_data=data)


def subuser_apikey_modification(self, subUid: int, accessKey: str, **kwargs) -> dict:
    data = {
        'subUid': subUid,
        'accessKey': accessKey
    }
    data = {**data, **kwargs}
    return self.sign_request('subuser', 'POST', '/v2/sub-user/api-key-modification', body_data=data)


def subuser_apikey_deletion(self, subUid: int, accesKey: str) -> dict:
    data = {
        'subuid': subUid,
        'accessKey': accesKey
    }
    return self.sign_request('subuser', 'POST', '/v2/sub-user/api-key-deletion', body_data=data)


def transfer_between_parent_subaccount(self, subUid: int, currency: str, amount: float, _type: str) -> dict:
    data = {
        'sub-uid': subUid,
        'currency': currency,
        'amount': amount,
        'type': _type
    }
    return self.sign_request('subuser', 'POST', '/v1/subuser/transfer', body_data=data)


def query_deposit_address_subuser(self, subUid: int, currency: str) -> dict:
    data = {
        'subUid': subUid,
        'currency': currency
    }
    return self.sign_request('subuser', 'GET', '/v2/sub-user/deposit-address', data)


def query_deposit_history_subuser(self, subUid: int, **kwargs) -> dict:
    data = {
        'subUid': subUid
    }
    data = {**data, **kwargs}
    return self.sign_request('subuser', 'GET', '/v2/sub-user/query-deposit', data)


def aggregate_balance_subusers(self) -> dict:
    return self.sign_request('subuser', 'GET', '/v1/subuser/aggregate-balance')


def account_balance_subuser(self, subUid: int) -> dict:
    return self.sign_request('subuser', 'GET', f'/v1/account/accounts{subUid}')
