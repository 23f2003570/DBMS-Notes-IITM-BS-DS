# PostgreSQL Commands

## Setting up PostgreSQL with Docker

1. add a user called `postgres:postgres` with id `999:999`
   - for Why? check this Dockerfile https://hub.docker.com/layers/library/postgres/10.18/images/sha256-e37849ff3307519e542e6ad13ae3aa2ab8131e448df126f0f86d2c38980c31da?context=explore
   - the text name of user/group is not important but it has to have uid:gid as 999:999

### MacOSX Notes

To install PG client Tools

```sh
brew doctor
brew update
brew install libpq

psql --host localhost --port 5432 --password --username dbuser --dbname dbname
```
To create a user and group with a specific ID (`999:999`) on macOS, you can use the following steps. Note that you'll need administrator (sudo) privileges.

#### 1. **Create a Group with a Specific GID (999):**
To create a group with the `GID` of `999`, use the `sudo` command with `dscl` (Directory Service command-line utility):

```bash
sudo dscl . -create /Groups/postgres
sudo dscl . -create /Groups/postgres PrimaryGroupID 999
```

#### 2. **Create a User with a Specific UID (999):**
To create a user with a `UID` of `999`, follow these steps:

```bash
sudo dscl . -create /Users/postgres
sudo dscl . -create /Users/postgres UserShell /bin/bash
sudo dscl . -create /Users/postgres RealName "PostgreSQL"
sudo dscl . -create /Users/postgres UniqueID 999
sudo dscl . -create /Users/postgres PrimaryGroupID 999
sudo dscl . -create /Users/postgres NFSHomeDirectory /opt/postgres
```

#### 3. **Set a Password for the User:**
To set a password for the new user:

```bash
sudo passwd postgres

################################### WARNING ###################################
# This tool does not update the login keychain password.                      #
# To update it, run `security set-keychain-password` as the user in question, #
# or as root providing a path to such user's login keychain.                  #
###############################################################################
```

#### 4. **Create a Home Directory (Optional):**
If you want to create the home directory for the user:

```bash
sudo mkdir /opt/postgres
sudo chown postgres:postgres  /opt/postgres
```

This creates a home directory at ` /opt/postgres` and sets the correct ownership.

## Connecting

## List Databases

```sh
$ \l
                              List of databases
   Name    | Owner  | Encoding |  Collate   |   Ctype    | Access privileges
-----------+--------+----------+------------+------------+-------------------
 dbuser    | dbuser | UTF8     | en_US.utf8 | en_US.utf8 |
 postgres  | dbuser | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | dbuser | UTF8     | en_US.utf8 | en_US.utf8 | =c/dbuser        +
           |        |          |            |            | dbuser=CTc/dbuser
 template1 | dbuser | UTF8     | en_US.utf8 | en_US.utf8 | =c/dbuser        +
           |        |          |            |            | dbuser=CTc/dbuser
```
## Create Database
```sql
CREATE DATABASE Company;    # postgres makes it lower case
```

## Connect to a Database
```sh
$ \c databasename #always lower case OR FATAL:  database "Myenterprise" does not exist
```

## Creating Relations

```sh
$ \d
#Did not find any relations.

$ CREATE TABLE Department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL);

$ CREATE TABLE Employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    dept_id INT REFERENCES Department(id));

$ INSERT INTO Department (id, name) VALUES (1, "Computer Science"); # ERROR:  column "Computer Science" does not exist. Single quotes please
$ INSERT INTO Department (id, name) VALUES (1, 'Mechanical Engineering'); # ERROR:  duplicate key value violates unique constraint "department_pkey"
$ INSERT INTO Department (name) VALUES ('Mechanical Engineering'); # OK id 2
$ INSERT INTO Department (id, name) VALUES (null, 'Chemical Engineering'); # ERROR:  null value in column "id" violates not-null constraint
$ INSERT INTO Department (name) VALUES ('Chemical Engineering'); # OK id 3 (not 6)
$ INSERT INTO Department (name) VALUES ('Industrial Production Engineering'); # OK id-4
$ INSERT INTO Department (name) VALUES ('Electrical Engineering'); # ERROR:  duplicate key value violates unique constraint "department_pkey", DETAIL:  Key (id)=(5) already exists.
$ INSERT INTO Department (name) VALUES ('Electrical Engineering'); # OK !!!! id = 6
$ INSERT INTO Employee (name, dept_id) VALUES ('Prof. Andrew Thangaraj', 6);
$ INSERT INTO Employee (name, dept_id) VALUES ('Prof. Nitin Chandrachoodan',6);
$ INSERT INTO Employee (name, dept_id) VALUES ('Prof. Partha Pratim Das',1);

```

## Cartesian Product
```sql
SELECT e.name, d.name from employee as e, department as d;
```
```sh
            name            |               name
----------------------------+-----------------------------------
 Prof. Andrew Thangaraj     | Computer Science
 Prof. Nitin Chandrachoodan | Computer Science
 Prof. Partha Pratim Das    | Computer Science
 Prof. Andrew Thangaraj     | Mechanical Engineering
 Prof. Nitin Chandrachoodan | Mechanical Engineering
 Prof. Partha Pratim Das    | Mechanical Engineering
 Prof. Andrew Thangaraj     | Aerospace Engineering
 Prof. Nitin Chandrachoodan | Aerospace Engineering
 Prof. Partha Pratim Das    | Aerospace Engineering
 Prof. Andrew Thangaraj     | Chemical Engineering
 Prof. Nitin Chandrachoodan | Chemical Engineering
 Prof. Partha Pratim Das    | Chemical Engineering
 Prof. Andrew Thangaraj     | Industrial Production Engineering
 Prof. Nitin Chandrachoodan | Industrial Production Engineering
 Prof. Partha Pratim Das    | Industrial Production Engineering
 Prof. Andrew Thangaraj     | Electrical Engineering
 Prof. Nitin Chandrachoodan | Electrical Engineering
 Prof. Partha Pratim Das    | Electrical Engineering
(18 rows)
```

## INNER/NATURAL JOIN

## Truncate

The `TRUNCATE` command in SQL is used to remove all rows from a table quickly and efficiently. Here are some key points about the `TRUNCATE` command:

1. **Data Removal**: `TRUNCATE` deletes all rows in a table, but the table structure, including its columns, constraints, and indexes, remains intact.

2. **Performance**: `TRUNCATE` is generally faster than `DELETE` because it doesn't log individual row deletions. Instead, it logs the page deallocations, making it more efficient for large tables.

3. **Cannot Use WHERE Clause**: Unlike `DELETE`, `TRUNCATE` cannot filter rows based on a condition. It always removes all rows.

4. **Cannot Be Used with Indexed Views**: `TRUNCATE` cannot be used on tables that are referenced by foreign key constraints unless those constraints are dropped or disabled.

5. **Resets Identity Columns**: If the table has an identity column, truncating the table will reset the identity counter to the seed value defined for that column.

6. **Transaction Behavior**: `TRUNCATE` is a DDL (Data Definition Language) command and, in most databases, cannot be rolled back if executed outside of a transaction. However, within a transaction, it can be rolled back if not yet committed.

#### Example
```sql
TRUNCATE TABLE employees;
```

This command would remove all records from the `employees` table without affecting its structure.


## ALTER TABLE

```sql
ALTER TABLE no_primary DROP column_name;
ALTER TABLE no_primary DROP CONSTRAINT constraint_name;
```

## Correlation Name

```sql
SELECT DISTINCT T.name
FROM instructor AS T, instructor AS S
WHERE T.salary > S.salary AND S.dept_name = 'Biology';
```

An identifier, such as T and S, that is used to rename a relation is referred to as a `correlation name` in the SQL standard, but it is also commonly referred to as a *table alias*, or a *correlation variable*, or a *tuple variable*.

## Order By

- By default, the order by clause lists items in ascending order.
- To specify the sort order, we may specify desc for descending order or asc for ascending order.

```sql
SELECT *
FROM instructor
ORDER BY salary DESC, name asc;
```

## Where Clause Predicates

```SQL
WHERE salary BETWEEN 90000 AND 100000;
WHERE salary <= 100000 AND salary >= 90000;
WHERE instructor.ID=teaches.ID AND dept_name = 'Biology';
WHERE (instructor.ID, dept_name) = (teaches.ID, 'Biology'); --ORACLE DOES NOT SUPPORT THIS
WHERE salary IS NULL;
WHERE salary > 10000 IS UNKNOWN;
```

## Predicates
- IS NULL
- IS NOT NULL
  
## SET OPERATIONS

- union (OR), intersect (AND), and except (DIFFERENCE)
- The union operation automatically eliminates duplicates, unlike the `select` clause. Use `UNION ALL` to retain duplicates
- Intersect is an AND. Not supported by MYSQL. Use sub queries instead
  - The intersect operation automatically eliminates duplicates 
  - Use `INTERSECT ALL` to retain duplicates
- The `EXCEPT` operation outputs all tuples from its first input that do not occur in the second input;
  - its a SET DIFFERENCE
  - Oracle uses `minus` keyword
  - Use `EXCEPT ALL` to retain duplicates

## NULL VALUES
- The result of an arithmetic expression (involving, for example, +, −, ∗, or ∕) is null if any of the input values is null
- SQL therefore treats as `unknown` the comparison result of any comparison involving a null value
  - 1 < null is unknown
  - AND: The result of true and unknown is unknown, false and unknown is false, while unknown and unknown is unknown.
  - OR: The result of true or unknown is true, false or unknown is unknown, while unknown or unknown is unknown.
  - NOT: The result of not unknown is unknown.

## AGGREGATE FUNCTIONS 

Aggregate functions are functions that take a collection (a set or multiset) of values as input and return a single value. SQL offers five standard built-in aggregate functions:9

- Average: avg
- Minimum: min
- Maximum: max
- Total: sum
- Count: count
- select count (distinct ID)
- avoid aggregated attributes in GROUP BY

### Find the average salary in each department.

```sql
SELECT dept_name, avg(salary) AS avg_salary
FROM instructor
GROUP BY dept_name;
```

### Erroneous Query
```sql
/* erroneous query */
select dept name, ID, avg (salary)
from instructor
group by dept name;

-- ID is not in the GROUP BY
```

### Find the number of instructors in each department who teach a course in the Spring 2018 semester.

**dept_name|instr_count**

```sql

SELECT C.dept_name, count(T.id)
FROM course AS C, teaches AS T
WHERE T.semester = 'Spring' AND T.year = 2008
GROUP BY C.dept_name
```