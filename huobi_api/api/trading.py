def place_new_order(self, account_id: str, symbol: str, _type: str, amount: str, **kwargs) -> dict:
    data = {
        'account-id': account_id,
        'symbol': symbol,
        'type': _type,
        'amount': amount
    }
    data = {**data, **kwargs}
    return self.sign_request('trading', 'POST', '/v1/order/orders/place', body_data=data)


def place_batch_orders(self, account_id: str, symbol: str, _type: str, amount: str, **kwargs) -> dict:
    data = {
        'account-id': account_id,
        'symbol': symbol,
        'type': _type,
        'amount': amount
    }
    data = {**data, **kwargs}
    return self.sign_request('trading', 'POST', '/v1/order/batch-orders', body_data=data)


def submit_cancel_order(self, order_id: str, **kwargs) -> dict:
    data = kwargs
    return self.sign_request('trading', 'POST', f'/v1/order/orders/{order_id}/submitcancel', body_data=data)


def submit_cancel_order_client_id(self, client_order_id: str) -> dict:
    data = {
        'client-order-id': client_order_id
    }
    return self.sign_request('trading', 'POST', '/v1/order/orders/submitCancelClientOrder', body_data=data)


def get_open_orders(self, **kwargs) -> dict:
    data = kwargs
    return self.sign_request('trading', 'GET', '/v1/order/openOrders', data)


def submit_cancel_multiple_orders(self, **kwargs) -> dict:
    data = kwargs
    return self.sign_request('trading', 'POST', '/v1/order/orders/batchCancelOpenOrders', body_data=data)


def submit_cancel_multiple_orders_ids(self, **kwargs) -> dict:
    data = kwargs
    return self.sign_request('trading', 'POST', '/v1/order/orders/batchcancel', body_data=data)


def dead_man_switch(self, timeout: int) -> dict:
    data = {
        'timeout': timeout
    }
    return self.sign_request('trading', 'POST', '/v2/algo-orders/cancel-all-after', body_data=data)


def get_order_detail(self, order_id: str) -> dict:
    return self.sign_request('trading', 'GET', f'/v1/order/orders/{order_id}')


def get_order_detail_id(self, clientOrderId: str) -> dict:
    data = {
        'clientOrderId': clientOrderId
    }
    return self.sign_request('trading', 'GET', '/v1/order/orders/getClientOrder', data)


def get_match_result_order(self, order_id: str) -> dict:
    return self.sign_request('trading', 'GET', f'/v1/order/orders/{order_id}/matchresults')


def search_past_orders(
        self,
        symbol: str,
        states: str,
        _types: str = None,
        start_time: int = None,
        end_time: int = None,
        **kwargs
) -> dict:
    not_required_data = {
        'types': _types if _types else '',
        'start-time': start_time if start_time else '',
        'end-time': end_time if end_time else ''
    }
    mandatory_data = {
        'symbol': symbol,
    }
    mandatory_data = {**mandatory_data, **not_required_data, **{'states': states}}
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    data = dict((k, v) for k, v in data.items() if v)
    return self.sign_request('trading', 'GET', '/v1/order/orders', data)


def search_history_orders_48hours(self, **kwargs) -> dict:
    data = kwargs
    return self.sign_request('trading', 'GET', '/v1/order/history', data)


def search_match_results(self, symbol: str, _types: str, **kwargs) -> dict:
    data = {
        'symbol': symbol,
        'types': _types
    }
    data = {**data, **kwargs}
    return self.sign_request('trading', 'GET', '/v1/order/matchresults', data)


def get_current_fee_rate_applied(self, symbols: str) -> dict:
    data = {
        'symbols': symbols
    }
    return self.sign_request('trading', 'GET', '/v2/reference/transact-fee-rate', data)
