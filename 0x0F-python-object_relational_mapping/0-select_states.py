#!/usr/bin/python3
"""  Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb;

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd = "root", db="My_db", charset="utfs")
