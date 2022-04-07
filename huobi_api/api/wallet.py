

def get_deposit_address(self, currency: str):
    data = {
        'currency': currency
    }
    return self.sign_request('GET', '/v2/account/deposit/address', data)

def get_withdraw_quota(self, currency: str):
    data = {
        'currency': currency
    }
    return self.sign_request('GET', '/v2/account/withdraw/quota', data)

def get_withdraw_address(self, currency: str, **kwargs):
    """
    note: str = None
    limit: int = None
    fromId: int = None
    """
    mandatory_data = {
        'currency': currency,
    }
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('GET', '/v2/account/withdraw/address', data)

def withdraw(self, address: str, currency: str, amount: str, fee: float, **kwargs):
    """
    chain: str = None
    addr-tag: str = None
    client-order-id: str = None
    """
    mandatory_data = {
        'address': address,
        'currency': currency,
        'amount': amount,
        'fee': fee
    }
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('POST', '/v1/dw/withdraw/api/create', body_data=data)

def withdrawal_order_by_order_id(self, clientOrderId: str):
    data = {
        'clientOrderId': clientOrderId
    }
    return self.sign_request('GET', '/v1/query/withdraw/client-order-id', data)

def cancel_withdraw(self, withdraw_id: str):
    return self.sign_request('POST', f'/v1/dw/withdraw-virtual/{withdraw_id}/cancel')

def get_deposit_withdraw(self, type: str, currency: str = None, **kwargs):
    """
    from: str = None
    size: str = None
    direct: str = None
    """
    not_required_data = {
        'currency': currency
    } if currency else {}
    mandatory_data = {
        'type': type,
    }
    mandatory_data = {**not_required_data, **mandatory_data}
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('GET', '/v1/query/deposit-withdraw', data)
