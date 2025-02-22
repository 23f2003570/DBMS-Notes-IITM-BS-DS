# Questions:

## Q5:

Find out the number of female students in each department. (Database: LIS)

```sql
SELECT COUNT(*) AS Female_Count, D.department_name  FROM students AS S INNER JOIN departments AS D ON S.department
_code = D.department_code AND S.gender='F' GROUP BY D.department_name;
```

## Q6: 

Find the names and date-of-births of those managers who have joined in years 2019 and
2020. (Database: FLIS)

```sql
SELECT name, dob FROM managers WHERE TO_CHAR(SINCE,'YYYY') IN ('2019', '2020');
```

## Q7:
```
Find the names of all those teams where the last name of the team starts with the letter S. Use the name attribute of the teams table to answer this question. (Database: FLIS)
```
```sql
SELECT name FROM teams WHERE name LIKE '%S'
```

Q8:



---


## Mock Tests

### Q1:

**Q005flisdb: Write an SQL query to find the name of the city of teams whose home jersey color is 'Red'. [Database: FLIS] flisdb:**


```SQL
SELECT city FROM teams WHERE jersey_home_color='Red'
```

### Q2:

**Q002flisdb: Write an SQL query to find the player IDs of the players whose name ends with 'a'.[Database: FLIS] flisdb:**

```SQL
SELECT player_id FROM players WHERE name LIKE '%a'
```

### Q3:

**Q001flisdb: Write an SQL query to find the match dates where the host team score is not between 1 and 4.[Database: FLIS] flisdb:**

```sql
SELECT match_date FROM matches WHERE host_team_score NOT BETWEEN 1 AND 4
```

### Q4

**Q001flisdb:Write an SQL query to find the name of the manager of team 'Arawali'.[Database: FLIS] flisdb:**

```sql
SELECT M.name FROM managers AS M INNER JOIN teams as T
ON M.team_id = T.team_id
WHERE T.name = 'Arawali'
```


### Q5

**Q010flisdb:Write an SQL query to find the name and the dob(date of birth) of the youngest player of the team 'Thunder'. [Database: FLIS] flisdb:**

```sql
SELECT P.name, P.dob FROM players AS P
INNER JOIN teams AS T ON P.team_id = T.team_id
WHERE T.name='Thunder'
ORDER BY P.dob ASC
LIMIT 1


SELECT P.name, P.dob FROM players AS P
INNER JOIN teams AS T ON P.team_id = T.team_id
WHERE T.name='Thunder' AND P.dob = (SELECT max(P.dob) FROM players AS P INNER JOIN teams AS T  ON P.team_id = T.team_id WHERE T.name='Thunder');
```

### Q6

**Q002flisdb: Write an SQL query to print the name, the jersey number, team ID and the name of the manager (of the team) of each player whose jersey number is not the given numbers (44,88,55,65,17). Note that the players could be of different teams. [Database: FLIS] flisdb:**

```sql
SELECT P.name, P.jersey_no, P.team_id, M.name FROM players as P 
INNER JOIN teams AS T ON T.team_id = P.team_id
INNER JOIN managers AS M ON M.team_id = T.team_id
WHERE P.jersey_no NOT IN (44,88,55,65,17)
```


### Q7

**Q002flisdb: Write an SQL query to find the name, dob and the respective team name and the manager name of each player whose jersey number is '39'.[Database: FLIS] flisdb:**

```sql
SELECT P.name, P.dob, T.name, M.name FROM players AS P
INNER JOIN managers AS M ON M.team_id = P.team_id
INNER JOIN teams AS T ON T.team_id = P.team_id
WHERE P.jersey_no = 39
```

## Q8

```
Instructions:

Note: Do not hard code the database name in your program, because your program will be run against a different database instance for evaluation. 

For the database connection, use the following connection string variables:


database = sys.argv[1]	//name of the database is obtained from the command line argument
user = os.environ.get('PGUSER') 
password = os.environ.get('PGPASSWORD') 
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')
```

**Problem Statement:**

Write a Python program to print the ISBN numbers of books which are published in a given year. Here, the year is obtained as the value of function L(x) (given after the sample output) at x. You have to read the value of x from the input file "number.txt", and use it to find the value of L(x). Your program must assume that the file number.txt resides in the same folder as your Python program.


You have to iterate through the list and print each value separately as shown in the output below: 

9789352921171
9789351343202
9789353333380
The line function is given below:
L5(x) = 2000 + 5*x + 5


```py
import sys, os, psycopg2

database=sys.argv[1]
user = os.environ.get('PGUSER') 
password = os.environ.get('PGPASSWORD') 
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')


def Lx(num):
    return 2000 + (5 * num) + 5

try:
    num = 0
    with open('number.txt', 'r') as fp:
        num = int(fp.readline().strip())
    
    year = Lx(num)
    
    connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    
    cursor = connection.cursor()
    cursor.execute('SELECT ISBN_no FROM book_catalogue WHERE year=%s', (year,))
    rows = cursor.fetchall()
    
    for row in rows:
        print(f'{row[0]}')
    
    
    

except Exception as ex:
    print(ex)
finally:
    pass
```


## Q9

```
In this question, you must write a Python program to output the name of the main referee for a given match date (in yyyy-mm-dd format). The input to your program is a file named “date.txt” that has the match date as the first word of the file. Your program must assume that date.txt resides in the same folder as your Python program. 


The output name has to be formatted as follows. The last name is displayed followed by the initials of the first name, then a full stop, a space and then the initials of the middle name (if the middle name exists), followed by a full stop.

For example, if the name of the main referee is “Kennedy Sapam”, the output must be ”Sapam K.” 

If the name of the main referee is “Asit Kumar Sarkar”, the output must be ”Sarkar A. K.”
```

