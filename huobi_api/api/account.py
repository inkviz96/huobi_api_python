

def get_accounts(self):
    return self.sign_request('GET', '/v1/account/accounts')

def get_account_balance(self, account_id: int):
    return self.sign_request('GET', f'/v1/account/accounts/{account_id}/balance')

def get_total_valuation(self, **kwargs):
    """
    accountType: str = None
    valuationCurrency: str = None
    """
    data = kwargs
    return self.sign_request('GET', '/v2/account/valuation', data)

def get_asset_valuation(self, accountType: str, **kwargs):
    mandatory_data = {
        'accountType': accountType
    }
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('GET', '/v2/account/asset-valuation', data)

def account_transfer(
        self, from_user: int,
        from_account_type: str,
        from_account: int,
        to_user: int,
        to_account_type: str,
        to_account: int,
        currency: str,
        amount: str
):
    data = {
        'from-user': from_user,
        'from-account-type': from_account_type,
        'from-account': from_account,
        'to-user': to_user,
        'to-account_type': to_account_type,
        'to-account': to_account,
        'currency': currency,
        'amount': amount
    }
    return self.sign_request('POST', '/v1/account/transfer', body_data=data)

def get_account_history(self):
    return self.sign_request('GET', '/v1/account/history')

def get_account_ledger(self, accountId: str, **kwargs):
    """
    currency: str = None
    transactTypes: str = None
    startTime: int = None
    endTime: int = None
    sort: str = None
    limit: int = None
    fromId: int = None
    """
    mandatory_data = {
        'accountId': accountId
    }
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('GET', '/v2/account/ledger', data)

def transfer_fund_between_spot_account(self, currency: str, amount: float, type:str):
    data = {
        'currency': currency, # Currency name 	Refer to GET /v1/common/currencys
        'amount': amount,
        'type': type # Type of the transfer 	"futures-to-pro" or "pro-to-futures"
    }
    return self.sign_request('POST', '/v1/futures/transfer', body_data=data)

def get_point_balance(self, **kwargs):
    """
    subUid: str = None
    """
    data = kwargs
    return self.sign_request('GET', '/v2/point/account', data)

def point_transfer(self, fromUid: str, toUid: str, groupId: int, amount: str):
    data = {
        'fromUid': fromUid,
        'toUid': toUid,
        'groupId': groupId,
        'amount': amount
    }
    return self.sign_request('POST', '/v2/point/transfer', body_data=data)
