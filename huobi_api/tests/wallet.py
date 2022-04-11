from huobi_api.tests.utils import mock_http_response, random_str
from huobi_api.client import Client
import responses
from huobi_api.exceptions import ParameterIsInvalid


key = random_str()
secret = random_str()
client = Client(key, secret)


mock_item_deposit_address = {'status': 200, "data": [
        {
            "userId": 12345678,
            "currency": "btc",
            "address": "0xd476b0d77583fbda5180039f1f513b750cb4f527",
            "addressTag": "",
            "chain": "hbtc"
        },
    ]
}

@mock_http_response(
    responses.GET, '/v2/account/deposit/address', mock_item_deposit_address, 200
)
def test_get_deposit_address():
    response = client.get_deposit_address(currency='btc')
    response.should.equal(mock_item_deposit_address)


mock_item_quota = {
    'data': {
        'chains':
            [
                {
                    'chain': 'hrc20usdt',
                    'maxWithdrawAmt': '2000000.000000000000000000',
                    'remainWithdrawQuotaPerDay': '4845303.99999991',
                    'remainWithdrawQuotaPerYear': '-1',
                    'remainWithdrawQuotaTotal': '-1',
                    'withdrawQuotaPerDay': '4845303.99999991',
                    'withdrawQuotaPerYear': '-1',
                    'withdrawQuotaTotal': '-1'
                }
            ],
        'currency': 'usdt'
    },
    'status': 200
}

@mock_http_response(
    responses.GET, '/v2/account/withdraw/quota', mock_item_quota, 200
)
def test_get_withdraw_quota():
    response = client.get_withdraw_quota(currency='btc')
    response.should.equal(mock_item_quota)


mock_exception = {'status': 2002}
@mock_http_response(
    responses.POST, '/v1/dw/withdraw/api/create', mock_exception, 2002
)
def test_withdraw_exception():
    client.withdraw.when.called_with(address='', currency='', amount=2, fee=0.0002).should.throw(
        ParameterIsInvalid
    )


mock_item_withdraw = {
    "status": 200,
    "data": {
        "address": "0xde709f2102306220921060314715629080e2fb77",
        "amount": "0.05",
        "currency": "eth",
        "fee": "0.01"
}
}

@mock_http_response(
    responses.POST, '/v1/dw/withdraw/api/create', mock_item_withdraw, 200
)
def test_withdraw():
    response = client.withdraw(
        address='0xde709f2102306220921060314715629080e2fb77',
        currency='eth',
        amount='0.05',
        fee=0.01
    )
    response.should.equal(mock_item_withdraw)


mock_item_withdraw_address = {
    "status": 200,
    "data": [
        {
            "currency": "usdt",
            "chain": "hrc20usdt",
            "note": "tom",
            "addressTag": "",
            "address": "0x3b994f25c4c25e99d4d26364ffc014cce64600ca"
        }
    ],
    "next-id": 30137790
}

@mock_http_response(
    responses.GET, '/v2/account/withdraw/address', mock_item_withdraw_address, 200
)
def test_get_withdraw_address():
    response = client.get_withdraw_address(
        currency='usdt'
    )
    response.should.equal(mock_item_withdraw_address)
