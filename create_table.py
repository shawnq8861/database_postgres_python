#!/usr/bin/python

import psycopg2

def main():
	print("Hello Create Table!")
	connection = psycopg2.connect(database="mydb", user="postgres",
	password="RobotMan!2018", host="127.0.0.1", port="5432")
	print("connected to database...")
	#
	# grab the cursor
	#
	cursor = connection.cursor()
	#
	# create weather table
	#
	create_table = """CREATE TABLE weather (
		city            varchar(80), 
		temp_lo         int,           -- low temperature
    	temp_hi         int,           -- high temperature
    	prcp            real,          -- precipitation
    	date            date);"""
	cursor.execute(create_table)
	#
	# create cities table
	#
	create_table = """CREATE TABLE cities (
    	name            varchar(80),
    	location        point);"""
	cursor.execute(create_table)
    #
    # don't forget to commit the changes
    #
	connection.commit()
	print("table created...")
	#
	# close connection when done
	#
	cursor.close()
	connection.close()
	
main()

