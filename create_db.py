#!/usr/bin/python

import psycopg2

def main():
	print("Hello Create DB!")
	#
	# if database does not exist, it will be created
	#
	connection = psycopg2.connect(database="postgres", user="postgres",
	password="nvidia", host="127.0.0.1", port="5432")
	#
	# enable autocommit
	#
	connection.autocommit = True
	#
	# get a connection cursor
	#
	cursor = connection.cursor()
	#
	# create a database
	#
	cursor.execute("CREATE DATABASE mydb;")
	#
    # don't forget to commit the changes
    #	
	connection.commit()
	cursor.close()
	connection.close()
	#
	# connect to the new database
	#
	connection = psycopg2.connect(database="mydb", user="postgres",
	password="RobotMan!2018", host="127.0.0.1", port="5432")
	print("connected to new database...")
	#
	# close connection when done
	#
	connection.close()
	
main()

