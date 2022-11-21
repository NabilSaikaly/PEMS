import mysql.connector
from mysql.connector import Error 



def test_db_connection(host, database, user, password):
	"""Provided {host}, {database}, {user}, {password}
	Tests DB Connection, Shows All Databases under the specified {user}, Selects a specific DB {database}.""" 
	try:
		connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
		connection_boolean = connection.is_connected()
		if connection_boolean == True:
			database_server_info = connection.get_server_info()
			print("Successfully connected to MySQL Server.\nServer Version: ",database_server_info)

			cursor = connection.cursor()
			cursor.execute("SHOW DATABASES;")
			record = cursor.fetchall()
			print("Available DBs:", record)
			cursor.execute("SELECT database();")
			record = cursor.fetchone()
			print("Selected DB: ", record)

	except Error as CapturedError:
		print(f"Error while trying to connect to MySQL: {CapturedError}")

	finally:
		if connection_boolean == True:
			cursor.close()
			connection.close()
			print(f"MySQL Server {database_server_info} Connection is terminated.")



def insert_values(host, database, user, password, sql_insertion_query):
	"""Executes an SQL Insertion Query on the specified DB"""	
	try:
		connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
		connection_boolean = connection.is_connected()
		cursor = connection.cursor()
		cursor.execute(sql_insertion_query)
		connection.commit()
		# print(f"Query Successfully Inserted into the DB: {database} ")
		cursor.close()
	except Error as CapturedError:
		print(f"Failed to Insert the provided Query into {database}.\n [ERROR]: {CapturedError}")

	else:
		print("Successfull Insertion.")
	finally:
		if connection_boolean == True:
			connection.close()
			# print("MySQL Connection is Terminated.")


def obtain_values(host, database, user, password, sql_selection_query):
	"""Executes an SQL Selection Query on the specified DB and prints the results"""
	try:
		connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
		connection_boolean = connection.is_connected()
		cursor = connection.cursor()
		cursor.execute(sql_selection_query)
		records = cursor.fetchall()
		return records

	except Error as CapturedError:
		print(f"Error retrieving the query from the MySQL database {database}.\n [ERROR]: {CapturedError}")

	finally:
		if connection_boolean == True:
			connection.close()
			cursor.close()
			# print("MySQL Connection is Terminated.")


# Main Method
# If you want to test DBConnector alone, please speciy the host, database, user and password as variables before calling any function