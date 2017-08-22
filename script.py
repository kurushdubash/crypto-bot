#!/usr/bin/python
from bittrex import bittrex
from constants import *

api_key = "8a3428dc510440228172f81f7d31f5bf "
api_secret = "63b790f5c5ef44c3978620bb1ecca13f"

Exchange = bittrex.Bittrex(api_key, api_secret)

def track_currency_value():
    market_summaries = Exchange.get_market_summaries()[RESULT]
    currencies = []
    bitcoin_usd_value = float(0)
    for currency in market_summaries:
        if(currency["MarketName"].split("-")[0] == "BTC"):
            currency_in_market = MarketSummary(currency);
            currencies.append(currency_in_market)
            print '"' + currency["MarketName"] + '",'
            
        if(currency["MarketName"].split("-")[0] == "USDT" \
            and currency["MarketName"].split("-")[1] == "BTC"):
            bitcoin_usd_value = float(currency["Last"])
    for item in currencies:
        item.usd = bitcoin_usd_value * item.last
    # DB.update(currencies)

# track_currency_value()
Exchange.get_deposit_history();

for item in Exchange.get_market_summaries()[RESULT]:
	value = item["MarketName"].split("-")[1]
	response = Exchange.get_deposit_address(value)
	print response
	if(response[RESULT]!=None):
		print response[RESULT]["Currecny"] + response[RESULT]["Address"]
	else:
		print "Not found for : " + value

