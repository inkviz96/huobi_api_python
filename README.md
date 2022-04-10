### HuobiPoolApi
[Official Documentation](https://huobiapi.github.io/docs/spot/)

[Github repository](https://github.com/inkviz96/huobi_api_python)

Get user accounts list
```python
from huobi_api.client import Client
cl = Client(access_api_key='knt3juterjg45', secret_key='fdwr42rwefsw3r1')
cl.get_accounts()
```

Withdraw from huobi pool Btc in hrc20btc chain
```python
from huobi_api.client import Client
cl = Client(access_api_key='knt3juterjg45', secret_key='fdwr42rwefsw3r1')
response = cl.chains_information(currency='btc')
data = response['data']
for x in data:
    for y in x["chains"]:
        if y["chain"] == "hrc20btc":
            fee = y["transactFeeWithdraw"]
cl.withdraw(address='0xr32rhdf234rfi3', currency='btc', amount='0.0321', fee=fee)
```
