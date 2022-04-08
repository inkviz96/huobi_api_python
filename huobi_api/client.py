

class Client:
    def __init__(self, access_api_key: str, secret_key: str) -> None:
        self.access_api_key = access_api_key
        self.secret_key = secret_key
        self.base_uri = 'api.huobi.pro'

    from huobi_api.api.wallet import get_deposit_address
    from huobi_api.api.wallet import get_withdraw_quota
    from huobi_api.api.wallet import get_withdraw_address
    from huobi_api.api.wallet import withdraw
    from huobi_api.api.wallet import withdrawal_order_by_order_id
    from huobi_api.api.wallet import cancel_withdraw
    from huobi_api.api.wallet import get_deposit_withdraw

    from huobi_api.api.account import get_accounts
    from huobi_api.api.account import get_account_balance
    from huobi_api.api.account import get_total_valuation
    from huobi_api.api.account import get_asset_valuation
    from huobi_api.api.account import account_transfer
    from huobi_api.api.account import get_account_history
    from huobi_api.api.account import get_account_ledger
    from huobi_api.api.account import transfer_fund_between_spot_account
    from huobi_api.api.account import get_point_balance
    from huobi_api.api.account import point_transfer

    from huobi_api.api.reference import get_currencys_settings
    from huobi_api.api.reference import chains_information
    from huobi_api.api.reference import system_status
    from huobi_api.api.reference import market_status
    from huobi_api.api.reference import supported_trading_currencies
    from huobi_api.api.reference import supported_trading_symbols
    from huobi_api.api.reference import get_symbols_settings
    from huobi_api.api.reference import get_market_symbols
    from huobi_api.api.reference import get_currency_and_chains
    from huobi_api.api.reference import get_current_timestamp

    from huobi_api.api.market import get_klines
    from huobi_api.api.market import get_latest_aggregate_ticker
    from huobi_api.api.market import get_latest_tickers_all_pairs
    from huobi_api.api.market import get_market_depth
    from huobi_api.api.market import get_last_trade
    from huobi_api.api.market import get_most_recent_trades
    from huobi_api.api.market import get_last_24h_market_summary
    from huobi_api.api.market import get_real_time_nav

    from huobi_api.signing import sign_request
