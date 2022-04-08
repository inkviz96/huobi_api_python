from datetime import datetime
from urllib.parse import urlencode

import requests
import json
import hmac
import hashlib
import base64

from huobi_api.check_response import exception_catch


def sign_request(self, api: str, method: str, endpoint: str, data: dict = None, body_data: dict = None) -> json:
    base_data = {
        'AccessKeyId': self.access_api_key,
        'SignatureMethod': 'HmacSHA256',
        'SignatureVersion': '2',
        'Timestamp': str(datetime.utcnow().isoformat())[0:19],
    }
    full_data = {**base_data, **data} if data else base_data
    params = urlencode(full_data)
    pre_signed_text = f'{method}\n{self.base_uri}\n{endpoint}\n{params}'
    hash_code = hmac.new(self.secret_key.encode(), pre_signed_text.encode(), hashlib.sha256).digest()
    signature = urlencode({'Signature': base64.b64encode(hash_code).decode()})
    url = f'https://{self.base_uri}{endpoint}?{params}&{signature}'
    response = requests.request(method, url, json=body_data)
    exception_catch(api, response)
    return json.loads(response.text)
