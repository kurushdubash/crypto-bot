from decimal import Decimal
from datetime import datetime
from constants import currency_names


class Currency(object):
	def __init__(self, dictionary):
		self.currency = dictionary["Currency"]
		self.currency_long = dictionary["CurrencyLong"]
		self.min_confirmation = dictionary["MinConfirmation"]
		self.tx_fee = dictionary["TxFee"]
		self.is_active = dictionary["IsActive"]
		self.coin_type = dictionary["CoinType"]
		self.base_address =dictionary["BaseAddress"]

class MarketSummary(object):
	def __init__(self, dictionary, BTC_value):
		self.market_name = dictionary["MarketName"]
		self.market_name_full = currency_names(self.market_name.split('-')[1])
		self.high = Decimal(dictionary["High"])
		self.low = Decimal(dictionary["Low"])
		self.volume = Decimal(dictionary["Volume"])
		self.last = Decimal(dictionary["Last"])
		self.base_volume = Decimal(dictionary["BaseVolume"])
		date = datetime.strptime(dictionary["TimeStamp"], "%Y-%B-%dT%H:%M:%S.%M").date()
		self.timestamp = date
		self.bid = Decimal(dictionary["Bid"])
		self.ask = Decimal(dictionary["Ask"])
		self.open_buy_orders = Decimal(dictionary["OpenBuyOrders"])
		self.open_sell_orders = Decimal(dictionary["OpenSellOrders"])
		self.prevday = Decimal(dictionary["PrevDay"])
		self.created = dictionary["Created"]
		self.usd = Decimal(BTC_value) * self.last 
