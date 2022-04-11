from huobi_api.tests.utils import mock_http_response, random_str
from huobi_api.client import Client
import responses

mock_item = {'status': 200}
key = random_str()
secret = random_str()

@mock_http_response(
    responses.GET, "/v1/account/accounts", mock_item, 200
)
def test_get_account():
    """Tests the API endpoint to get accounts"""
    client = Client(key, secret)
    response = client.get_accounts()
    response.should.equal(mock_item)
