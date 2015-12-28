


#### MySQLdb ####

### Turn cursor result to dictionary list ###
def process_sql(cursor, add_list=None):
	if add_list:
		return_list = add_list
	else:
		return_list = []
	desc = cursor.description
	for row in cursor:
		row_dict = {}
		for (name, value) in zip(desc, row):
			row_dict[name[0]] = value
		return_list.append(row_dict)
	return return_list

def process_mongo(cursor, add_list=None):
	if add_list:
		return_list = add_list
	else:
		return_list = []
	for doc in cursor:
		return_list.append(doc)
	return return_list