
import MySQLdb
from pymongo import MongoClient
from config import get_mongo_properties, get_mysql_properties

mongo_properties = get_mongo_properties()
mysql_properties = get_mysql_properties()


def connect_mongo():
	mongo_url = "mongodb://%(user)s:%(pwd)s@%(host)s:%(port)s/%(db)s" % mongo_properties
	mongo_client = MongoClient(mongo_url)
	return mongo_client

def connect_mysql():
	mysqlclient = MySQLdb.connect(
		host=mysql_properties.get("host"),
		user=mysql_properties.get("user"),
		passwd=mysql_properties.get("pwd"),
		db=mysql_properties.get("db")
	)
	return mysqlclient
