#!/usr/bin/python
from bittrex import bittrex
from database import DataBase
from bittrex_utils import Currency, MarketSummary
import threading

api_key = ""
api_secret = ""

api_key2 = ""
api_secret2 = ""
Exchange = bittrex.Bittrex(api_key, api_secret)

DB = DataBase(host="",    # your host, usually localhost
                     user="kurush",         # your username
                     passwd="",  # your password
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

