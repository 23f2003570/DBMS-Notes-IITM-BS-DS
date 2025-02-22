'''
In this question, you have to write a Python program to print
the names of the players and the team of each player of all
those players whose jersey number is a prime number. 

The list should be ordered in reverse alphabetical order of
player names. If two or more players have the same name, then
further sorting should be done on the team name, again in
reverse alphabetical order.

The format of output is as given below:

Name of the player, followed by a comma (,), then a space
and then the team name.


For example, if Arjun has jersey number 5 and is playing for
All Stars and Pranav, with jersey number 7,is playing for
team Amigos, then the output will be:

Pranav, Amigos

Arjun, All Stars
'''


import psycopg2
import sys
import os

def isprime(n):
    if n <= 1:
        return False
    for i in range(1, (n//2)+1):
        if i != 1:
            if n % i == 0:
                return False
    return True

try:
    dbname = sys.argv[1]
    user = os.environ.get('PGUSER')
    password = os.environ.get('PGPASSWORD')
    host = os.environ.get('PGHOST')
    port = os.environ.get('PGPORT')
    
    connection = psycopg2.connect(database=dbname, user=user, password=password, host=host, port=port)
    cursor = connection.cursor()
    
    cursor.execute('SELECT p.jersey_no, p.name, t.name FROM players AS p INNER JOIN teams AS t ON p.team_id = t.team_id ORDER BY p.name DESC;')
    rows = cursor.fetchall()
    
    for row in rows:
        if isprime(row[0]):
            print(f'{row[1]}, {row[2]}')
    cursor.close()
    connection.close()
    
except Exception as e:
    print(e)
finally:
    pass

    
'''
CORRECT CODE
Tanish, Thunder
Steven, All Stars
Srihan, Thunder
Shlok, Amigos
Rudrash, Thunder
Raghav, Thunder
Paul, All Stars
Michael, Arawali
Manas, Thunder
Madhav, Amigos
Joshua, All Stars
Jerry, All Stars
James, Black Eagles
George, Black Eagles
Finley, Black Eagles
Charles, All Stars
Bhaskar, Thunder
Alexander, Black Eagles
Ahmed, Amigos
Advik, Amigos
Adi, Amigos
============================
Creating new PostgreSQL cluster 10/regress ...
/usr/lib/postgresql/10/bin/initdb -D /pg_virtualenv.4W0A4d/data/10/regress --auth-local peer --auth-host md5 --username=nsjail --pwfile=/pg_virtualenv.4W0A4d/postgresql-common/pwfile --nosync
The files belonging to this database system will be owned by user "nsjail".
This user must also own the server process.

The database cluster will be initialized with locale "C.UTF-8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /pg_virtualenv.4W0A4d/data/10/regress ... ok
creating subdirectories ... ok
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default timezone ... Etc/UTC
selecting dynamic shared memory implementation ... posix
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok

Sync to disk skipped.
The data directory might become corrupt if the operating system crashes.

Success. You can now start the database server using:

    /usr/lib/postgresql/10/bin/pg_ctl -D /pg_virtualenv.4W0A4d/data/10/regress -l logfile start

Warning: The parent /var/run/postgresql of the selected
stats_temp_directory does not exist. Not adding this setting in
postgresql.conf.
Ver Cluster Port Status Owner  Data directory                        Log file
10  regress 5432 online nsjail /pg_virtualenv.4W0A4d/data/10/regress /pg_virtualenv.4W0A4d/log/postgresql-10-regress.log

DROP DATABASE
CREATE DATABASE
CREATE ROLE
END_OF_INSIDE_VIRTUALENV
Dropping cluster 10/regress ...
'''