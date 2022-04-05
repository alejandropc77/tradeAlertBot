import requests
import urllib
import logging
from socket import timeout
from collections import defaultdict
from requests.exceptions import HTTPError, Timeout, InvalidURL
from typing import List, Dict
from time import sleep


#from requests.models import Response
#apiKey = 'YAgXXsrDFhZc4afZTfJ2s4qlJVaOmtwtLiYbBfIdBFNvFSHET3XlVahBUFJU5gxx';
#apiSecret = 'bgmV7iDyLY5H8EUb0Efpn6OpmfWgwJTYIXsUlYSSF0naavgM1BBgdeV0xzFRsbPT';
#from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager;
#client = Client(apiKey, apiSecret)
symbolName = ''

def init(symbolName):
    # get market depth
    exc_info= client.get_exchange_info()
    # get all symbol prices
    prices = client.get_all_tickers()
    avg_price = client.get_avg_price(symbol = symbolName)
    print(avg_price)
    return client

url = "http://wapi/v3/sub-account/assets.html?"

print()
print("Success")
print()
print()



