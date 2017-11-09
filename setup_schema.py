import MySQLdb

def connectDb():

	#Please put your password

	config = {'host': 'localhost', 'username': 'root', 'password': 'sonudeb', 'db': 'instawork'}

	db = MySQLdb.connect(config['host'], config['username'], config['password'], config['db'])

	return db

def createTable(tablename):

	db = connectDb()

	bool_val = checkTableExists(db, tablename)

	if bool_val == False:
		dbcur = db.cursor()
		sql_query = """CREATE TABLE {0} (memberid varchar(35) PRIMARY KEY, firstname varchar(50), lastname varchar(50), phonenumber varchar(50), email varchar(100), role TEXT )""".format(tablename)
		dbcur.execute(sql_query)
		db.commit()
		print "Table created successfully"
		return "True"
	else:
		print "Table already exist"
		return "False"


def checkTableExists(dbcon, tablename):
	dbcur = dbcon.cursor()
	dbcur.execute("""
		SELECT COUNT(*)
		FROM information_schema.tables
		WHERE table_name = '{0}'
		""".format(tablename))
	if dbcur.fetchone()[0] == 1:
		dbcur.close()
		return True

	dbcur.close()
	return False

if __name__ == '__main__':
	
	resp = createTable("teamtest")

	if resp == "True":

		print "Successfully created table"

	else:
		print "Some issues found"