#!/usr/bin/python
from bittrex import bittrex
from database import DataBase
from bittrex_utils import Currency, MarketSummary
import threading

api_key = "8a3428dc510440228172f81f7d31f5bf"
api_secret = "63b790f5c5ef44c3978620bb1ecca13f"

api_key2 = "5e5ce42fefd54684839945e6c4bba6b0"
api_secret2 = "39b25eb11a9240eab984b0f2a6074e02"
Exchange = bittrex.Bittrex(api_key, api_secret)

DB = DataBase(host="104.236.177.161",    # your host, usually localhost
                     user="kurush",         # your username
                     passwd="=2@fcM6LT6Vg=Exe",  # your password
                     db="crypto")        # name of the data base

import constants as c

def track_currency_value(delimeter="BTC"):
    threading.Timer(5.0, track_currency_value).start()
    market_summaries = Exchange.get_market_summaries()[c.RESULT]
    currencies = []
    bitcoin_usd_value = float(0)
    for currency in market_summaries:
        symbol_buy = currency["MarketName"].split("-")[0]
        symbol_sell = currency["MarketName"].split("-")[1]
        if(symbol_buy == delimeter and symbol_sell in c.top_100):
            currency_in_market = MarketSummary(currency);
            currencies.append(currency_in_market)

        if(symbol_buy == "USDT" \
            and symbol_sell == "BTC"):
            bitcoin_usd_value = float(currency["Last"])
    for item in currencies:
        item.usd = bitcoin_usd_value * item.last
    DB.update(currencies)

track_currency_value()

