from huobi_api.api_client import Api


class Client(Api):
    def __init__(self, access_api_key: str, secret_key: str) -> None:
        self.base_uri = 'api.huobi.pro'
        super(Client, self).__init__(access_api_key, secret_key)
