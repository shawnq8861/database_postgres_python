#!/usr/bin/python

import psycopg2

def main():
	print("Hello Insert Values!")
	connection = psycopg2.connect(database="mydb", user="postgres",
	password="nvidia", host="127.0.0.1", port="5432")
	print("connected to database...")
	#
	# grab the cursor
	#
	cursor = connection.cursor()
	#
	# insert values into weather table, implied column order
	#
	weather_values = """INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, 			'1994-11-27');"""
	cursor.execute(weather_values)
	#
	# insert values into weather table with column names
	#
	weather_values = """INSERT INTO weather (city, temp_lo, temp_hi, prcp, date) 			VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29');"""
	cursor.execute(weather_values)
	weather_values = """INSERT INTO weather (date, city, temp_hi, temp_lo) VALUES 			('1994-11-29', 'Hayward', 54, 37);"""
	cursor.execute(weather_values)
	#
	# insert values into cities without column names
	#
	cities_values = """INSERT INTO cities VALUES ('San Francisco', '(-194.0, 			53.0)');"""
	cursor.execute(cities_values)
    #
    # don't forget to commit the changes
    #
	connection.commit()
	print("values inserted...")
	#
	# close cursor and connection when done
	#
	cursor.close()
	connection.close()
	
main()

