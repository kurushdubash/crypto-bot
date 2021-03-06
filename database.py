import MySQLdb
from bittrex_utils import *
import constants as c
from datetime import datetime

CHANGELOG_INSERT = """INSERT INTO changelog (`sql_command`, `executed`, `created_date`) VALUES (%s, %s, %s);"""

MARKET_DATA_INSERT = """INSERT INTO market_data (`market_name`, `full_name`, `last`, `usd`, `timestamp`, `low`, `high`, `volume`, `bid`, `ask`, `inserted`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

GET_ROWS_BY_FULL_NAME = """SELECT full_name, last, usd, market_name FROM market_data WHERE full_name=%s AND inserted > DATEADD(HOUR, -%s, GETDATE()) ORDER BY inserted DESC"""

class DataBase(object):
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.database = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        self.cur = self.database.cursor()

    def run_command(self, command):
        try:
            self.cur.execute(command)
            data = ("'" + command +"'", True, datetime.now())
            self.cur.execute(CHANGELOG_INSERT, data)
            self.database.commit()
        except Exception as e:
            c.log.error("Failed to run command: " + command)
            c.log.error(e)

    def check_changelog(self):
        self.cur.execute("SELECT * FROM changelog WHERE executed=0")
        for item in self.cur:
            print item[0]
            self.run_command(item[0])

    def update(self, object):
        try:
            if(isinstance(object, MarketSummary)):
                self._update_db_with_currency(object)
            if(isinstance(object, list)):
                if(len(object) > 0):
                    if(isinstance(object[0], MarketSummary)):
                        self._update_db_with_currencies(object)
        except Exception as e:
            c.log.error("Failed to find suitable type to upload to the database")
            c.log.error(object)
            c.log.error(e)

    def _update_db_with_currency(self, obj):
        try:
            data = ((obj.market_name, obj.market_name_full, obj.last, obj.usd, obj.timestamp, obj.low, obj.high, obj.volume, obj.bid, obj.ask, datetime.now()))
            self.cur.execute(MARKET_DATA_INSERT, data)
            self.database.commit()
        except Exception as e:
            c.log.error("Failed to update the db with currency : " + obj.market_name_full)
            c.log.error(e)

    def _update_db_with_currencies(self, objs):
        try:
            data = []
            for obj in objs:
                time_now = datetime.now()
                data.append((obj.market_name, obj.market_name_full, obj.last, obj.usd, obj.timestamp.strftime("%Y-%m-%dT%H:%M:%S"), obj.low, obj.high, obj.volume, obj.bid, obj.ask, time_now))
            self.cur.executemany(MARKET_DATA_INSERT, data)
            self.database.commit()
        except Exception as e:
            c.log.error("Failed to update the db with currencies : " + str(objs))
            c.log.error(e)

    def get_data(self, coin, hours):
	    data = (coin, hours)
	    self.cur.execute(GET_ROWS_BY_FULL_NAME, data)
	    for (full_name, last, usd, market_name) in self.cur:
		    print str(full_name) + ' ' + str(last) + str(usd) + str(market_name)
