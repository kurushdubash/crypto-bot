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


# currs = Exchange.get_market_summaries()["result"]
# currs_objs = []
# for curr in currs:
# 	currs_objs.append(MarketSummary(curr))
# for item in currs_objs:
# 	print str(item.market_name) + " : " + str(item.last)

# print ""

# for a in Exchange.get_marketsummary("BTC-ETC")["result"]: 
# 	for key, value in a.iteritems():
# 		print key 
# 		print str(value) + '\n'

# def track_currency_value():
# 	market_summaries = Exchange.get_market_summaries()[RESULT]
# 	for currency in market_summaries:
# 		currency_in_market = MarketSummary(currency);
# 		DB.update(currency_in_market)
# 		break

# track_currency_value()
# DB.run_command("CREATE TABLE test (laugh int);");
DB.run_command("DROP TABLE test;");
# DB.check_changelog()