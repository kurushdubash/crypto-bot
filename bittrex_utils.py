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
	def __init__(self, dictionary):
		self.market_name = dictionary["MarketName"]
		self.high = dictionary["High"]
		self.low = dictionary["Low"]
		self.volume = dictionary["Volume"]
		self.last = dictionary["Last"]
		self.base_volume = dictionary["BaseVolume"]
		self.timestamp = dictionary["TimeStamp"]
		self.bid = dictionary["Bid"]
		self.ask = dictionary["Ask"]
		self.open_buy_orders = dictionary["OpenBuyOrders"]
		self.open_sell_orders = dictionary["OpenSellOrders"]
		self.prevday = dictionary["PrevDay"]
		self.created = dictionary["Created"]
		# self.display_market_name = dictionary["DisplayMarketName"]