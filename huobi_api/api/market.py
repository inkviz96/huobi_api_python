import json


def get_klines(self, symbol: str, period: str, **kwargs) -> json:
    """
    size: int = None
    """
    mandatory_data = {
        'symbol': symbol,
        'period': period
    }
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('market', 'GET', '/market/history/kline', data)


def get_latest_aggregate_ticker(self, symbol: str) -> json:
    data = {
        'symbol': symbol,
    }
    return self.sign_request('market', 'GET', '/market/detail/merged', data)


def get_latest_tickers_all_pairs(self) -> json:
    return self.sign_request('market', 'GET', '/market/tickers')


def get_market_depth(self, symbol: str, _type: str, depth: int = None, **kwargs) -> json:
    not_required_data = {
        'depth': depth
    } if depth else {}
    mandatory_data = {
        'symbol': symbol,
    }
    mandatory_data = {**mandatory_data, **not_required_data, **{'type': _type}}
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('market', 'GET', '/market/depth', data)


def get_last_trade(self, symbol: str) -> json:
    data = {
        'symbol': symbol,
    }
    return self.sign_request('market', 'GET', '/market/trade', data)


def get_most_recent_trades(self, symbol: str, **kwargs) -> json:
    """
    size: int = None
    """
    mandatory_data = {
        'symbol': symbol,
    }
    data = {**mandatory_data, **kwargs} if kwargs else mandatory_data
    return self.sign_request('market', 'GET', '/market/history/trade', data)


def get_last_24h_market_summary(self, symbol: str) -> json:
    data = {
        'symbol': symbol,
    }
    return self.sign_request('market', 'GET', '/market/detail', data)


def get_real_time_nav(self, symbol: str) -> json:
    data = {
        'symbol': symbol,
    }
    return self.sign_request('market', 'GET', '/market/etp', data)
