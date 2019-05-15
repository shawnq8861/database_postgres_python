#!/usr/bin/python

import psycopg2

def main():
	print("Hello Query Values!\n")
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
	# build up the query string
	#
	select_string = "SELECT"
	for col in columns:
		select_string = select_string + " " + col + ","
	select_string = select_string[ :len(select_string) - 1]
	select_string = select_string + " FROM weather;"
	#
	# select all of the values from the weather table
	#
	cursor.execute(select_string)
	#
	# fetch the values returned from the query
	#
	table_rows = cursor.fetchall()
	for row in table_rows:
		col_index = 0
		for col in columns:
			print(col + ": " + str(row[col_index]))
			col_index = col_index + 1
		col_index = 0
		print("\n")
	#
	# close cursor and connection when done
	#
	cursor.close()
	connection.close()
	
main()

