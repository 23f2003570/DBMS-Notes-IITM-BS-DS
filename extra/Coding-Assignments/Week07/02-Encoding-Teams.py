'''
In this problem, you have to write a Python program to print
an encoding of the ids of the teams whose jersey colour at home
is different from the jersey colour when they play away from home.


The encoding must be using a shift cipher, which is detailed below.

An alphabet is mapped to another alphabet as follows. For a given alphabet α,
let pos be the position at which α occurs in the alphabet 
listing (A at 1, B at 2, …. Z at 26). Then the encoding of α is
the alphabet at the position (pos + 7) mod 26.

For example, if M is the alphabet, then the position at which M occurs
in the alphabet listing is 13. Then, the encoding of M is the
alphabet at the position (13 + 7) mod 26 = 20, which is T. 

For each digit β, the encoding of β is (β+7) mod 10.

For example, if 3 is the digit, then the encoding of 3 is the number
(3 + 7) mod 10 = 0.

The ids should be listed in the ascending order before performing the encoding.

Each line in the output of the program must correspond to one row retrieved
from the table.
'''


import psycopg2
import os, sys

dbname = sys.argv[1]
pghost = os.environ.get('PGHOST')
pgport = os.environ.get('PGPORT')
pguser = os.environ.get('PGUSER')
pgpassword = os.environ.get('PGPASSWORD')

try:
    connection = psycopg2.connect(database=dbname, host=pghost, port=pgport, user=pguser, password=pgpassword)
    cursor = connection.cursor()
    cursor.execute('SELECT team_id FROM teams WHERE jersey_home_color <> jersey_away_color ORDER BY team_id ASC')
    rows = cursor.fetchall()
    for row in rows:
        team_id = row[0]
        encoded_team_id = ''
        for c in team_id:
            if c.isalpha():
                encoded_team_id += chr(ord('A') + ((ord(c) - ord('A') + 1 + 7) % 26))
            elif c.isnumeric():
                encoded_team_id += chr(ord('0') + ((ord(c) - ord('0') + 1 + 7) % 10))
        print(encoded_team_id)
    
    cursor.close()
    connection.close()
    
except Exception as ex:
    print('Exception: ' + ex)
finally:
    pass