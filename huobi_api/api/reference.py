def get_currencys_settings(self, **kwargs):
    data = kwargs
    return self.sign_request('GET', '/v1/settings/common/currencys', data)

def supported_currencys(self):
    return self.sign_request('GET', '/v1/common/currencys')

def chains_information(self, **kwargs):
    """
    currency: str = None
    authorizedUser: bool = None
    """
    data = kwargs
    return self.sign_request('GET', '/v2/reference/currencies', data)

