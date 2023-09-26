from trade_script import *

client = AlpacaClient(config.API_KEY, config.SECRET_KEY, paper=True)
account = dict(client.get_account())
for k,v in account.items():
    print(f"{k:30}{v}")