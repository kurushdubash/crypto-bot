import MySQLdb
from bittrex_utils import *
import time
from datetime import datetime

CHANGELOG_INSERT = """INSERT INTO changelog (`sql_command`, `executed`, `created_date`) VALUES (%s, %s, %s);"""

# # Use all the SQL you like
# cur.execute("SELECT * FROM YOUR_TABLE_NAME")

class DataBase(object):
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.database = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        self.cur = self.database.cursor()

    def run_command(self, command):
        # try:
        # print self.cur.execute(command)
        data = ("'" + command +"'", True, datetime.now())
        self.cur.execute(CHANGELOG_INSERT, data)
        self.database.commit()
        # except Exception as e:
        #     raise e
        #     print "Failed to execute command : " + command

    def check_changelog(self):
        self.cur.execute("SELECT * FROM changelog WHERE executed=0")
        for item in self.cur:
            print item[0]
            # self.run_command(item[0])

    def update(self, object):
        if(isinstance(object, MarketSummary)):
            self._update_db_with_currency(object)

    def _update_db_with_currency(self, object):
        values = ""
        for key, value in vars(object).iteritems():
            if not key.startswith("__"):
                values += str(value) + ", "
        values = values[:-2]
        print values
        query = "INSERT INTO market_currencies VALUES (" + values + ");"
        print query
        # cur.execute(query)