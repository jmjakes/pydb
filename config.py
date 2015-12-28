# config
# for config stuff


try:
	import secure
except:
	print "secure.py not found, loading insecure.py settings"
	import insecure as secure

def get_mongo_properties():
	return secure.MONGO_ACCESS


def get_mysql_properties():
	return secure.MYSQL_ACCESS

