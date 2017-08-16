import MySQLdb
from bittrex_utils import *

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