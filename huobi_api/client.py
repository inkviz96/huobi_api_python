

class Client:
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
    from huobi_api.api.reference import supported_currencys
    from huobi_api.api.reference import chains_information

    from huobi_api.signing import sign_request
