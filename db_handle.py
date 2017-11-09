import MySQLdb


def connectDb():

	#Please put your password

	config = {'host': 'localhost', 'username': 'root', 'password': '######', 'db': 'instawork'}

	db = MySQLdb.connect(config['host'], config['username'], config['password'], config['db'])

	return db

def allMembers(table_name):

	db = connectDb()
	cur = db.cursor()
	cur.execute('select * from {0}'.format(table_name))
	results = cur.fetchall()
	cur.close()
	return results
	# print results

def insertToDb(table_name, member_id, first_name, last_name, phone_no, email, role):

	db = connectDb()
	cur = db.cursor()
	str_insert = "insert into {0}".format(table_name) 
	status = cur.execute(str_insert+' (memberid, firstname, lastname, phonenumber, email, role) values(%s, %s, %s, %s, %s, %s)', (member_id, first_name, last_name, phone_no, email, role))
	db.commit()
	cur.close()
	print "Successfully inserted a row"
	return status

def updateDb(table_name, member_id, new_prop):

	db = connectDb()
	cur = db.cursor()

	status = ""

	for key, value in new_prop.iteritems():

		if "phone_no" in key:
			key = "phonenumber"
		if "first_name" in key:
			key = "firstname"
		if "last_name" in key:
			key = "lastname"

		query_str = "update {0} set {1}='{2}' where memberid='{3}'".format(table_name, key, value, member_id) 
		print query_str
		status = cur.execute(query_str)
	db.commit()
	cur.close()

	print "Successfully updated"
	return status

def deleteFromDb(table_name, member_id):

	db = connectDb()
	cur = db.cursor()

	query_str = "delete from {0} where memberid = '{1}'".format(table_name, member_id)

	status = cur.execute(query_str)
	print status
	db.commit()
	cur.close()

	print "Successfully deleted"
	return status

if __name__ == '__main__':

	createTable("team")

	
