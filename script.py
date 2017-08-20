#!/usr/bin/python
from bittrex import bittrex
from bittrex_utils import *
from database import DataBase

api_key = "8a3428dc510440228172f81f7d31f5bf "
api_secret = "63b790f5c5ef44c3978620bb1ecca13f"


# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[0]

# db.close()

DB = DataBase(host="104.236.177.161",    # your host, usually localhost
                     user="kurush",         # your username
                     passwd="=2@fcM6LT6Vg=Exe",  # your password
                     db="crypto")        # name of the data base
Exchange = bittrex.Bittrex(api_key, api_secret)
MESSAGE = "message"
RESULT = "result"
SUCCESS = "success"

def track_currency_value():
	market_summaries = Exchange.get_market_summaries()[RESULT]
	currencies = []
	bitcoin_usd_value = float(0)
	for currency in market_summaries:
		if(currency["MarketName"].split("-")[0] == "BTC"):
			currency_in_market = MarketSummary(currency);
			currencies.append(currency_in_market)

		if(currency["MarketName"].split("-")[0] == "USDT" \
			and currency["MarketName"].split("-")[1] == "BTC"):
			bitcoin_usd_value = float(currency["Last"])
	for item in currencies:
		item.usd = bitcoin_usd_value * item.last
	DB.update(currencies)

track_currency_value()
