### HuobiPoolApi


Get user accounts list
```
from client import Client
cl = Client(access_api_key='knt3juterjg45', secret_key='fdwr42rwefsw3r1')
cl.get_accounts()
```

Withdraw from huobi pool Btc in hrc20btc chain
```
from client import Client
cl = Client(access_api_key='knt3juterjg45', secret_key='fdwr42rwefsw3r1')
response = cl.chains_information(currency='btc')
data = response['data']
for x in data:
    if x["currency"] == "btc":
        for y in x["chains"]:
            if y["chain"] == "hrc20btc":
                fee = y["transactFeeWithdraw"]
cl.withdraw(address='0xr32rhdf234rfi3', currency='btc', amount='0.0321', fee=fee)
```
