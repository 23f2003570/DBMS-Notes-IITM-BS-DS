'''
Instructions:


Note: Do not hard code the database name in your program, because your
program will be run against a different database instance for evaluation. 


For the database connection, use the following connection string variables:



database = sys.argv[1]	//name of the database is obtained from the command
line argument

user = os.environ.get('PGUSER') 
password = os.environ.get('PGPASSWORD') 
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')

Write a Python program to output the jersey number of the player.
Player's name is given in a file named 'player.txt' resides in
the same folder as python program file. 
The output of the python program is only jersey number.  
For example, if the jersey number of the player is 99. Then output
must be 99 only. Note: No spaces.

'''


import psycopg2
import os, sys

dbname = sys.argv[1]
host = os.environ.get("PGHOST")
port = os.environ.get("PGPORT")
username = os.environ.get("PGUSER")
password = os.environ.get("PGPASSWORD")


try:
    name = ''
    with open('player.txt', 'r') as fp:
        name = fp.readline().strip()

    connection = psycopg2.connect(host=host, port=port, user=username, password=password, database=dbname)
    cursor = connection.cursor()
    cursor.execute('SELECT jersey_no FROM players WHERE name=%s', (name,))
    rows = cursor.fetchall()
    
    if len(rows) > 0:
        print(rows[0][0])
        
    cursor.close()
    connection.close()
except Exception as ex:
    print(ex)
finally:
    pass