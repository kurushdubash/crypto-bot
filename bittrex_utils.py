from constants import *

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
	def __init__(self, dictionary, BTC_value=0):
		self.market_name = dictionary["MarketName"]
		self.market_name_full = currency_names[self.market_name.split('-')[1]]
		self.high = float(dictionary["High"])
		self.low = float(dictionary["Low"])
		self.volume = float(dictionary["Volume"])
		self.last = float(dictionary["Last"])
		self.base_volume = float(dictionary["BaseVolume"])
		date = datetime.strptime(dictionary["TimeStamp"].split(".")[0], "%Y-%m-%dT%H:%M:%S")
		self.timestamp = date
		self.bid = float(dictionary["Bid"])
		self.ask = float(dictionary["Ask"])
		self.open_buy_orders = float(dictionary["OpenBuyOrders"])
		self.open_sell_orders = float(dictionary["OpenSellOrders"])
		self.prevday = float(dictionary["PrevDay"])
		self.created = dictionary["Created"]
		self.usd = float(BTC_value) * self.last
