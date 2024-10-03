# PostgreSQL Commands

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