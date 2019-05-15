#!/usr/bin/python

import psycopg2

def main():
	print("Hello Update Values!\n")
	connection = psycopg2.connect(database="mydb", user="postgres",
	password="nvidia", host="127.0.0.1", port="5432")
	#
	# grab the cursor
	#
	cursor = connection.cursor()
	#
	# define the table columns
	#
	columns = ["city", "temp_lo", "temp_hi", "prcp", "date"]
	#
	# define update string
	#
	update_string = """UPDATE weather SET temp_hi = temp_hi + 2,  temp_lo = temp_lo + 			2 WHERE date > '1994-11-28';"""
	#
	# modify the values by executing the update string
	#
	cursor.execute(update_string)
	#
	# commit changes
	#
	connection.commit()
	#
	# close cursor and connection when done
	#
	cursor.close()
	connection.close()
	
main()

