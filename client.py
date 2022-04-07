

class Client:
    def __init__(self, access_api_key: str, secret_key: str) -> None:
        self.access_api_key = access_api_key
        self.secret_key = secret_key


    from api.account import get_accounts
    from api.account import get_account_balance
    from api.account import get_total_valuation
    from api.account import get_asset_valuation
    from api.account import account_transfer
    from api.account import get_account_history
    from api.account import get_account_ledger
    from api.account import transfer_fund_between_spot_account
    from api.account import get_point_balance
    from api.account import point_transfer

    from api.wallet import get_deposit_address
    from api.wallet import get_withdraw_quota
    from api.wallet import get_withdraw_address
    from api.wallet import withdraw
    from api.wallet import withdrawal_order_by_order_id
    from api.wallet import cancel_withdraw
    from api.wallet import get_deposit_withdraw

    from signing import sign_request


