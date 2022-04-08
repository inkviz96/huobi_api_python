import json

from huobi_api.exceptions import exception_status_code
from requests import Response


def exception_catch(api: str, response: Response) -> None:
    status_code = response.status_code
    response_status = json.loads(response.text)['status']
    exception_status_code(api, status_code, response_status)
