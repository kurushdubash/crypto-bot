from database import DataBase 

DB = DataBase(host="",    # your host, usually localhost
                     user="kurush",         # your username
                     passwd="",  # your password
                     db="crypto")        # name of the data base

QUERIES = []
for item in QUERIES:
	DB.run_command(QUERIES)
