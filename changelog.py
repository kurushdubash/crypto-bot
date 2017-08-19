from database import DataBase 

DB = DataBase(host="104.236.177.161",    # your host, usually localhost
                     user="kurush",         # your username
                     passwd="=2@fcM6LT6Vg=Exe",  # your password
                     db="crypto")        # name of the data base

QUERIES = []
for item in QUERIES:
	DB.run_command(QUERIES)
