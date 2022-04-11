from abc import ABC

class Api(ABC):
    def __init__(self, access_api_key: str, secret_key: str) -> None:
        self.access_api_key = access_api_key
        self.secret_key = secret_key

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

    from huobi_api.api.subuser import deduction_for_parent_and_subuser
    from huobi_api.api.subuser import apikey_query
    from huobi_api.api.subuser import get_uid
    from huobi_api.api.subuser import subuser_creation
    from huobi_api.api.subuser import get_subuser_list
    from huobi_api.api.subuser import lock_unlock_subuser
    from huobi_api.api.subuser import get_subuser_status
    from huobi_api.api.subuser import set_tradable_market
    from huobi_api.api.subuser import set_asset_transfer_permission
    from huobi_api.api.subuser import get_subuser_account_list
    from huobi_api.api.subuser import subuser_apikey_creation
    from huobi_api.api.subuser import subuser_apikey_modification
    from huobi_api.api.subuser import subuser_apikey_deletion
    from huobi_api.api.subuser import transfer_between_parent_subaccount
    from huobi_api.api.subuser import query_deposit_address_subuser
    from huobi_api.api.subuser import query_deposit_history_subuser
    from huobi_api.api.subuser import aggregate_balance_subusers
    from huobi_api.api.subuser import account_balance_subuser

    from huobi_api.api.trading import place_new_order
    from huobi_api.api.trading import place_batch_orders
    from huobi_api.api.trading import submit_cancel_order
    from huobi_api.api.trading import submit_cancel_order_client_id
    from huobi_api.api.trading import get_open_orders
    from huobi_api.api.trading import submit_cancel_multiple_orders
    from huobi_api.api.trading import submit_cancel_multiple_orders_ids
    from huobi_api.api.trading import dead_man_switch
    from huobi_api.api.trading import get_order_detail
    from huobi_api.api.trading import get_order_detail_id
    from huobi_api.api.trading import get_match_result_order
    from huobi_api.api.trading import search_past_orders
    from huobi_api.api.trading import search_history_orders_48hours
    from huobi_api.api.trading import search_match_results
    from huobi_api.api.trading import get_current_fee_rate_applied

    from huobi_api.signing import sign_request
