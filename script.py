# Main script

# imports
from dbconnect import connect_mongo, connect_mysql
from dbsupport import process_sql, process_mongo
import sys

# Any helper methods?

if __name__ == "__main__":


	# connect
	try:
		sql_client = connect_mysql()
		mongo_client = connect_mongo()
	except Exception as ex:
		print "FAILED TO CONNECT TO DATABASES"
		print ex
		sys.exit()

	try:
		print "do some stuff"
	except Exception as ex:
		print "SOMETHING WENT WRONG:"
		print ex
	finally:
		sql_client.close()
		mongo_client.close()

	