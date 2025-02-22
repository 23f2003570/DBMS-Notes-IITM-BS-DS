'''
Write a Python program to print the roll number of the student.
Student's first name is given in a file named 'name.txt' resides
in the same folder as python program file.
The output of the python program is only roll number.  
For example, if the first name of the student is 'Vikas'.
Then output must be CS01 only. Note: No spaces.
'''

import psycopg2, os, sys

database = sys.argv[1]
user = os.environ.get("PGUSER")
password = os.environ.get("PGPASSWORD")
host = os.environ.get("PGHOST")
port = os.environ.get("PGPORT")

fname = ''
with open('name.txt', 'r') as fp:
    fname = fp.readline().strip()
    
try:
    connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
    cursor = connection.cursor()
    cursor.execute('SELECT roll_no FROM students WHERE student_fname=%s', (fname,))
    rows = cursor.fetchall()
    print(rows[0][0])
    cursor.close()
    connection.close()
except Exception as ex:
    pass
finally:
    pass
    
    
