def get_currencys_settings(self, **kwargs):
    data = kwargs
    return self.sign_request('GET', '/v1/settings/common/currencys', data)

def chains_information(self, **kwargs):
    """
    currency: str = None
    authorizedUser: bool = None
    """
    data = kwargs
    return self.sign_request('GET', '/v2/reference/currencies', data)

def system_status(self):
    return self.sign_request('GET', 'https://status.huobigroup.com/api/v2/summary.json')

def market_status(self):
    return self.sign_request('GET', '/v2/market-status')

def supported_trading_symbols(self, **kwargs):
    """
    ts: int = None
    """
    data = kwargs
    return self.sign_request('GET', '/v2/settings/common/symbols', data)

def supported_trading_currencies(self, **kwargs):
    """
    ts: int = None
    """
    data = kwargs
    return self.sign_request('GET', '/v2/settings/common/currencies', data)

def get_symbols_settings(self, **kwargs):
    """
    ts: int = None
    """
    data = kwargs
    return self.sign_request('GET', '/v1/settings/common/symbols', data)

def get_market_symbols(self, **kwargs):
    """
    symbols: str = None
    ts: int = None
    """
    data = kwargs
    return self.sign_request('GET', '/v1/settings/common/market-symbols', data)

def get_currency_and_chains(self, **kwargs):
    """
    currency: str = None
    authorizedUser: bool = None
    """
    data = kwargs
    return self.sign_request('GET', '/v2/reference/currencies', data)

def get_current_timestamp(self):
    return self.sign_request('GET', '/v1/common/timestamp')
