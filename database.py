import MySQLdb
from bittrex_utils import *
import time
from datetime import datetime

CHANGELOG_INSERT = """INSERT INTO changelog (`sql_command`, `executed`, `created_date`) VALUES (%s, %s, %s);"""

MARKET_DATA_INSERT = """INSERT INTO market_data (`market_name`, `last`, `timestamp`, `low`, `high`, `volume`, `bid`, `ask`, `inserted`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

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
            print "Failed to execute command : " + command
            raise e

    def check_changelog(self):
        self.cur.execute("SELECT * FROM changelog WHERE executed=0")
        for item in self.cur:
            print item[0]
            # self.run_command(item[0])

    def update(self, object):
        if(isinstance(object, MarketSummary)):
            self._update_db_with_currency(object)

    def _update_db_with_currency(self, obj):
        data = (obj.market_name, obj.last, obj.timestamp, obj.low, obj.high, obj.volume, obj.bid, obj.ask, datetime.now())
        self.cur.execute(MARKET_DATA_INSERT, data)
        self.database.commit()
        